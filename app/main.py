from fastapi import FastAPI
from app import models, config
from app.database import engine
from .routers import user, auth, post

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(post.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "Welcome to my API"}
