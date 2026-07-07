from app.services.ingestion_service import ingestion_service
from app.services.embedding_service import embedding_service
from app.services.search_service import search_service

knowledge_base = ingestion_service.ingest_document(
    "sample_data/employee_handbook.pdf"
)

question = "How many vacation leave days do employees have?"

question_embedding = embedding_service.create_embedding(question)

results = search_service.search(
    question_embedding,
    knowledge_base
)

print("\nQUESTION:")
print(question)

print("\nTOP MATCHES:\n")

for i, (chunk, score) in enumerate(results):

    print("=" * 80)
    print(f"Rank #{i+1}")
    print(f"Similarity: {score:.4f}")
    print(chunk.text[:350])
    print()