from pydantic import BaseModel

class Admin_User_Mangaement(BaseModel):
    total_users: int
    total_students: int
    total_landlords: int
    total_listings: int
    active_listings: int
    total_reviews: int


# This matches the "Top Cards" on your dashboard
class DashboardStats(BaseModel):
    total_listings: int
    total_users: int
    avg_area_score: float
    listings_growth: int  # The "+48 this week" part

# This matches one row in your "Recent Listings" table
class ListingSummary(BaseModel):
    property_name: str
    property_type: str
    area: str
    score: int
    price: float
    status: str

    class Config:
        from_attributes = True    