import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

from app.db import get_connection
from app.embedder import get_embedding

query = "I can't access Canvas. Working from home."

query_embedding = np.array(
    get_embedding(query)
).reshape(1, -1)

conn = get_connection()
cur = conn.cursor()

cur.execute(
    """
    SELECT
        id,
        question,
        answer,
        embedding
    FROM qa_cache
    WHERE embedding IS NOT NULL;
    """
)

rows = cur.fetchall()

best_score = -1
best_match = None

for row in rows:
    row_id, question, answer, embedding = row

    db_embedding = np.array(embedding).reshape(1, -1)

    similarity = cosine_similarity(
        query_embedding,
        db_embedding
    )[0][0]

    print(f"{question} -> {similarity:.4f}")

    if similarity > best_score:
        best_score = similarity
        best_match = row

print("\nBEST MATCH:")
print(best_match)
print("Score:", best_score)

cur.close()
conn.close()