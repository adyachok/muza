from pydantic import BaseModel
from typing import Optional


class PersonaBase(BaseModel):
    name: str
    age: Optional[int] = None


class PersonaCreate(PersonaBase):
    pass


class PersonaUpdate(PersonaBase):
    pass


class PersonaResponse(PersonaBase):
    id: int

    class Config:
        orm_mode = True
