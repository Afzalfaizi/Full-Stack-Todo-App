from sqlmodel import SQLModel, Field
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from fastapi import Form



class Todo(SQLModel, table=True): 
    id: int = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    description: str
    email: str 
    is_Completed: bool
    user_id:int = Field(foreign_key="user.id")

class UpdateTodo(SQLModel):
    name: str = Field(default=None)
    description: str | None
    email: str | None
    is_Completed: bool | None
    
class User (SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username:str
    email: str
    password: str

class Register_User(OAuth2PasswordRequestForm):
        email: Annotated[
            str,
            Form(),
        ]

