import time
from openai import OpenAI
from app.config import OPENAI_API_KEY
from app.utils.memory import get_conversation_memory, update_conversation_memory
from app.services.rag_service import retrieve_relevant_context
from app.services.crm_service import log_conversation

client = OpenAI(api_key=OPENAI_API_KEY)

MODEL_NAME = "gpt-3.5-turbo"

def generate_llm_response(session_id: str, message: str, user_id: int = None):
    start_time = time.time()

    # 1. Retrieve memory
    memory = get_conversation_memory(session_id)

    # 2. Retrieve relevant context from RAG
    context = retrieve_relevant_context(message)

    # 3. Construct prompt
    prompt = f"""
You are a helpful assistant.
Here is some relevant information:
{context}

Conversation history:
{memory}

User: {message}
AI:"""

    # 4. Make OpenAI API call with new SDK
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )

    reply = response.choices[0].message.content.strip()

    # 5. Update memory
    update_conversation_memory(session_id, message, reply)

    # 6. Optional: log to CRM
    if user_id is not None:
        log_conversation(user_id, message, reply)

    return reply, {"response_time": round(time.time() - start_time, 2)}
