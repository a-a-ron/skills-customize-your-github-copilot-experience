# Starter code for FastAPI REST API assignment

# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Example Pydantic model
class Item(BaseModel):
    id: int
    name: str
    description: str = None

# In-memory storage for items
items: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI REST API!"}

# Add your CRUD endpoints below
