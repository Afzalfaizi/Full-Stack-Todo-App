from passlib.context import CryptContext
from sqlmodel import Session, select
from typing import Annotated
from app.config.db import get_session
from fastapi import Depends
from app.models.todos import User, Todo
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timezone, timedelta
from app.models.todos import TokenData

SECRET_KEY = '9980b505fb4aca80beca586aec55f4bb73bfac5e8c16f821bdea06445d75680c'
ALGORITHM = 'HS256'
EXPIRY_TIME = 30

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

def create_access_token(data:dict, expiry_time:timedelta|None):
    data_to_encode = data.copy()
    if expiry_time:
        expire = datetime.now(timezone.utc) + expiry_time
    else: 
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    data_to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(data_to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
    
def current_user (token:Annotated[str, Depends(oauth_scheme)], session:Annotated[Session, Depends(get_session)]):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token, Please login again",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        username: str | None = payload.get("sub")
        if username is None:
            raise credential_exception
        token_data = TokenData(username=username)
        return username
    except:
        raise JWTError
    user = get_user_from_db(session, username=token_data.username)
    if not user:
        raise credential_exception
    return user