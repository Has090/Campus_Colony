from typing import List
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from fastapi.responses import Response
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.listing import ListingCreate, ListingResponse
from app.services.listing_service import (
    create_listing,
    get_listings,
    delete_listing
)

from app.models.listing import Listing

router = APIRouter()



@router.post("/", response_model=ListingResponse)
async def add_listing(
    title: str = Form(...),
    description: str = Form(None),
    price: float = Form(...),
    type: str = Form(...),
    area_id: int = Form(...),
    landlord_id: int = Form(...),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    

    data = ListingCreate(
        title=title,
        description=description,
        price=price,
        type=type,
        area_id=area_id,
        landlord_id=landlord_id
    )

    return create_listing(db, data, image)



@router.get("/", response_model=List[ListingResponse])
def list_listings(db: Session = Depends(get_db)):
    return get_listings(db)





@router.delete("/{listing_id}")
def remove_listing(listing_id: int, db: Session = Depends(get_db)):
    result = delete_listing(db, listing_id)

    if not result:
        raise HTTPException(status_code=404, detail="Listing not found")

    return {"message": "Listing deleted"}