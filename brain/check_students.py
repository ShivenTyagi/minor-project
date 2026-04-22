import os
import psycopg2
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Users/nishkarshsharma/Documents/Projectssss/backend/backend/.env")
db_url = os.environ.get("DATABASE_URL")

try:
    conn = psycopg2.connect(db_url)
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM students;")
    count = cur.fetchone()[0]
    print(f"Number of students in database: {count}")
    conn.close()
except Exception as e:
    print(f"Error checking table: {e}")
