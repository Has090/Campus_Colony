from app.database import SessionLocal
from app.models.user import User
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