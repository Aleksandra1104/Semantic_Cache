CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS qa_cache (
    id SERIAL PRIMARY KEY,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    category TEXT,
    embedding VECTOR(384),
    created_at TIMESTAMP DEFAULT NOW(),
    hit_count INT DEFAULT 0
);