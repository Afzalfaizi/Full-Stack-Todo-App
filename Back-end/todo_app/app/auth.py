from passlib.context import CryptContext
from sqlmodel import Session
from typing import Annotated
from todo_app.db import get_session
from fastapi import Depends

pwd_context = CryptContext(schemes="bcrypt", deprecated = "auto")