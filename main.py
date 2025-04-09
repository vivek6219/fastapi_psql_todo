import models
from routes.routes import router
from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import database, metadata, engine

metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    #startup 
    print("App is starting up")
    await database.connect()
    #yield control to fastapi to handle requests
    yield
    
    #shutdown
    print("App is shutting down")
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(router)
