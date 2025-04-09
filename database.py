from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql://todo_user:password@localhost/todo_db"

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL)

