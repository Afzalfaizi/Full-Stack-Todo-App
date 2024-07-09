from fastapi import APIRouter, Depends
from typing import Annotated
from todo_app.models import Register_User


user_router = APIRouter(
    prefix ="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}}
)

@user_router.get("/")
async def read_user():
    return {"message": "Welcome to Imtiaz Mart User Page"}

@user_router.post("/register")
async def register_user(form_data:Annotated[Register_User, Depends()]):
    pass