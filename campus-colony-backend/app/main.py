from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def root():
    return {"message": "Campus Colony API running"}