from pydantic import BaseModel, ConfigDict
from typing import Optional


class ListingCreate(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    type: str
    area_id: int
    landlord_id: int
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class ListingResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    price: float
    type: str
    area_id: int
    landlord_id: int
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    image_url: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)