from app.services.embedding_service import embedding_service

embedding = embedding_service.create_embedding(
    "Employees receive 15 vacation leave days."
)

print(type(embedding))
print(len(embedding))
print(embedding[:10])