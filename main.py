from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class GroceryItem(BaseModel):
    id: int
    name: str
    quantity: int

grocery_lists: Dict[str, List[GroceryItem]] = {
    "regular": [],
    "costco": [],
}

def get_next_id(list_name: str) -> int:
    items = grocery_lists.get(list_name, [])
    if not items:
        return 1
    return max(item.id for item in items) + 1

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, list_name: str = "regular"):
    items = grocery_lists.get(list_name, [])
    return templates.TemplateResponse("index.html", {
        "request": request,
        "list_name": list_name,
        "lists": list(grocery_lists.keys()),
        "items": items
    })

@app.get("/groceries/{list_name}", response_model=List[GroceryItem])
def get_groceries(list_name: str):
    if list_name not in grocery_lists:
        raise HTTPException(status_code=404, detail="List not found.")
    return grocery_lists[list_name]

@app.post("/groceries/{list_name}", response_model=GroceryItem)
def add_grocery(list_name: str, item: GroceryItem):
    if list_name not in grocery_lists:
        raise HTTPException(status_code=404, detail="List not found.")
    if any(g.id == item.id for g in grocery_lists[list_name]):
        raise HTTPException(status_code=400, detail="Item with this ID already exists.")
    grocery_lists[list_name].append(item)
    return item

@app.put("/groceries/{list_name}/{item_id}", response_model=GroceryItem)
def update_grocery(list_name: str, item_id: int, item: GroceryItem):
    if list_name not in grocery_lists:
        raise HTTPException(status_code=404, detail="List not found.")
    for idx, g in enumerate(grocery_lists[list_name]):
        if g.id == item_id:
            grocery_lists[list_name][idx] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found.")

@app.delete("/groceries/{list_name}/{item_id}")
def delete_grocery(list_name: str, item_id: int):
    if list_name not in grocery_lists:
        raise HTTPException(status_code=404, detail="List not found.")
    for idx, g in enumerate(grocery_lists[list_name]):
        if g.id == item_id:
            del grocery_lists[list_name][idx]
            return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found.")

@app.post("/add", response_class=RedirectResponse)
def add_item(
    request: Request,
    list_name: str = Form(...),
    name: str = Form(...),
    quantity: int = Form(...)
):
    if list_name not in grocery_lists:
        grocery_lists[list_name] = []
    new_id = get_next_id(list_name)
    grocery_lists[list_name].append(GroceryItem(id=new_id, name=name, quantity=quantity))
    return RedirectResponse(f"/?list_name={list_name}", status_code=303)

@app.post("/delete", response_class=RedirectResponse)
def delete_item(
    list_name: str = Form(...),
    id: int = Form(...)
):
    if list_name in grocery_lists:
        grocery_lists[list_name] = [g for g in grocery_lists[list_name] if g.id != id]
    return RedirectResponse(f"/?list_name={list_name}", status_code=303)

@app.post("/create_list", response_class=RedirectResponse)
def create_list(
    request: Request,
    new_list_name: str = Form(...)
):
    if new_list_name and new_list_name not in grocery_lists:
        grocery_lists[new_list_name] = []
    return RedirectResponse(f"/?list_name={new_list_name}", status_code=303)

@app.post("/delete_list", response_class=RedirectResponse)
def delete_list(
    request: Request,
    delete_list_name: str = Form(...)
):
    if delete_list_name in grocery_lists:
        del grocery_lists[delete_list_name]
    # Redirect to another list or default
    next_list = next(iter(grocery_lists.keys()), "regular")
    return RedirectResponse(f"/?list_name={next_list}", status_code=303)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8069, reload=True)
