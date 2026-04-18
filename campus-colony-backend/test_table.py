from app.database import engine
from sqlalchemy import text

with engine.connect() as conn:
    # Shows all tables in your database
    result = conn.execute(text("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public'
    """))
    print("=== TABLES IN YOUR DATABASE ===")
    for row in result:
        print(row[0])

    # Shows all columns in listings table
    result2 = conn.execute(text("""
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_name = 'listings'
    """))
    print("\n=== COLUMNS IN LISTINGS TABLE ===")
    for row in result2:
        print(f"  {row[0]} → {row[1]}")
