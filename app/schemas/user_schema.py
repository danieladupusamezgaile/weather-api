from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str
    first_name: str

class UserRead(BaseModel):
    id: int
    username: str
    first_name: str
    is_active: bool

    class Config:
        orm_mode = True
    
class UserInDB(UserRead):
    hashed_password: str
