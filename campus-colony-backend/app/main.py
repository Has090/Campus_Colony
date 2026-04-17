from fastapi import FastAPI
from app.database import Base, engine
from app.models.area import Area

from app.routes.areas import router as areas_router
from app.routes.auth import router as auth_router
#from app.routes.admin import router as admin_router
from app.routes.landlords import router as landlords_router
from app.routes.listings import router as listings_router
app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(areas_router, prefix="/areas", tags=["Areas"])
#app.include_router(admin_router, prefix="/admin", tags=["Admin"])
app.include_router(landlords_router, prefix="/landlords", tags=["Landlords"])
app.include_router(listings_router, prefix="/listings", tags=["Listings"])

@app.get("/")
def root():
    return {"message": "Campus Colony API running"}

from sqlalchemy import text

@app.get("/tables")
def get_tables():
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema='public';
        """))
        return [row[0] for row in result]


@app.get("/drop-all")
def drop_all():
    with engine.connect() as conn:
        conn.execute(text("""
            DO $$ DECLARE
                r RECORD;
            BEGIN
                FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public')
                LOOP
                    EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
                END LOOP;
            END $$;
        """))
        conn.commit()
    return {"message": "All tables dropped"}



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