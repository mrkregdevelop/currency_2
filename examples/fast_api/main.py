from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, count: Optional[int] = None):
    return {"item_id": item_id}
