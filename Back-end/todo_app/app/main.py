from fastapi import FastAPI
import uvicorn
from sqlmodel import SQLModel, Field, Session, select
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()


class Todo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    description: str
    email: str 
    
@app.get("/getTodos")
def getTodos():
    with Session(engine) as session:
        statement = select(Users).where(Users.id == 1)
        results = session.exec(statement)
        data = results.all()
        print(data)
        return 

@app.post("/todos")
def todos():
    return todos

