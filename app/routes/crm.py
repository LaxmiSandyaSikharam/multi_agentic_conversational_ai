from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.services.crm_service import create_user, update_user, get_conversation_history

router = APIRouter()

class UserCreateRequest(BaseModel):
    name: str
    email: str
    company: Optional[str] = None
    preferences: Optional[str] = None

class UserUpdateRequest(BaseModel):
    user_id: int
    name: Optional[str]
    email: Optional[str]
    company: Optional[str]
    preferences: Optional[str]

@router.post("/create_user")
def create(user: UserCreateRequest):
    try:
        user_id = create_user(user)
        return {"user_id": user_id, "status": "created"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/update_user")
def update(user: UserUpdateRequest):
    try:
        success = update_user(user)
        return {"updated": success}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/conversations/{user_id}")
def fetch_conversations(user_id: int):
    try:
        history = get_conversation_history(user_id)
        return {"user_id": user_id, "conversations": history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
