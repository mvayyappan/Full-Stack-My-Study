# My Study Life - Full Stack Quiz Platform

A complete full-stack competitive exam preparation platform with quiz system, real-time scoring, user authentication, and progress tracking. Built for students preparing for **TNPSC, Banking, Railways, and SSC** exams.

## 🚀 Features

✅ **User Authentication** - Secure signup/login with JWT tokens  
✅ **50+ Quizzes** - 500+ questions across multiple subjects  
✅ **Quiz Player** - Real-time timer, progress tracking, instant scoring  
✅ **Progress Dashboard** - Track quiz history and performance  
✅ **Responsive Design** - Works on desktop and mobile  
✅ **API Documentation** - Auto-generated Swagger UI  
✅ **GitHub Pages Deployment** - Live frontend hosting  

## 📁 Project Structure

```
My-Study-Life-Project/
├── frontend/                    # Web application (HTML/CSS/JS)
│   ├── index.html              # Home page
│   ├── pages/
│   │   ├── login.html          # Login page
│   │   ├── signup.html         # Registration page
│   │   ├── dashboard.html      # Quiz dashboard
│   │   ├── quiz.html           # Quiz player
│   │   ├── quiz_selection.html # Quiz selection
│   │   └── e-books/            # Study materials
│   ├── css/                    # Stylesheets
│   ├── js/
│   │   └── api.js             # Backend API client
│   └── assets/                # Images and resources
│
├── backend/                     # FastAPI backend server
│   ├── main.py                # Application entry point
│   ├── models.py              # Database models
│   ├── database.py            # DB configuration
│   ├── routers/
│   │   ├── auth.py            # Auth endpoints
│   │   └── quiz.py            # Quiz endpoints
│   ├── utils/
│   │   └── security.py        # JWT token handling
│   ├── mega_seed.py           # Database seeding
│   └── requirements.txt        # Python dependencies
│
├── docs/                        # GitHub Pages content
├── .github/workflows/          # CI/CD automation
├── .gitignore
└── README.md
```

## 🛠 Tech Stack

### Frontend
- **HTML5**, **CSS3**, **JavaScript** (Vanilla)
- Fetch API for backend communication
- LocalStorage for token management
- Font Awesome 6.4.2 icons
- Google Fonts
- Responsive grid layout

### Backend
- **FastAPI** 0.128.0 - Modern Python web framework
- **PostgreSQL** - Relational database
- **SQLAlchemy** 2.0.45 - ORM
- **JWT Authentication** - Secure token-based auth
- **Uvicorn** - ASGI server
- **CORS** - Cross-origin support

## ⚡ Quick Start

### Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create and seed database
python -c "from database import init_db; init_db()"
python mega_seed.py

# Start server
python main.py
```

Backend runs on: `http://127.0.0.1:8000`

### Frontend Setup

```bash
# From project root
cd frontend

# Start local server
python -m http.server 5500
```

Frontend runs on: `http://127.0.0.1:5500`

Visit: `http://127.0.0.1:5500/index.html`

## 📚 Sample Login Credentials

```
Email:    test@example.com
Password: testpassword123
```

## 🔌 API Documentation

Once backend is running:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

### Key Endpoints

#### Authentication
```
POST   /api/auth/signup          - Register new user
POST   /api/auth/login           - Login user
POST   /api/auth/logout          - Logout user
GET    /api/auth/me              - Get current user
```

#### Quizzes
```
GET    /api/quizzes              - List all quizzes
GET    /api/quiz/{quiz_id}       - Get quiz with questions
POST   /api/quiz/{quiz_id}/submit - Submit quiz answers
GET    /api/progress             - Get user progress
```

## 📊 Database Schema

| Table | Purpose |
|-------|---------|
| **users** | User accounts, authentication, profile |
| **quizzes** | Quiz metadata (title, description, category) |
| **questions** | Quiz questions with multiple choice options |
| **user_answers** | Student responses during quiz |
| **progress** | Quiz history, scores, timestamps |

### Sample Data Included
- 50 complete quizzes
- 500+ questions (10 per quiz)
- Multiple difficulty levels
- Standard 1-12 study materials
- Bank, Railway, SSC, TNPSC exams

## 🐛 Troubleshooting

### Invalid Token Error
```
Solution: Clear localStorage and login again
1. Open DevTools (F12)
2. Go to Application → LocalStorage
3. Delete 'authToken' key
4. Login again
```

### Quiz Not Loading
```
Checklist:
✓ PostgreSQL service is running
✓ Backend server is running (python main.py)
✓ Database is seeded (python mega_seed.py)
✓ API URL is correct in frontend/js/api.js
```

### CORS Issues
```
Ensure:
✓ Backend CORS origins include frontend URL
✓ Requests include correct Authorization header
✓ Tokens are being sent as Bearer tokens
```

## 🚀 Deployment

### Frontend (GitHub Pages)
```bash
# Deployment is automated via GitHub Actions
# Push to main branch and it auto-deploys to gh-pages
git push origin main
```

Live at: https://mvayyappan.github.io/My-Study-Life-Project/

### Backend (Optional)
Deploy to: Heroku, AWS, DigitalOcean, Google Cloud

Update API_URL in `frontend/js/api.js` to production endpoint.

## 📱 Features Detail

### Quiz Player
- Real-time countdown timer
- Question navigation (previous/next)
- Progress indicator
- Instant score calculation
- Results display with statistics

### Dashboard
- Featured quizzes (quick access)
- Quiz categories
- Progress overview
- Quiz history

### Authentication
- User registration
- Email-based login
- JWT token security
- Auto-logout on token expiry
- Token validation on page load

## 🔐 Security

- JWT tokens with HS256 algorithm
- Tokens expire after 24 hours
- Secure password validation
- CORS protection
- SQL injection prevention via ORM
- XSS protection in frontend

## 🎯 Quiz Categories

- **TNPSC** - Tamil Nadu Public Service Commission
- **Banking** - SBI, IBPS, RBI exams
- **Railways** - RRB NTPC, Group D
- **SSC** - Central Government Services
- **Standard Materials** - Grades 1-12 study materials

## 📈 Future Enhancements

- [ ] Admin dashboard for quiz management
- [ ] Advanced analytics and reports
- [ ] Certificate generation
- [ ] Leaderboard system
- [ ] Mobile app (React Native)
- [ ] Real-time collaboration
- [ ] Video tutorials integration

## ✨ Recent Updates

✅ Fixed JWT token extraction for quiz submission  
✅ Added login page token validation  
✅ Deployed to GitHub Pages  
✅ Organized frontend/backend folders  
✅ Bilingual support removed for simplicity  
✅ Comprehensive error handling and logging  

## 📞 Support

- Open an issue on GitHub for bugs/requests
- Check troubleshooting section above
- Review API documentation at `/docs` endpoint

## 📄 License

MIT License - Free to use for educational purposes

---

**Built with ❤️ for competitive exam aspirants**  
**Last Updated**: February 2026  
**Status**: ✅ Production Ready
