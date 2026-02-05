# My Study Life - Quiz Platform

A full-stack competitive exam preparation platform with quiz system, progress tracking, and study materials for students preparing for TNPSC, Banking, Railways, and SSC exams.

## Project Structure

```
My-Study-Life-Project/
├── frontend/              # Frontend web application
│   ├── index.html        # Home page
│   ├── css/              # Stylesheets
│   ├── js/               # JavaScript (API client, scripts)
│   ├── pages/            # HTML pages (dashboard, quiz, etc.)
│   ├── assets/           # Images and resources
│   └── pages/e-books/    # E-books pages
│
├── backend/              # FastAPI backend server
│   ├── main.py          # Application entry point
│   ├── models.py        # SQLAlchemy ORM models
│   ├── database.py      # Database configuration
│   ├── routers/         # API route handlers
│   │   ├── auth.py      # Authentication endpoints
│   │   ├── quiz.py      # Quiz endpoints
│   │   └── ...
│   ├── utils/           # Utility functions
│   │   └── security.py  # JWT token management
│   ├── venv/            # Python virtual environment
│   └── requirements.txt # Python dependencies
│
└── README.md
```

## Features

- **User Authentication**: Signup/Login with JWT tokens
- **Quiz System**: 50+ quizzes with 500+ questions across 5 subjects
- **Three Difficulty Levels**: Easy, Medium, Hard
- **Quiz Player**: Full-featured quiz interface with:
  - Real-time timer
  - Progress tracking
  - Score calculation
  - Answer submission
- **Progress Tracking**: User quiz results and performance analytics
- **Responsive Design**: Works on desktop and mobile devices
- **Exam Categories**:
  - TNPSC (Tamil Nadu Public Service Commission)
  - Banking (SBI, IBPS, RBI)
  - Railways (RRB NTPC, Group D)
  - SSC (Central Government Services)

## Tech Stack

### Frontend
- HTML5, CSS3, JavaScript (Vanilla)
- Fetch API for backend communication
- LocalStorage for token persistence
- Font Awesome icons
- Google Fonts

### Backend
- **Framework**: FastAPI 0.128.0
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy 2.0.45
- **Authentication**: JWT (JSON Web Tokens)
- **Server**: Uvicorn ASGI server

## Installation

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**:
   - **Windows**: `.\venv\Scripts\activate`
   - **Mac/Linux**: `source venv/bin/activate`

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Create database**:
   ```bash
   python -c "from database import init_db; init_db()"
   ```

6. **Seed sample data**:
   ```bash
   python mega_seed.py
   ```

7. **Start backend server**:
   ```bash
   python main.py
   ```
   Backend will run on `http://127.0.0.1:8000`

### Frontend Setup

1. **Navigate to project root**:
   ```bash
   cd ..
   ```

2. **Start a local HTTP server**:
   ```bash
   python -m http.server 5500
   ```
   Frontend will run on `http://127.0.0.1:5500`

3. **Open in browser**:
   - Navigate to `http://127.0.0.1:5500/frontend/`

## API Documentation

Once the backend is running, view API docs at:
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## Database Schema

### Tables
- **users**: User accounts and authentication
- **quizzes**: Quiz metadata and configuration
- **questions**: Quiz questions with options
- **user_answers**: Student quiz responses
- **progress**: User quiz attempt history and scores

### Sample Data
- 50 quizzes (10 of each: Tamil, English, Maths, Science, Social Studies)
- 500+ questions (10 questions per quiz)
- Multiple difficulty levels (Easy, Medium, Hard)
- Available for grades 6-10

## Sample Credentials

```
Email: test@example.com
Password: testpassword123
```

## Usage

1. **Register** - Create new account on signup page
2. **Login** - Access dashboard after authentication
3. **Browse Quizzes** - View all available quizzes on dashboard
4. **Start Quiz** - Click on any quiz to begin
5. **Answer Questions** - Select answers and navigate through questions
6. **Submit** - Complete quiz and view results
7. **Track Progress** - Monitor your quiz performance on dashboard

## API Endpoints

### Authentication
- `POST /api/auth/signup` - Register new user
- `POST /api/auth/login` - Login user
- `POST /api/auth/logout` - Logout user
- `GET /api/auth/me` - Get current user profile

### Quizzes
- `GET /api/quizzes` - List all quizzes
- `GET /api/quiz/{quiz_id}` - Get quiz with questions
- `POST /api/quiz/{quiz_id}/submit` - Submit quiz answers
- `GET /api/progress` - Get user progress/history

## Configuration

Backend settings in `backend/main.py`:
- **Database URL**: PostgreSQL connection string
- **Secret Key**: JWT secret for token signing
- **CORS Origins**: Allowed frontend origins
- **Token Expiration**: JWT token validity period

## Development

### Making Changes

1. **Backend changes**: Edit files in `backend/` and restart server
2. **Frontend changes**: Edit files in `frontend/` (auto-loaded in browser)
3. **Database schema changes**: Update `models.py` and run migrations

### Troubleshooting

#### Invalid Token Error
- Clear browser localStorage (DevTools → Application → LocalStorage)
- Login again to get fresh token
- Check backend is running with `python main.py`

#### Quiz Not Loading
- Ensure PostgreSQL is running
- Verify database has quiz data: `python mega_seed.py`
- Check network tab in browser DevTools

#### CORS Issues
- Verify frontend URL matches CORS allowed origins in backend
- Check backend is running before opening frontend

## Deployment

### Backend
- Host on cloud platform (Heroku, AWS, DigitalOcean, Google Cloud)
- Set environment variables for database and secrets
- Use production database

### Frontend
- Host on GitHub Pages, Vercel, or Netlify
- Update API_URL in js/api.js to point to production backend
- Build and deploy

## Future Enhancements

- [ ] Admin dashboard for quiz management
- [ ] Analytics and performance reports
- [ ] Certificate generation upon completion
- [ ] Leaderboard system
- [ ] Study materials library
- [ ] Notes taking feature
- [ ] Mobile app (React Native/Flutter)

## License

MIT License - feel free to use for educational purposes

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Built with ❤️ for competitive exam aspirants**
