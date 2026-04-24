from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.landlord import LandlordCreate
from app.services.landlord_service import (
    create_landlord,
    get_landlords,
    delete_landlord
)

from app.utils.dependencies import require_admin

router = APIRouter()


@router.post("/")
def add_landlord(
    data: LandlordCreate,
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    return create_landlord(db, data)


@router.get("/")
def list_landlords(db: Session = Depends(get_db)):
    return get_landlords(db)


@router.delete("/{landlord_id}")
def remove_landlord(
    landlord_id: int,
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    result = delete_landlord(db, landlord_id)

    if not result:
        raise HTTPException(status_code=404, detail="Landlord not found")

    return {"message": "Landlord deleted"}