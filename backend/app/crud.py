# backend/app/crud.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import models, schemas

# -----------------------------
# TASKS
# -----------------------------

def get_tasks_by_type(db: Session, task_type: str):
    return db.query(models.Task).filter(models.Task.type == task_type).all()


def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def update_task(db: Session, task_id: int, task_update: schemas.TaskUpdate):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        return None

    for field, value in task_update.dict(exclude_unset=True).items():
        setattr(db_task, field, value)

    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        return None

    db.delete(db_task)
    db.commit()
    return db_task


# -----------------------------
# PROJECTS
# -----------------------------

def get_projects(db: Session):
    return db.query(models.Project).all()


def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def update_project(db: Session, project_id: int, project_update: schemas.ProjectUpdate):
    db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if db_project is None:
        return None

    for field, value in project_update.dict(exclude_unset=True).items():
        setattr(db_project, field, value)

    db.commit()
    db.refresh(db_project)
    return db_project


def delete_project(db: Session, project_id: int):
    db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if db_project is None:
        return None

    db.delete(db_project)
    db.commit()
    return db_project


# -----------------------------
# CONTEXTS
# -----------------------------

def get_contexts(db: Session):
    return db.query(models.Context).all()


def create_context(db: Session, context: schemas.ContextCreate):
    db_context = models.Context(**context.dict())
    db.add(db_context)
    try:
        db.commit()
        db.refresh(db_context)
        return db_context
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Context with this name already exists.")
    


def update_context(db: Session, context_id: int, context_update: schemas.ContextUpdate):
    db_context = db.query(models.Context).filter(models.Context.id == context_id).first()
    if db_context is None:
        return None

    for field, value in context_update.dict(exclude_unset=True).items():
        setattr(db_context, field, value)

    db.commit()
    db.refresh(db_context)
    return db_context


def delete_context(db: Session, context_id: int):
    db_context = db.query(models.Context).filter(models.Context.id == context_id).first()
    if db_context is None:
        return None

    db.delete(db_context)
    db.commit()
    return db_context