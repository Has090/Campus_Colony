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



