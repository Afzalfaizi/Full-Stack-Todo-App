from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine, Session, select
import uvicorn

app = FastAPI()

connection_string = 'postgresql://postgres.lbmuulohpxlzgumdqzao:Ifltp3*789258@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres'
engine = create_engine(connection_string)
class Users(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    description: str
    email: str 
    
SQLModel.metadata.create_all(engine)

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