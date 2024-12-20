from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base, User
from pydantic import BaseModel
from passlib.context import CryptContext
from typing import List
import logging

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Create database tables
Base.metadata.create_all(bind=engine)

# Create an instance of FastAPI
app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Models
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
    name: str = None
    email: str = None
    password: str = None

    class Config:
        orm_mode = True

# Routes
@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(name=user.name, email=user.email, password=hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    logger.info(f"User created: {user.email}")
    return new_user

@app.get("/users", response_model=List[UserResponse])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.patch("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user_data.email:
        existing_user = db.query(User).filter(User.email == user_data.email).first()
        if existing_user and existing_user.id != user_id:
            raise HTTPException(status_code=400, detail="Email already in use")
    update_data = user_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    logger.info(f"User updated: {user.email}")
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    logger.info(f"User deleted: {user_id}")
    return {"message": "User deleted successfully"}


# ---------------- VIDEOS CRUD ----------------
class VideoCreate(BaseModel):
    title: str
    description: str
    youtube_url: str
    category: str
    uploaded_by: int

    class Config:
        from_attributes = True  # Using from_attributes to be compatible with Pydantic V2

class VideoUpdate(BaseModel):
    title: str = None
    description: str = None
    youtube_url: str = None
    category: str = None

    class Config:
        from_attributes = True  # Using from_attributes to be compatible with Pydantic V2

class VideoResponse(BaseModel):
    id: int
    title: str
    description: str
    youtube_url: str
    category: str
    uploaded_by: int

    class Config:
        from_attributes = True  # Using from_attributes to be compatible with Pydantic V2

@app.get("/videos", response_model=List[VideoResponse])
def get_videos(db: Session = Depends(get_db)):
    videos = db.query(Video).all()
    return videos

@app.post("/videos", response_model=VideoResponse)
def create_video(video: VideoCreate, db: Session = Depends(get_db)):
    # Create the new video object from the request data
    new_video = Video(
        title=video.title,
        description=video.description,
        youtube_url=video.youtube_url,
        uploaded_by=video.uploaded_by,
    )
    
    # Add the new video to the database
    db.add(new_video)
    db.commit()
    db.refresh(new_video)  # Refresh the object to get the ID from the DB
    logger.info(f"Video created: {video.title}")
    return new_video

@app.get("/videos", response_model=List[VideoResponse])
def get_videos(offset: int = 0, limit: int = 10, search: str = "", db: Session = Depends(get_db)):
    # Build the query based on the search query and pagination parameters
    query = db.query(Video)
    
    if search:
        # Example of searching by title using ILIKE for case-insensitive matching
        query = query.filter(Video.title.ilike(f"%{search}%"))

    # Apply pagination with offset and limit
    videos = query.offset(offset).limit(limit).all()
    return videos


@app.put("/videos/{video_id}", response_model=VideoResponse)
def update_video(video_id: int, video: VideoCreate, db: Session = Depends(get_db)):
    db_video = db.query(Video).filter(Video.id == video_id).first()
    if not db_video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    # Update the video attributes
    db_video.title = video.title
    db_video.description = video.description
    db_video.youtube_url = video.youtube_url
    db.commit()
    db.refresh(db_video)  # Refresh to get the updated video data
    return db_video



@app.delete("/videos/{video_id}")
def delete_video(video_id: int, db: Session = Depends(get_db)):
    video = db.query(Video).filter(Video.id == video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    db.delete(video)
    db.commit()
    logger.info(f"Video deleted: {video_id}")
    return {"message": "Video deleted successfully"}

