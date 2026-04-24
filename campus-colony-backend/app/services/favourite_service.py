from sqlalchemy.orm import Session
from app.models.favourite import Favourite


def add_favourite(db: Session, user_id: int, listing_id: int):
    fav = Favourite(user_id=user_id, listing_id=listing_id)

    db.add(fav)
    db.commit()
    db.refresh(fav)

    return fav


def remove_favourite(db: Session, user_id: int, listing_id: int):
    fav = db.query(Favourite).filter(
        Favourite.user_id == user_id,
        Favourite.listing_id == listing_id
    ).first()

    if not fav:
        return None

    db.delete(fav)
    db.commit()

    return True


def get_favourites(db: Session, user_id: int):
    return db.query(Favourite).filter(Favourite.user_id == user_id).all()