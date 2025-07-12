from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from app.services.llm_service import generate_llm_response

router = APIRouter()

# ✅ Request model
class ChatRequest(BaseModel):
    session_id: str
    message: str
    user_id: Optional[int] = None

# ✅ Metadata model for structured Swagger view
class ChatMetadata(BaseModel):
    source: Optional[str] = Field(None, description="Where the response was sourced from")
    tokens_used: Optional[int] = Field(None, description="Total tokens used for the reply")
    model: Optional[str] = Field(None, description="LLM model used to generate the response")
    confidence_score: Optional[float] = Field(None, description="AI's confidence score for the reply")

# ✅ Response model
class ChatResponse(BaseModel):
    reply: str = Field(..., description="The AI-generated response")
    metadata: ChatMetadata = Field(..., description="Additional context about the response")

# ✅ Route
@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        reply, metadata_dict = generate_llm_response(
            session_id=request.session_id,
            message=request.message,
            user_id=request.user_id
        )
        # 👇 Convert dict to ChatMetadata
        metadata = ChatMetadata(**metadata_dict)
        return ChatResponse(reply=reply, metadata=metadata)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

