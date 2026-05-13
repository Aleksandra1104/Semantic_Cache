from app.db import get_connection
from app.embedder import get_embedding
from pgvector.psycopg2 import register_vector


def search_similar(query: str, limit: int = 3):
    query_embedding = get_embedding(query)

    conn = get_connection()
    register_vector(conn)

    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            id,
            question,
            answer,
            category,
            hit_count,
            1 - (embedding <=> %s::vector) AS similarity
        FROM qa_cache
        WHERE embedding IS NOT NULL
        ORDER BY embedding <=> %s::vector
        LIMIT %s;
        """,
        (query_embedding, query_embedding, limit)
    )

    results = cur.fetchall()

    cur.close()
    conn.close()

    return results


if __name__ == "__main__":
    query = input("Search query: ")

    results = search_similar(query)

    for row in results:
        row_id, question, answer, category, similarity = row
        print(f"\nID: {row_id}")
        print(f"Question: {question}")
        print(f"Answer: {answer}")
        print(f"Category: {category}")
        print(f"Similarity: {similarity:.4f}")