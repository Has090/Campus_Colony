from fastapi import Depends, HTTPException
from app.utils.security import get_current_user
from app.models.user import User


def require_admin(user: User = Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return user


def require_student(user: User = Depends(get_current_user)):
    if user.role != "student":
        raise HTTPException(status_code=403, detail="Student access required")
    return user