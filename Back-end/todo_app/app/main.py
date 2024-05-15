from fastapi import FastAPI
import uvicorn
from sqlmodel import  Session, select
from dotenv import load_dotenv
from .config.db import  engine, create_Tables
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

@app.post("/create_todo")
def create_todos(todo: Todo):
    with Session(engine) as session:
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return {"Status":200, "Message": "Todo Created Successfully"}
    
create_Tables()

# def start():
    
    # uvicorn.run("app.main:app", host="127.0.0.1", port=8080, reload=True)