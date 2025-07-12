import json
import os

MEMORY_FILE = "app/utils/memory_store.json"

def get_conversation_memory(session_id: str):
    if not os.path.exists(MEMORY_FILE):
        return ""

    with open(MEMORY_FILE, 'r') as f:
        data = json.load(f)

    return "\n".join(data.get(session_id, []))

def update_conversation_memory(session_id: str, user_msg: str, bot_reply: str):
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    convo = data.get(session_id, [])
    convo.append(f"User: {user_msg}\nAI: {bot_reply}")
    data[session_id] = convo

    with open(MEMORY_FILE, 'w') as f:
        json.dump(data, f, indent=2)
