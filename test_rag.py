from app.services.ingestion_service import ingestion_service
from app.services.rag_service import rag_service

knowledge_base = ingestion_service.ingest_document(
    "sample_data/employee_handbook.pdf"
)

answer = rag_service.answer(
    "How many vacation leave days do employees receive?",
    knowledge_base
)

print(answer)