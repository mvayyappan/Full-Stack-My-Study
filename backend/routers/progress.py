from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.progress import Progress
from models.user import User
from schemas.progress import ProgressResponse
from utils.security import decode_token

router = APIRouter(
    prefix="/api/progress",
    tags=["Progress"]
)

def get_current_user_id(token: str, db: Session = Depends(get_db)):
    """Get current user ID from token"""
    email = decode_token(token)
    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    return user.id

@router.get("/user", response_model=list[ProgressResponse])
def get_user_progress(token: str, db: Session = Depends(get_db)):
    """Get all quiz results for current user"""
    user_id = get_current_user_id(token, db)
    
    progress_list = db.query(Progress).filter(Progress.user_id == user_id).all()
    return progress_list

@router.get("/quiz/{quiz_id}")
def get_quiz_result(quiz_id: int, token: str, db: Session = Depends(get_db)):
    """Get result for specific quiz taken by user"""
    user_id = get_current_user_id(token, db)
    
    progress = db.query(Progress).filter(
        Progress.user_id == user_id,
        Progress.quiz_id == quiz_id
    ).first()
    
    if not progress:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Quiz result not found"
        )
    
    return progress

@router.get("/stats")
def get_user_stats(token: str, db: Session = Depends(get_db)):
    """Get user statistics"""
    user_id = get_current_user_id(token, db)
    
    progress_list = db.query(Progress).filter(Progress.user_id == user_id).all()
    
    if not progress_list:
        return {
            "total_quizzes": 0,
            "average_score": 0,
            "total_correct": 0,
            "total_questions": 0
        }
    
    total_correct = sum(p.correct_answers for p in progress_list)
    total_questions = sum(p.total_questions for p in progress_list)
    average_score = sum(p.score for p in progress_list) / len(progress_list)
    
    return {
        "total_quizzes": len(progress_list),
        "average_score": round(average_score, 2),
        "total_correct": total_correct,
        "total_questions": total_questions
    }
