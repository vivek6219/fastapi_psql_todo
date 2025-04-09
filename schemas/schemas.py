from typing import Optional
from pydantic import BaseModel

class TodoIn(BaseModel):
    title: str

class TodoOut(BaseModel):
    id: int
    title: str
    completed: bool