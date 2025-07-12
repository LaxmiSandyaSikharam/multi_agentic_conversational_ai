from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import chat, upload, crm

app = FastAPI(
    title="Multi-Agentic Conversational AI System",
    description="LLM + RAG + CRM chatbot",
    version="1.0.0"
)

# Allow CORS (for testing with Postman or browser)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(upload.router, prefix="/upload_docs", tags=["Document Upload"])
app.include_router(crm.router, prefix="/crm", tags=["CRM"])
