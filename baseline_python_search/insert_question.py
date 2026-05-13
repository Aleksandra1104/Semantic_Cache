from app.db import get_connection

conn = get_connection()
cur = conn.cursor()

question = "How do I unlock my account?"
answer = "Contact IT support or use the account recovery portal."
category = "account"

cur.execute(
    """
    INSERT INTO qa_cache (question, answer, category)
    VALUES (%s, %s, %s);
    """,
    (question, answer, category)
)

conn.commit()

cur.close()
conn.close()

print("Question saved successfully.")