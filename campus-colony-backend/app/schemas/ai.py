from pydantic import BaseModel

class RentPredictionRequest(BaseModel):
    area_name: str
    area_category: str
    property_type: str
    total_area: float
    bedrooms: int
    bathrooms: int
    kitchens: int
    floors: int
    parking: int
    furnished: str
    electricity_backup: str
    gas_available: str
    distance_city_center: float
    near_school: str
    near_market: str