from app.services.azure_openai_service import AzureOpenAIService

service = AzureOpenAIService()

reply = service.chat("Hello! Tell me about yourself in one sentence.")

print(reply)