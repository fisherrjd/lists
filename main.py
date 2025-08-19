from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import SQLModel, Field, Session, create_engine, select

from typing import List, Optional

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# SQLModel models
class GroceryList(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class GroceryItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    quantity: int
    list_id: int = Field(foreign_key="grocerylist.id")


# SQLite setup
sqlite_file_name = "/app/dbdata/grocery.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=False)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, list_name: str = "regular"):
    with Session(engine) as session:
        lists = session.exec(select(GroceryList)).all()
        selected_list = session.exec(
            select(GroceryList).where(GroceryList.name == list_name)
        ).first()
        items = []
        if selected_list:
            items = session.exec(
                select(GroceryItem).where(GroceryItem.list_id == selected_list.id)
            ).all()
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "list_name": list_name,
                "lists": [l.name for l in lists],
                "items": items,
            },
        )


@app.get("/groceries/{list_name}", response_model=List[GroceryItem])
def get_groceries(list_name: str):
    with Session(engine) as session:
        grocery_list = session.exec(
            select(GroceryList).where(GroceryList.name == list_name)
        ).first()
        if not grocery_list:
            raise HTTPException(status_code=404, detail="List not found.")
        items = session.exec(
            select(GroceryItem).where(GroceryItem.list_id == grocery_list.id)
        ).all()
        return items


@app.post("/groceries/{list_name}", response_model=GroceryItem)
def add_grocery(list_name: str, item: GroceryItem):
    with Session(engine) as session:
        grocery_list = session.exec(
            select(GroceryList).where(GroceryList.name == list_name)
        ).first()
        if not grocery_list:
            raise HTTPException(status_code=404, detail="List not found.")
        item.list_id = grocery_list.id
        session.add(item)
        session.commit()
        session.refresh(item)
        return item


@app.put("/groceries/{list_name}/{item_id}", response_model=GroceryItem)
def update_grocery(list_name: str, item_id: int, item: GroceryItem):
    with Session(engine) as session:
        grocery_list = session.exec(
            select(GroceryList).where(GroceryList.name == list_name)
        ).first()
        if not grocery_list:
            raise HTTPException(status_code=404, detail="List not found.")
        db_item = session.exec(
            select(GroceryItem).where(
                GroceryItem.id == item_id, GroceryItem.list_id == grocery_list.id
            )
        ).first()
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found.")
        db_item.name = item.name
        db_item.quantity = item.quantity
        session.add(db_item)
        session.commit()
        session.refresh(db_item)
        return db_item


@app.delete("/groceries/{list_name}/{item_id}")
def delete_grocery(list_name: str, item_id: int):
    with Session(engine) as session:
        grocery_list = session.exec(
            select(GroceryList).where(GroceryList.name == list_name)
        ).first()
        if not grocery_list:
            raise HTTPException(status_code=404, detail="List not found.")
        db_item = session.exec(
            select(GroceryItem).where(
                GroceryItem.id == item_id, GroceryItem.list_id == grocery_list.id
            )
        ).first()
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found.")
        session.delete(db_item)
        session.commit()
        return {"detail": "Item deleted"}


@app.post("/add", response_class=RedirectResponse)
def add_item(
    request: Request,
    list_name: str = Form(...),
    name: str = Form(...),
    quantity: int = Form(...),
):
    with Session(engine) as session:
        grocery_list = session.exec(
            select(GroceryList).where(GroceryList.name == list_name)
        ).first()
        if not grocery_list:
            grocery_list = GroceryList(name=list_name)
            session.add(grocery_list)
            session.commit()
            session.refresh(grocery_list)
        item = GroceryItem(name=name, quantity=quantity, list_id=grocery_list.id)
        session.add(item)
        session.commit()
    return RedirectResponse(f"/?list_name={list_name}", status_code=303)


@app.post("/delete", response_class=RedirectResponse)
def delete_item(list_name: str = Form(...), id: int = Form(...)):
    with Session(engine) as session:
        grocery_list = session.exec(
            select(GroceryList).where(GroceryList.name == list_name)
        ).first()
        if grocery_list:
            db_item = session.exec(
                select(GroceryItem).where(
                    GroceryItem.id == id, GroceryItem.list_id == grocery_list.id
                )
            ).first()
            if db_item:
                session.delete(db_item)
                session.commit()
    return RedirectResponse(f"/?list_name={list_name}", status_code=303)


@app.post("/create_list", response_class=RedirectResponse)
def create_list(request: Request, new_list_name: str = Form(...)):
    with Session(engine) as session:
        exists = session.exec(
            select(GroceryList).where(GroceryList.name == new_list_name)
        ).first()
        if new_list_name and not exists:
            grocery_list = GroceryList(name=new_list_name)
            session.add(grocery_list)
            session.commit()
    return RedirectResponse(f"/?list_name={new_list_name}", status_code=303)


@app.post("/delete_list", response_class=RedirectResponse)
def delete_list(request: Request, delete_list_name: str = Form(...)):
    with Session(engine) as session:
        grocery_list = session.exec(
            select(GroceryList).where(GroceryList.name == delete_list_name)
        ).first()
        if grocery_list:
            # Delete items first
            items = session.exec(
                select(GroceryItem).where(GroceryItem.list_id == grocery_list.id)
            ).all()
            for item in items:
                session.delete(item)
            session.delete(grocery_list)
            session.commit()
        # Redirect to another list or default
        next_list = session.exec(select(GroceryList)).first()
        next_list_name = next_list.name if next_list else "regular"
    return RedirectResponse(f"/?list_name={next_list_name}", status_code=303)
