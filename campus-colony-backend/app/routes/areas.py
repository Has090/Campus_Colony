from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.area import AreaCreate

router = APIRouter()


@router.post("/")
def add_area(area: AreaCreate, db: Session = Depends(get_db)):
    from app.services.area_service import create_area
    return create_area(db, area)


@router.get("/")
def list_areas(db: Session = Depends(get_db)):
    from app.services.area_service import get_areas
    return get_areas(db)


@router.delete("/{area_id}")
def remove_area(area_id: int, db: Session = Depends(get_db)):
    from app.services.area_service import delete_area

    result = delete_area(db, area_id)
    if not result:
        raise HTTPException(status_code=404, detail="Area not found")
    return {"message": "Area deleted"}