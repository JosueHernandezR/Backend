from datetime import datetime

from pydantic import UUID4, BaseModel, EmailStr

# Shared properties
class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    gender: str
    is_active: bool

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    pass

class UserInDBBase(UserBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Additional properties to return via API
class User(UserInDBBase):
    pass

# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str