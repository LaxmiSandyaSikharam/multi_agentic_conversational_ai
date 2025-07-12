from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.llm_service import generate_llm_response

router = APIRouter()

# Input format for /chat POST endpoint
class ChatRequest(BaseModel):
    session_id: str
    message: str

# Output format
class ChatResponse(BaseModel):
    reply: str
    metadata: dict

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        reply, metadata = generate_llm_response(
            session_id=request.session_id,
            message=request.message
        )
        return ChatResponse(reply=reply, metadata=metadata)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
