"""
    This file is responsible for all the main handles of the FastAPI webapp. This is also where the application starts.
    I don't plan on spending very much time on this, it's just a technical demo to prove I can use FastAPI.
    I mean like, literally half an hour (we'll see).
"""

from fastapi import FastAPI
from models import *
from db import *

# create the app object
app = FastAPI()

# routes are as followed:

@app.get("/")
def read_root():
    """
        This is the default route.
    """
    return {"This is a simple Fast API webapp."}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    """
        This function reads a user from the database.
    """
    obj = User(id=user_id, name="John Doe", age=25) # temp
    # some super quick and simple validation
    assert obj.id > 0, "ID must be greater than 0."
    assert obj.age > 0, "Age must be greater than 0."
    assert obj.name != "", "Name must not be empty."
    return {"user_id": obj.id, "name": obj.name, "age": obj.age}

@app.post("/users/")
def create_user(id: int, name: str, age: int):
    """
        This function creates a user in the database.
    """
    assert id > 0, "ID must be greater than 0."
    assert name != "", "Name must not be empty."
    assert age > 0, "Age must be greater than 0."
    user = User(id=id, name=name, age=age)
    create_user("user", user)
    return user