from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Company Knowledge Chatbot API",
    version="1.0.0"
)

app.include_router(router, prefix="/api")


@app.get("/")
def home():
    return {
        "message": "Company Knowledge Chatbot API"
    }