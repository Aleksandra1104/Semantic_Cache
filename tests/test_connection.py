import os
from dotenv import load_dotenv
from app.db import get_connection

load_dotenv()
print("DATABASE_URL:", os.getenv("DATABASE_URL"))

conn = get_connection()
cur = conn.cursor()

cur.execute("""
    SELECT
        current_database(),
        current_user,
        inet_server_addr(),
        inet_server_port(),
        version();
""")
print("Connection info:", cur.fetchone())

cur.execute("""
    SELECT extname, extversion
    FROM pg_extension;
""")
print("Extensions:", cur.fetchall())

cur.close()
conn.close()