from fastapi import FastAPI
from app.database import Base,engine
from app.models import User,Task
from app.routers import auth,tasks
Base.metadata.create_all(bind=engine)
app=FastAPI(title="FastAPI Task Management API",version="1.0.0")
app.include_router(auth.router);app.include_router(tasks.router)
@app.get("/")
def home(): return {"message":"FastAPI Task Management API","status":"running"}
@app.get("/health")
def health(): return {"status":"healthy"}
