from fastapi import FastAPI
from app.database import Base, engine
from sqlalchemy import text

from app.models.listing import Listing
from app.models.landlord import Landlord
from app.models.area import Area

from app.routes.areas import router as areas_router
from app.routes.auth import router as auth_router
#from app.routes.admin import router as admin_router
from app.routes.landlords import router as landlords_router
from app.routes.listings import router as listings_router
from app.routes.ai import router as ai_router
app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(areas_router, prefix="/areas", tags=["Areas"])
#app.include_router(admin_router, prefix="/admin", tags=["Admin"])
app.include_router(landlords_router, prefix="/landlords", tags=["Landlords"])
app.include_router(listings_router, prefix="/listings", tags=["Listings"])
app.include_router(ai_router, prefix="/ai", tags=["AI Model"])

@app.get("/")
def root():
    return {"message": "Campus Colony API running"}


@app.get("/tables")
def get_tables():
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema='public';
        """))
        return [row[0] for row in result]


@app.post("/reset-db")
def reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    return {"message": "Database reset successfully"}



@app.get("/schema")
def get_schema():
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT 
                table_name,
                column_name,
                data_type
            FROM information_schema.columns
            WHERE table_schema = 'public'
            ORDER BY table_name, ordinal_position;
        """))

        schema = {}

        for table, column, dtype in result:
            if table not in schema:
                schema[table] = []
            schema[table].append({
                "column": column,
                "type": dtype
            })

        return schema
