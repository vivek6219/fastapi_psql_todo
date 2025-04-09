from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from database import metadata

#base class for models
Base = declarative_base(metadata=metadata)

class Todo(Base):
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(Boolean, default=False, nullable=False)

