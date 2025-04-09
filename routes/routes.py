from schemas.schemas import TodoIn, TodoOut
from crud import crud

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get("/todos", response_model=list[TodoOut])
async def get_todos():
    #call crud function to get all todos
    return await crud.get_all_todos()

@router.post("/enter_todo", response_model=TodoOut)
async def add_todo(todo: TodoIn):
    #call crud function to get all todos
    return await crud.create_todo(todo)
