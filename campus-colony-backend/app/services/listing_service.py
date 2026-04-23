from sqlalchemy.orm import Session
from app.models.listing import Listing


from app.utils.helpers import upload_image

def create_listing(db: Session, data, image_file=None):
    image_url = None

    if image_file:
        image_url = upload_image(image_file.file) 

    listing = Listing(
        **data.model_dump(),
        image_url=image_url
    )

    db.add(listing)
    db.commit()
    db.refresh(listing)

    return listing

def get_listings(db: Session):
    listings = db.query(Listing).all()

    result = []

    for l in listings:
        result.append({
            "id": l.id,
            "title": l.title,
            "description": l.description,
            "price": l.price,
            "type": l.type,
            "area_id": l.area_id,
            "landlord_id": l.landlord_id,
            "image_url": l.image_url if l.image_url else None
        })

    return result


def delete_listing(db: Session, listing_id: int):
    listing = db.query(Listing).filter(Listing.id == listing_id).first()

    if not listing:
        return None

    db.delete(listing)
    db.commit()
    return True