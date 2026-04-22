import os
import psycopg2
from dotenv import load_dotenv

# Load env from the backend directory
load_dotenv(dotenv_path="/Users/nishkarshsharma/Documents/Projectssss/backend/backend/.env")

db_url = os.environ.get("DATABASE_URL")
print(f"Testing connection to: {db_url.split('@')[-1] if db_url else 'None'}")

if not db_url:
    print("Error: DATABASE_URL not found")
    exit(1)

try:
    conn = psycopg2.connect(db_url)
    print("Successfully connected to Supabase!")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")
