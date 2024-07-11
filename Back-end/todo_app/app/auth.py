from passlib.context import CryptContext
from sqlmodel import Session, select
from typing import Annotated
from app.config.db import get_session
from fastapi import Depends
from app.models.todos import User, Todo

pwd_context = CryptContext(schemes="bcrypt", deprecated = "auto")

def hash_password(password):
    return pwd_context.hash(password)
     
def get_user_from_db(session:Annotated[Session, Depends(get_session)], username:str, email:str):
    statement = select(User).where(User.username == username)
    user = session.exec(statement).first()
    if not user:
        statement = select(User).where(User.email == email)
        user = session.exec(statement).first()
        if user:
            return user
    
    return user