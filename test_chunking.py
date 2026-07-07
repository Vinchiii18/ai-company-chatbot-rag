from app.services.document_service import document_service
from app.services.chunking_service import chunking_service

text = document_service.extract_text(
    "sample_data/employee_handbook.pdf"
)

chunks = chunking_service.chunk_text(text)

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print("=" * 60)
    print(f"Chunk {i+1}")
    print(chunk)