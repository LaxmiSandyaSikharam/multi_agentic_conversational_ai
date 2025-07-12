import faiss
import os
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer
from app.config import VECTOR_INDEX_PATH, VECTOR_DATA_PATH

EMBEDDING_MODEL = SentenceTransformer('all-MiniLM-L6-v2')

def search_similar_chunks(query, top_k=3):
    if not os.path.exists(VECTOR_INDEX_PATH) or not os.path.exists(VECTOR_DATA_PATH):
        return []

    query_vec = EMBEDDING_MODEL.encode([query]).astype('float32')

    index = faiss.read_index(VECTOR_INDEX_PATH)
    with open(VECTOR_DATA_PATH, 'rb') as f:
        documents = pickle.load(f)

    D, I = index.search(query_vec, top_k)
    return [documents[i] for i in I[0] if i < len(documents)]
