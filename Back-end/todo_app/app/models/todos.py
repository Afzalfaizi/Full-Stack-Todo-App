from sqlmodel import SQLModel, Field



class Todo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    description: str
    is_completed: bool
    