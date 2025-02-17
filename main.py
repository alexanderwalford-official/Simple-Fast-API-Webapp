"""
    This file is responsible for all the main handles of the FastAPI webapp. This is also where the application starts.
    I don't plan on spending very much time on this, it's just a technical demo to prove I can use FastAPI.
    I mean like, literally half an hour (we'll see).
"""

from fastapi import FastAPI
from models import *
from db import *

app = FastAPI()

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
    obj = User(id=user_id, name="John Doe", age=25)
    return {"user_id": user_id}

@app.post("/users/")
def create_user(user: User):
    """
        This function creates a user in the database.
    """
    create_user("user", user)
    return user