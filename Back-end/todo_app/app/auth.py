from passlib.context import CryptContext
from sqlmodel import Session, select
from typing import Annotated
from app.config.db import get_session
from fastapi import Depends
from app.models.todos import User, Todo
from fastapi.security import OAuth2PasswordBearer

oauth_scheme = OAuth2PasswordBearer(tokenUrl = "/token")

pwd_context = CryptContext(schemes="bcrypt", deprecated = "auto")

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password, hash_password):
    return pwd_context.verify(password, hash_password)
     
def get_user_from_db(session:Annotated[Session, Depends(get_session)], username:str, email:str):
    statement = select(User).where(User.username == username)
    user = session.exec(statement).first()
    if not user:
        statement = select(User).where(User.email == email)
        user = session.exec(statement).first()
        if user:
            return user
    
    return user

def authenticate_user (username, email, password, session:Annotated[Session, Depends(get_session)]):
    db_user = get_user_from_db(session, username = username, email=email )
    if not db_user:
        return False
if not verify_password(password=password, hash_password=db_user.password):
    return False
return db_user