from fastapi import FastAPI
import uvicorn
from sqlmodel import SQLModel, Field, Session, select, create_engine
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

@app.get("/getTodos")
def getTodos():
    with Session(engine) as session:
        statement = select(Todo).where(Todo.id == 1)
        results = session.exec(statement)
        data = results.all()
        print(data)
        return 

@app.post("/todos")
def todos():
    return todos

