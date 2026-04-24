from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    type = Column(String)
    image_url = Column(String, nullable=True)

    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    area_id = Column(Integer, ForeignKey("areas.id", ondelete="SET NULL"))
    landlord_id = Column(Integer, ForeignKey("landlords.id", ondelete="SET NULL"))

    area = relationship("Area", back_populates="listings")
    landlord = relationship("Landlord", back_populates="listings")
    reviews = relationship("Review", back_populates="listing", cascade="all, delete")
    favourites = relationship("Favourite", cascade="all, delete")