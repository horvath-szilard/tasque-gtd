from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/contexts", tags=["contexts"])

@router.get("/", response_model=list[schemas.ContextRead])
def list_contexts(db: Session = Depends(get_db)):
    return crud.get_contexts(db)

@router.post("/", response_model=schemas.ContextRead)
def create_context(context: schemas.ContextCreate, db: Session = Depends(get_db)):
    return crud.create_context(db, context)

@router.put("/{context_id}", response_model=schemas.ContextRead)
def update_context(context_id: int, context_update: schemas.ContextUpdate, db: Session = Depends(get_db)):
    db_context = crud.update_context(db, context_id=context_id, context_update=context_update)
    if db_context is None:
        raise HTTPException(status_code=404, detail="Context not found")
    return db_context

@router.delete("/{context_id}", response_model=schemas.ContextRead)
def delete_context(context_id: int, db: Session = Depends(get_db)):
    db_context = crud.delete_context(db, context_id=context_id)
    if db_context is None:
        raise HTTPException(status_code=404, detail="Context not found")
    return db_context