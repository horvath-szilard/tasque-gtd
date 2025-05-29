# backend/app/main.py

from fastapi import FastAPI
from app.routes import tasks, projects, contexts

app = FastAPI(title="Donity – GTD Todo Manager")

app.include_router(tasks.router)
app.include_router(projects.router)
app.include_router(contexts.router)