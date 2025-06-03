from pydantic import BaseModel

class GroceryItem(BaseModel):
    id: int
    name: str
    quantity: int
    