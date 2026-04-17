from pydantic import BaseModel

class ListingCreate(BaseModel):
    property_name: str
    property_type: str
    area: str
    score: int
    price: float