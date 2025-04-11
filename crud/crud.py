from models.models import Todo
from schemas.schemas import TodoIn
from database import database

async def get_all_todos():
    query = Todo.__table__.select()
    return await database.fetch_all(query)

async def create_todo(todo :TodoIn):
    print("I have entered crud")
    
    query = Todo.__table__.insert().values(
        title=todo.title,
        completed=False
        ).returning(Todo.__table__.c.id)
    
    last_record_id = await database.execute(query=query)
    return {**todo.model_dump(), "id": last_record_id, "completed": False}