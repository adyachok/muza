from sqlalchemy.orm import Session
from app.db.models.persona import Persona
from app.schemas.persona import PersonaCreate, PersonaUpdate, PersonaResponse
from typing import List, Optional


def create_persona(db: Session, persona: PersonaCreate) -> PersonaResponse:
    db_persona = Persona(name=persona.name, age=persona.age)
    db.add(db_persona)
    db.commit()
    db.refresh(db_persona)
    return PersonaResponse.from_orm(db_persona)


def get_personas(db: Session, skip: int = 0, limit: int = 10) -> List[PersonaResponse]:
    personas = db.query(Persona).offset(skip).limit(limit).all()
    return [PersonaResponse.from_orm(persona) for persona in personas]


def get_persona(db: Session, persona_id: int) -> Optional[PersonaResponse]:
    persona = db.query(Persona).filter(Persona.id == persona_id).first()
    if persona:
        return PersonaResponse.from_orm(persona)
    return None


def update_persona(db: Session, persona_id: int, updated_persona: PersonaUpdate) -> Optional[PersonaResponse]:
    persona = db.query(Persona).filter(Persona.id == persona_id).first()
    if persona is None:
        return None
    persona.name = updated_persona.name
    persona.age = updated_persona.age
    db.commit()
    db.refresh(persona)
    return PersonaResponse.from_orm(persona)


def delete_persona(db: Session, persona_id: int) -> bool:
    persona = db.query(Persona).filter(Persona.id == persona_id).first()
    if persona is None:
        return False
    db.delete(persona)
    db.commit()
    return True
