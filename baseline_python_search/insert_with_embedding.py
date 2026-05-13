import json
from app.db import get_connection
from app.embedder import get_embedding


def insert_qa(question: str, answer: str, category: str | None = None) -> None:


    embedding = json.dumps(get_embedding(question))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO qa_cache (question, answer, category, embedding)
        VALUES (%s, %s, %s, %s);
        """,
        (question, answer, category, embedding)
    )

    conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":
    insert_qa(
        question="How do I reset my password?",
        answer="Use the password reset portal.",
        category="account"
    )

    print("Inserted successfully.")