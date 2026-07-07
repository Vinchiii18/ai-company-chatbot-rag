import json
from pathlib import Path

from app.models.document_chunk import DocumentChunk


class StorageService:
    """Handles saving and loading the knowledge base."""

    def save(
        self,
        knowledge_base: list[DocumentChunk],
        file_path: str
    ) -> None:

        data = []

        for chunk in knowledge_base:
            data.append({
                "text": chunk.text,
                "embedding": chunk.embedding
            })

        Path(file_path).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load(self, file_path: str):

        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)


storage_service = StorageService()