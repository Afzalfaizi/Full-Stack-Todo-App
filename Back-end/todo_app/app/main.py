from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, select
import uvicorn
from dotenv import load_dotenv
load_dotenv()
from app.router import user
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm

from .models.todos import Todo, UpdateTodo, Register_User
from .config.db import create_tables, engine

app = FastAPI()

app.include_router(router=user.user_router)

@app.get("/")
def mainRoute():
    return {"Status":200, "Message": "Welcome to Zia Online Mart"}

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
def update_todo(id:int, todo: UpdateTodo):
    with Session(engine) as session: 
        db_todo = session.get(Todo, id)
        if not db_todo:
            raise HTTPException(status_code=404, detail="Todo not found") 
        todo_data = todo.model_dump(exclude_unset=True)
        db_todo.sqlmodel_update(todo_data)
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)
        return {"Status":200, "Message": "Todo updated Successfully"}

@app.delete("/delete_todo/{todo_id}")
def delete_todo(todo_id: int):
    with Session(engine) as session:
        db_todo = session.get(Todo, todo_id)
        if not db_todo:
            raise HTTPException(status_code=404, detail="Todo not found") 
        session.delete(db_todo)
        return {"Status":200, "Message": "Todo deleted Successfully"}
    
def start():
    create_tables()
    uvicorn.run("app.main:app", host="127.0.0.1", port=8080, reload=True)
    
# login
@app.post("/token")
async def login(from_data:Annotated[OAuth2PasswordRequestForm, Depends()]):
    pass