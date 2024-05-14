from fastapi import FastAPI
import uvicorn
from sqlmodel import  Session, select
from dotenv import load_dotenv
from .config.db import create_Tables, engine
from .models.todos import Todo

load_dotenv()
app = FastAPI()

@app.get("/get_Todos")
def getTodos():
    with Session(engine) as session:
        statement = select(Todo)
        results = session.exec(statement)
        data = results.all()
        print(data)
        return 

@app.post("/todos")
def todos():
    return todos

create_Tables()

