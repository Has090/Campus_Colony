from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Area(Base):
    __tablename__ = "areas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    hospitals = Column(Integer, default=0)
    pharmacies = Column(Integer, default=0)
    libraries = Column(Integer, default=0)
    playgrounds = Column(Integer, default=0)
    gyms = Column(Integer, default=0)

    score = Column(Float, default=0.0)

    # 🔗 relationships
    listings = relationship("Listing", back_populates="area")