from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database import Base

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True)
    property_name = Column(String, nullable=False)
    property_type = Column(String) 
    area = Column(String)          
    score = Column(Integer)         # Area Score (0-100)
    price = Column(Float)
    status = Column(String, default="Active") 
    created_at = Column(DateTime, default=datetime.utcnow)