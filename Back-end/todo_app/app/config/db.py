from sqlmodel import SQLModel, create_engine

connection_string = os.geteng('DATABASE_URI')
engine = create_engine(connection_string)

def create_Tables():
    SQLModel.metadata.create_all(engine)
