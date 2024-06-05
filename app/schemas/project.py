from pydantic import BaseModel
from typing import Optional, List

from app.schemas.user import User


class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    status: Optional[str] = "ongoing"


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    pass


class ProjectResponse(ProjectBase):
    id: int
    # owner_id: str
    # nominated_users: List[User] = []

    class Config:
        orm_mode = True
        from_attributes = True
