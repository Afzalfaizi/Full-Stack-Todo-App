from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, select
import uvicorn
from dotenv import load_dotenv
load_dotenv()
from app.router import user
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from .auth import authenticate_user
from app.config.db import get_session
from .auth import create_access_token, current_user
from datetime import datetime, timedelta ,timezone
from .models.todos import Token
from .models.todos import User, Todo_Create

from .models.todos import Todo, UpdateTodo, Register_User
from .config.db import create_tables, engine

app = FastAPI()

app.include_router(router=user.user_router)

@app.get("/")
def mainRoute():
    return {"Status":200, "Message": "Welcome to Zia Online Mart"}

@app.get("/getTodos")
def getTodos(current_user:Annotated[User, Depends(current_user)],
            session:Annotated =[Session, Depends(get_session)]):
    
    with Session(engine) as session:
        statement = select(Todo)
        results = session.exec(statement)
        data = results.all()
        print(data)
        return data

@app.post("/create_todo/", response_model=Todo)
async def create_todo(current_user:Annotated[User, Depends(current_user)],
                todo: Todo_Create,
                session:Annotated [Session, Depends(get_session)]):
    new_todo = Todo(content=todo.content, user_id=current_user.id)

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
@app.post("/token", response_model= Token)
async def login(form_data:Annotated[OAuth2PasswordRequestForm, Depends()], session:Annotated[Session, Depends(get_session)]):            
    user = authenticate_user(form_data.username, form_data.password, session)
    user = authenticate_user (session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    expire_time = timedelta(minutes= EXPIRY_TIME)
    access_token = create_access_token({"sub":form_data.username}, expire_time)
    return Token(access_token=access_token, token_type="bearer")