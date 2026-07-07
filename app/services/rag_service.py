from app.models.document_chunk import DocumentChunk

from app.services.embedding_service import embedding_service
from app.services.search_service import search_service
from app.services.azure_openai_service import azure_openai_service


class RAGService:
    """Combines retrieval and generation."""

    def answer(
        self,
        question: str,
        knowledge_base: list[DocumentChunk]
    ) -> str:

        # Generate an embedding for the user's question
        question_embedding = embedding_service.create_embedding(question)

        # Find the most relevant chunks
        matches = search_service.search(
            question_embedding,
            knowledge_base,
            top_k=3
        )

        # Build the context from the retrieved chunks
        context = "\n\n".join(
            chunk.text for chunk, _ in matches
        )

        # Build the prompt
        prompt = f"""
You are an internal company assistant.

Answer ONLY using the information below.

If the answer is not found, respond with:

"I couldn't find that information in the company documents."

Company Documents:

{context}

Question:

{question}
"""

        return azure_openai_service.chat(prompt)


rag_service = RAGService()