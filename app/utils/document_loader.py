import os
import pickle
import faiss
import numpy as np
from app.config import VECTOR_INDEX_PATH, VECTOR_DATA_PATH
from sentence_transformers import SentenceTransformer
from PyPDF2 import PdfReader
import csv
import json

EMBEDDING_MODEL = SentenceTransformer('all-MiniLM-L6-v2')

def extract_text(file_path: str) -> str:
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == ".pdf":
        reader = PdfReader(file_path)
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    elif ext == ".txt":
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    elif ext == ".csv":
        with open(file_path, 'r', encoding='utf-8') as f:
            return "\n".join([" ".join(row) for row in csv.reader(f)])
    elif ext == ".json":
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.dumps(json.load(f), indent=2)
    else:
        raise ValueError("Unsupported file type")

def chunk_text(text: str, chunk_size=300, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def ingest_document(file_path: str) -> int:
    text = extract_text(file_path)
    chunks = chunk_text(text)

    embeddings = EMBEDDING_MODEL.encode(chunks).astype('float32')

    if os.path.exists(VECTOR_INDEX_PATH):
        index = faiss.read_index(VECTOR_INDEX_PATH)
        with open(VECTOR_DATA_PATH, 'rb') as f:
            stored_docs = pickle.load(f)
    else:
        index = faiss.IndexFlatL2(embeddings.shape[1])
        stored_docs = []

    start_id = len(stored_docs)
    stored_docs += [{"id": i + start_id, "content": chunk} for i, chunk in enumerate(chunks)]
    index.add(embeddings)

    faiss.write_index(index, VECTOR_INDEX_PATH)
    with open(VECTOR_DATA_PATH, 'wb') as f:
        pickle.dump(stored_docs, f)

    return len(chunks)
