# backend/app/schemas.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# ---------- Context Schemas ----------
class ContextBase(BaseModel):
    name: str


class ContextCreate(ContextBase):
    pass


class ContextRead(ContextBase):
    id: int

    class Config:
        from_attributes = True

class ContextUpdate(BaseModel):
    name: Optional[str] = None


# ---------- Project Schemas ----------
class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None


class ProjectCreate(ProjectBase):
    pass


class ProjectRead(ProjectBase):
    id: int

    class Config:
        orm_mode = True

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


# ---------- Task Schemas ----------
class TaskBase(BaseModel):
    title: str
    notes: Optional[str] = None
    type: str  # inbox, next_action, waiting, someday
    context_id: Optional[int] = None
    project_id: Optional[int] = None


class TaskCreate(TaskBase):
    pass


class TaskRead(TaskBase):
    id: int
    created_at: datetime
    context: Optional[ContextRead] = None
    project: Optional[ProjectRead] = None

    class Config:
        orm_mode = True

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    notes: Optional[str] = None
    type: Optional[str] = None
    context_id: Optional[int] = None
    project_id: Optional[int] = None

    class Config:
        from_attributes = True  # Pydantic v2-nek megfelelő új név