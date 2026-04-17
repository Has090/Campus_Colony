from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate, UserLogin
from app.services.auth_service import create_user, login_user

router = APIRouter()

# ✅ Student Signup
@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.name, user.email, user.password)

# ✅ Login (Student + Admin)
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    result = login_user(db, user.email, user.password)
    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return result