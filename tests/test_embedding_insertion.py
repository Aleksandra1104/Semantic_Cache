# from insert_with_embedding import insert_qa
from insert_pgvector import insert_qa

question = input("Question: ")
answer = input("Answer: ")
category = input("Category: ")

insert_qa(question, answer, category)

print("Saved.")