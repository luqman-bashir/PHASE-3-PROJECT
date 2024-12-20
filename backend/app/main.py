from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models import Base
from app.routers import  videos
from app.auth import auth_router


# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5178"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(videos.router, prefix="/videos", tags=["Videos"])
app.include_router(auth_router, prefix="/api", tags=["Authentication"])


@app.get("/")
def root():
    return {"message": "Welcome to the Educational Video App"}
