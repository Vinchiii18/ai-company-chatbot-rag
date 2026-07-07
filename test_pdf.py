from app.services.document_service import document_service

text = document_service.extract_text(
    "sample_data/employee_handbook.pdf"
)

print(text[:3000])