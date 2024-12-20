from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Video
from app.schemas import VideoCreate, VideoResponse
from app.database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=VideoResponse)
def create_video(video: VideoCreate, db: Session = Depends(get_db)):
    new_video = Video(
        title=video.title,
        description=video.description,
        youtube_url=video.youtube_url,
        uploaded_by=video.uploaded_by,
    )
    db.add(new_video)
    db.commit()
    db.refresh(new_video)
    return new_video


@router.get("/", response_model=List[VideoResponse])
def get_videos(offset: int = 0, limit: int = 10, search: str = "", db: Session = Depends(get_db)):
    query = db.query(Video)
    
    if search:
        query = query.filter(Video.title.ilike(f"%{search}%"))  # Search by title

    videos = query.offset(offset).limit(limit).all()
    return videos

@router.get("/videos/{video_id}", response_model=VideoResponse)
def get_video(video_id: int, db: Session = Depends(get_db)):
    # Get a specific video by its ID
    video = db.query(Video).filter(Video.id == video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found.")
    return video

@router.put("/{video_id}", response_model=VideoResponse)
def update_video(video_id: int, video: VideoCreate, db: Session = Depends(get_db)):
    db_video = db.query(Video).filter(Video.id == video_id).first()
    if not db_video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    db_video.title = video.title
    db_video.description = video.description
    db_video.youtube_url = video.youtube_url
    db.commit()
    db.refresh(db_video)  # Refresh to get the updated video data
    return db_video

@router.delete("/{video_id}")
def delete_video(video_id: int, db: Session = Depends(get_db)):
    video = db.query(Video).filter(Video.id == video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    db.delete(video)
    db.commit()
    return {"message": "Video deleted successfully"}