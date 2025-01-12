from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class User(UserBase):
    id: str

    class Config:
        orm_mode = True
        from_attributes = True
