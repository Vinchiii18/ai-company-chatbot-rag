import numpy as np

from app.models.document_chunk import DocumentChunk


class SearchService:
    """Simple semantic search using cosine similarity."""

    def cosine_similarity(
        self,
        embedding1: list[float],
        embedding2: list[float]
    ) -> float:

        a = np.array(embedding1)
        b = np.array(embedding2)

        return np.dot(a, b) / (
            np.linalg.norm(a) * np.linalg.norm(b)
        )

    def search(
        self,
        question_embedding: list[float],
        chunks: list[DocumentChunk],
        top_k: int = 3
    ):

        scores = []

        for chunk in chunks:

            similarity = self.cosine_similarity(
                question_embedding,
                chunk.embedding
            )

            scores.append(
                (chunk, similarity)
            )

        scores.sort(
            key=lambda x: x[1],
            reverse=True
        )

        return scores[:top_k]


search_service = SearchService()