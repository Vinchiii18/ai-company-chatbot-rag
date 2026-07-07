import fitz


class DocumentService:

    def extract_text(self, file_path: str):

        document = fitz.open(file_path)

        text = ""

        for page in document:
            text += page.get_text()

        return text


document_service = DocumentService()