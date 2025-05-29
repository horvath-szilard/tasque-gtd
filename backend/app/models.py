# backend/app/models.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class Context(Base):
    __tablename__ = "contexts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    tasks = relationship("Task", back_populates="context")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    tasks = relationship("Task", back_populates="project")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    notes = Column(Text)
    type = Column(String, nullable=False)  # inbox, next_action, waiting, someday
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    context_id = Column(Integer, ForeignKey("contexts.id"), nullable=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=True)

    context = relationship("Context", back_populates="tasks")
    project = relationship("Project", back_populates="tasks")