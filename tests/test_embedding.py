from app.embedder import get_embedding

text = "How do I reset my password?"

embedding = get_embedding(text)

print(type(embedding))
print(len(embedding))
print(embedding[:10])