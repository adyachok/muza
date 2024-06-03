from pydantic import BaseModel
from typing import Optional


class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None
    status: Optional[str] = "ongoing"


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = "ongoing"


class ProjectResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    status: Optional[str] = "ongoing"

    class Config:
        orm_mode = True
