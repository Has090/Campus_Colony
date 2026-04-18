from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.listing import Listing
from app.schemas.listing import ListingCreate, ListingUpdate

# GET all listings
def get_all_listings(db: Session, skip: int = 0, limit: int = 50):
    return db.query(Listing).offset(skip).limit(limit).all()

# GET one listing by id
def get_listing_by_id(db: Session, listing_id: int):
    listing = db.query(Listing).filter(Listing.id == listing_id).first()
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    return listing

# POST — create new listing
def create_listing(db: Session, data: ListingCreate):
    new_listing = Listing(
        title         = data.title,
        property_type = data.property_type,
        area          = data.area,
        price         = data.price,
        score         = data.score,
        status        = data.status,
        landlord_id   = data.landlord_id,
    )
    db.add(new_listing)
    db.commit()
    db.refresh(new_listing)
    return new_listing

# PUT — update existing listing
def update_listing(db: Session, listing_id: int, data: ListingUpdate):
    listing = db.query(Listing).filter(Listing.id == listing_id).first()
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")

    if data.title         is not None: listing.title         = data.title
    if data.property_type is not None: listing.property_type = data.property_type
    if data.area          is not None: listing.area          = data.area
    if data.price         is not None: listing.price         = data.price
    if data.score         is not None: listing.score         = data.score
    if data.status        is not None: listing.status        = data.status

    db.commit()
    db.refresh(listing)
    return listing

# DELETE — remove listing
def delete_listing(db: Session, listing_id: int):
    listing = db.query(Listing).filter(Listing.id == listing_id).first()
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")

    db.delete(listing)
    db.commit()
    return {"message": f"Listing {listing_id} deleted successfully"}