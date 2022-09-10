from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from app import models
from app.database import engine
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="fastapi",
            user="postgres",
            password="example",
            cursor_factory=RealDictCursor,
        )
        cursor = conn.cursor()
        print("Database connection was successfull!")
        break
    except Exception as error:
        print("Connecting to databse failed")
        print("Error: ", error)
        time.sleep(2)

app = FastAPI()
app.include_router(auth.router)
app.include_router(post.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "Welcome to my API"}
