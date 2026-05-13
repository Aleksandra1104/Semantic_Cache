from app.db import get_connection
from app.embedder import get_embedding
from pgvector.psycopg2 import register_vector


def insert_qa(question: str, answer: str, category: str | None = None):

    embedding = get_embedding(question)

    conn = get_connection()

    register_vector(conn)

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO qa_cache (
            question,
            answer,
            category,
            embedding
        )
        VALUES (%s, %s, %s, %s);
        """,
        (
            question,
            answer,
            category,
            embedding
        )
    )

    conn.commit()

    cur.close()
    conn.close()