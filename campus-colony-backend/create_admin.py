from app.database import SessionLocal


from app.models.user import User
from app.models.review import Review
from app.models.listing import Listing
from app.models.area import Area
from app.models.landlord import Landlord

from app.utils.security import hash_password

db = SessionLocal()

admin = User(
    name="Admin",
    email="admin@gmail.com",
    password=hash_password("admin123"),
    role="admin"
)

db.add(admin)
db.commit()

print("Admin created successfully!")