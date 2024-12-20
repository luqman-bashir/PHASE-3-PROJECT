from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# Base class for ORM models
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    # Relationship to Video table
    videos = relationship('Video', back_populates='owner', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"

class Video(Base):
    __tablename__ = "videos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    youtube_url = Column(String, nullable=False)
    uploaded_by = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationship to User table
    owner = relationship('User', back_populates='videos')

    def __repr__(self):
        return f"<Video(id={self.id}, title='{self.title}', user_id={self.user_id}, youtube_url='{self.youtube_url}')>"
