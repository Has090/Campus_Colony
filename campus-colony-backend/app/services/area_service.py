from sqlalchemy.orm import Session
from app.models.area import Area

# 🧠 Score Calculation
def calculate_score(area):
    return (
        area.hospitals * 2 +
        area.pharmacies * 1 +
        area.libraries * 1 +
        area.playgrounds * 1 +
        area.gyms * 1.5
    )

# ✅ Create Area
def create_area(db: Session, data):
    area = Area(
        name=data.name,
        hospitals=data.hospitals,
        pharmacies=data.pharmacies,
        libraries=data.libraries,
        playgrounds=data.playgrounds,
        gyms=data.gyms
    )

    area.score = calculate_score(area)

    db.add(area)
    db.commit()
    db.refresh(area)

    return area

# ✅ Get All Areas
def get_areas(db: Session):
    return db.query(Area).all()

# ✅ Delete Area
def delete_area(db: Session, area_id: int):
    area = db.query(Area).filter(Area.id == area_id).first()
    if not area:
        return None

    db.delete(area)
    db.commit()
    return True