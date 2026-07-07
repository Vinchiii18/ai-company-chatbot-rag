from app.services.document_service import document_service
from app.services.chunking_service import chunking_service
from app.services.embedding_service import embedding_service

text = document_service.extract_text(
    "sample_data/employee_handbook.pdf"
)

chunks = chunking_service.chunk_text(text)

print(f"Total chunks: {len(chunks)}\n")

for i, chunk in enumerate(chunks):

    embedding = embedding_service.create_embedding(chunk)

    print(f"Chunk {i+1}")
    print(f"Characters: {len(chunk)}")
    print(f"Embedding Dimensions: {len(embedding)}")
    print("-" * 60)