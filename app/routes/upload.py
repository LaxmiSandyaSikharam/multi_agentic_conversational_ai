from fastapi import APIRouter, UploadFile, File, HTTPException
import os
from app.utils.document_loader import ingest_document
from app.config import UPLOAD_DIR

router = APIRouter()

@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    try:
        os.makedirs(UPLOAD_DIR, exist_ok=True)
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        # Ingest into vector store
        num_chunks = ingest_document(file_path)

        return {
            "filename": file.filename,
            "status": "indexed",
            "chunks_indexed": num_chunks
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
