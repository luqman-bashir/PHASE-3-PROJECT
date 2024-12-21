# Educational Video App
# By Luqman Bashir
# 19/12/2024
A React-based application to manage and display educational videos. Users can add, edit, search, and delete videos. The app integrates with a FastAPI backend and utilizes SQLAlchemy for database interactions.

## Table of Contents
-Project Description
-Features
-Technologies Used
-File Structure
-Installation
-Usage
-API
-Live Server
-Contributors
-License
-Project Description

### The Educational Video App is designed to allow users to:

-Add new educational videos with a title, description, and category.
-Edit existing videos.
-Search videos by title or category.
-Display a list of videos with details.
-Delete videos.
-The app uses FastAPI for the backend to manage data and SQLAlchemy for database interactions, providing a robust and scalable system.

### Features
-User Authentication: Secure user registration and login using JWT authentication.
-Add Video: Users can add new educational videos.
-Edit Video: Users can edit existing videos.
-Delete Video: Users can delete videos they have uploaded.
-Search Functionality: Users can search for videos by title or category.

### Technologies Used
Frontend
React (JavaScript library for building user interfaces)
TailwindCSS (Utility-first CSS framework for styling)
HTML & CSS (Core web technologies)

Backend
FastAPI (Python web framework)
SQLAlchemy (Object-Relational Mapper for database interaction)
SQLite (Database for development)
Others
Alembic (Database migrations)
JWT (JSON Web Tokens for authentication)

### File Structure
bash
Copy code
/educational-video-app
│
├── /public
│   └── index.html                     # Main HTML file
│
├── /frontend
│   ├── /components
│   │   ├── AddVideoForm.js            # Form to add or edit videos
│   │   ├── Footer.js                  # Footer component
│   │   ├── Header.js                  # Header with app title and logo
│   │   ├── NavBar.js                  # Navigation bar with search functionality
│   │   └── VideoList.js               # List of videos
│   │
│   ├── /pages
│   │   ├── Home.js                    # Home page with video list
│   │   ├── About.js                   # About page
│   │
│   ├── /styles
│   │   └── App.css                    # Main CSS file
│
├── /backend
│   ├── /app
│   │   ├── auth.py                    # User authentication routes
│   │   ├── database.py                # Database connection and models
│   │   ├── models.py                  # Database models
│   │   ├── routers
│   │   │   ├── __init__.py            # Router initialization
│   │   │   └── videos.py              # Video routes
│   │   └── main.py                    # FastAPI main app entry
│
├── /migrations
│   └── ...                            # Alembic database migrations
│
├── package.json                       # Frontend dependencies and scripts
└── README.md                          # Project documentation
Installation
1. Clone the repository
bash
Copy code
git clone https://github.com/yourusername/educational-video-app.git
cd educational-video-app
2. Install backend dependencies
bash
Copy code
cd backend
pip install -r requirements.txt
3. Apply database migrations
bash
Copy code
alembic upgrade head
4. Install frontend dependencies
bash
Copy code
cd ../frontend
npm install
Usage
Start the Backend Server
Run the following command in the backend directory:

bash
Copy code
uvicorn app.main:app --reload
Start the Frontend Development Server
Run the following command in the frontend directory:

bash
Copy code
npm start
Access the Application

### API
User Endpoints
POST /auth/register: Register a new user.
POST /auth/login: Log in and retrieve an access token.
Video Endpoints
POST /videos: Add a new video (requires authentication).
GET /videos: Retrieve a list of all videos.
GET /videos/{id}: Retrieve details of a specific video.
PUT /videos/{id}: Update video details.
DELETE /videos/{id}: Delete a video.

### Live Server
-This is the explanation of my project[Screen recording](https://app.screencastify.com/v2/manage/videos/qqbP4J3qTnTpZusk06Zn).

-View my slides[Slides](https://www.canva.com/design/DAGZ0IKhHtA/xqZMkhqa5xnm2mu-LUg2GA/view?utm_content=DAGZ0IKhHtA&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h8c7d772e6d).

-Watch the [live demo](https://peaceful-snickerdoodle-11c590.netlify.app/auth).



### License

[MIT License](https://github.com/luqman-bashir/PHASE-3-PROJECT/blob/main/LICENSE.md)
