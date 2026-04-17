from sqlalchemy.orm import Session
from app.models.landlord import Landlord

def create_landlord(db: Session, data):
    landlord = Landlord(
        name=data.name,
        phone=data.phone,
        email=data.email
    )
    db.add(landlord)
    db.commit()
    db.refresh(landlord)
    return landlord

def get_landlords(db: Session):
    return db.query(Landlord).all()

def delete_landlord(db: Session, landlord_id: int):
    landlord = db.query(Landlord).filter(Landlord.id == landlord_id).first()
    if not landlord:
        return None

    db.delete(landlord)
    db.commit()
    return True