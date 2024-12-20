from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

class VideoBase(BaseModel):
    title: str
    description: Optional[str] = None
    youtube_url: str

class VideoCreate(VideoBase):
    uploaded_by: int

class VideoResponse(VideoBase):
    id: int
    uploaded_by: int

    class Config:
        from_attributes = True
