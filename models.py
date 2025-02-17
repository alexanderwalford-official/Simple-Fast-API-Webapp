from pydantic import BaseModel

class User(BaseModel):
    """
        Default user model.
    """
    id: int
    name: str
    age: int