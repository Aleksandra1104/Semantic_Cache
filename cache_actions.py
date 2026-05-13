from app.db import get_connection


def increment_hit_count(row_id: int) -> None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE qa_cache
        SET hit_count = hit_count + 1
        WHERE id = %s;
        """,
        (row_id,)
    )

    conn.commit()
    cur.close()
    conn.close()