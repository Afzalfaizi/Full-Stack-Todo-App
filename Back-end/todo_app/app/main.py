from fastapi import FastAPI
from sqlmodel import Session, select
import uvicorn
from dotenv import load_dotenv
from .config.db import create_tables, engine
from .models.todos import Todo, UpdateTodo

load_dotenv()

app = FastAPI()

@app.get("/getTodos")
def getTodos():
    with Session(engine) as session:
        statement = select(Todo)
        results = session.exec(statement)
        data = results.all()
        print(data)
        return data

@app.post("/create_todo")
def create_todo(todo: Todo):
    with Session(engine) as session:
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return {"Status":200, "Message": "Todo Created Successfully"}

@app.put("/update_todo/{id}")
def update_tod(todo: UpdateTodo):
    with Session(engine) as session: 
        db_todo = session.get(Todo, id)
    
def start():
    create_tables()
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)