from dataclasses import dataclass

@dataclass
class DocumentChunk:
    text: str
    embedding: list[float]