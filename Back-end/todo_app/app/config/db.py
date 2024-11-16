from sqlmodel import SQLModel, create_engine, Session
import os

connection_string = os.getenv('DATABASE_URI')
engine = create_engine(connection_string)

def create_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session