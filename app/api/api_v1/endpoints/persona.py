from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.crud import persona as crud_persona
from app.schemas.persona import PersonaCreate, PersonaUpdate, PersonaResponse
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=PersonaResponse)
def create_persona(persona: PersonaCreate, db: Session = Depends(get_db)):
    return crud_persona.create_persona(db, persona)


@router.get("/", response_model=List[PersonaResponse])
def read_personas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_persona.get_personas(db, skip=skip, limit=limit)


@router.get("/{persona_id}", response_model=PersonaResponse)
def read_persona(persona_id: int, db: Session = Depends(get_db)):
    persona = crud_persona.get_persona(db, persona_id)
    if persona is None:
        raise HTTPException(status_code=404, detail="Persona not found")
    return persona


@router.put("/{persona_id}", response_model=PersonaResponse)
def update_persona(persona_id: int, updated_persona: PersonaUpdate, db: Session = Depends(get_db)):
    persona = crud_persona.update_persona(db, persona_id, updated_persona)
    if persona is None:
        raise HTTPException(status_code=404, detail="Persona not found")
    return persona


@router.delete("/{persona_id}")
def delete_persona(persona_id: int, db: Session = Depends(get_db)):
    success = crud_persona.delete_persona(db, persona_id)
    if not success:
        raise HTTPException(status_code=404, detail="Persona not found")
    return {"message": "Persona deleted successfully"}
