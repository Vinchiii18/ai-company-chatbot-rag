from app.models.document_chunk import DocumentChunk

from app.services.document_service import document_service
from app.services.chunking_service import chunking_service
from app.services.embedding_service import embedding_service
from app.services.storage_service import storage_service


class IngestionService:
    """Processes a document into searchable chunks with embeddings."""

    def ingest_document(self, file_path: str) -> list[DocumentChunk]:

        text = document_service.extract_text(file_path)

        chunks = chunking_service.chunk_text(text)

        knowledge_base = []

        for chunk in chunks:

            embedding = embedding_service.create_embedding(chunk)

            knowledge_base.append(
                DocumentChunk(
                    text=chunk,
                    embedding=embedding
                )
            )

        return knowledge_base


ingestion_service = IngestionService()