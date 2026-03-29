from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

items: List[Item] = [
    Item(id=1, name="Sample Item", description="A starter API item", price=9.99)
]

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI item service"}

@app.get("/items")
async def read_items():
    return items

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items")
async def create_item(item: Item):
    items.append(item)
    return item
