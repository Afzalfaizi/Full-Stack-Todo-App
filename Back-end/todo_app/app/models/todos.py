from sqlmodel import SQLModel, Field


class Todo(SQLModel, table=True): 
    id: int = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    description: str
    email: str 
    is_Completed: bool

class UpdateTodo(SQLModel):
    name: str = Field(default=None)
    description: str | None
    email: str | None
    is_Completed: bool | None