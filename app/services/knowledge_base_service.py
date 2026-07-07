from app.models.document_chunk import DocumentChunk
from app.services.storage_service import storage_service


class KnowledgeBaseService:
    """Keeps the knowledge base loaded in memory."""

    def __init__(self):
        self._knowledge_base: list[DocumentChunk] = []

    def load(self, file_path: str):
        """Load the knowledge base from a JSON file."""

        data = storage_service.load(file_path)

        self._knowledge_base = [
            DocumentChunk(
                text=item["text"],
                embedding=item["embedding"]
            )
            for item in data
        ]

    def get_chunks(self) -> list[DocumentChunk]:
        """Return all loaded document chunks."""

        return self._knowledge_base

    def reload(self, file_path: str):
        """Reload the knowledge base."""

        self.load(file_path)


knowledge_base_service = KnowledgeBaseService()