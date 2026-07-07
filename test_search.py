from app.services.document_service import document_service
from app.services.chunking_service import chunking_service
from app.services.embedding_service import embedding_service
from app.services.search_service import search_service

# Load document
text = document_service.extract_text(
    "sample_data/employee_handbook.pdf"
)

# Split into chunks
chunks = chunking_service.chunk_text(text)

# Generate embeddings
chunk_embeddings = []

for chunk in chunks:
    embedding = embedding_service.create_embedding(chunk)
    chunk_embeddings.append((chunk, embedding))

# Ask a question
question = "How many vacation leave days do employees have?"

question_embedding = embedding_service.create_embedding(question)

# Search
results = search_service.search(
    question_embedding,
    chunk_embeddings
)

print("\nQUESTION:")
print(question)

print("\nTOP MATCHES:\n")

for i, (chunk, score) in enumerate(results):

    print("=" * 80)
    print(f"Rank #{i+1}")
    print(f"Similarity: {score:.4f}")
    print(chunk[:350])
    print()