from app.database import engine, Base
from sqlalchemy import text, inspect

# Import ALL models
from app.models.user import User
from app.models.listing import Listing
from app.models.review import Review
from app.models.area import Area

print("Connecting to Neon database...")

with engine.connect() as conn:
    print("Dropping tables...")
    conn.execute(text("DROP TABLE IF EXISTS reviews CASCADE;"))
    conn.execute(text("DROP TABLE IF EXISTS listings CASCADE;"))
    conn.execute(text("DROP TABLE IF EXISTS users CASCADE;"))
    conn.execute(text("DROP TABLE IF EXISTS areas CASCADE;"))
    conn.commit()
    print("All tables dropped.")

print("Creating fresh tables...")
Base.metadata.create_all(bind=engine)

# Verify what was created
inspector = inspect(engine)
tables = inspector.get_table_names()
print(f"\nTables now in database: {tables}")

# Show columns of listings table
cols = inspector.get_columns("listings")
print("\nColumns in listings table:")
for col in cols:
    print(f"  - {col['name']} ({col['type']})")