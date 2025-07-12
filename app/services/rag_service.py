from app.utils.vector_store import search_similar_chunks

def retrieve_relevant_context(query: str) -> str:
    results = search_similar_chunks(query)
    return "\n".join([r['content'] for r in results])
