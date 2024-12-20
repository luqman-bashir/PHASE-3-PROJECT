from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]

    class Config:
        orm_mode = True

class VideoCreate(BaseModel):
    title: str
    description: str
    youtube_url: str
    uploaded_by: int

    class Config:
        orm_mode = True

class VideoResponse(BaseModel):
    id: int
    title: str
    description: str
    youtube_url: str
    uploaded_by: int

    class Config:
        orm_mode = True

class VideoUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    youtube_url: Optional[str]

    class Config:
        orm_mode = True
