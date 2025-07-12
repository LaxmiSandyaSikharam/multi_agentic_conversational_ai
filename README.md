# 🧠 Multi-Agentic Conversational AI System

A modular FastAPI application that integrates **LLM**, **RAG (Retrieval-Augmented Generation)**, and **CRM logging** to provide conversational capabilities grounded in document knowledge.

---

## 🚀 Features

- 🤖 LLM-based chatbot using OpenAI
- 📄 Document upload and ingestion for context-aware conversation
- 📚 Embedding and vector search using `sentence-transformers` and `FAISS`
- 🧠 Memory persistence with user sessions
- 🧾 Lightweight CRM module to log user conversations
- 🧪 Interactive Swagger UI for testing

---

## 📁 Folder Structure

multi_agentic_conversational_ai/
├── app/
│ ├── main.py # FastAPI app entrypoint
│ ├── config.py # Configuration loader
│ ├── routes/ # API route handlers
│ ├── services/ # Core services (LLM, RAG, CRM)
│ └── utils/ # Helpers (memory, vector store, loader)
├── data/uploads/ # Uploaded knowledge base files (CSV/PDF/TXT)
├── db/ # SQLite database for CRM logs
├── .env # API keys and settings
├── requirements.txt # Python dependencies
└── README.md # You’re reading it!

yaml



---

## ⚙️ Setup Instructions

### ✅ 1. Clone and Navigate

```bash
git clone <your-repo-url>
cd multi_agentic_conversational_ai
✅ 2. Create a Conda Environment
bash

conda create -n agentic-ai python=3.10 -y
conda activate agentic-ai
✅ 3. Install Requirements
bash

pip install -r requirements.txt
If you face issues with faiss-cpu or sentence-transformers, install manually:

bash

pip install faiss-cpu sentence-transformers
🔐 .env File Setup
Create a .env file in the root:

ini

OPENAI_API_KEY=your_openai_key_here
▶️ Running the App
bash

uvicorn app.main:app --reload
Then open http://127.0.0.1:8000/docs to explore Swagger UI.

📂 Upload Your Dataset
Go to POST /upload_docs in Swagger UI.

Upload a .csv, .txt, or .pdf file.

The file is stored in data/uploads/.

Embeddings are generated and stored for retrieval.

💬 Start Chatting
Use POST /chat/ with:

json

{
  "session_id": "test-session",
  "message": "What did I upload?",
  "user_id": 1
}
The chatbot will answer using the uploaded documents.

📋 CRM Endpoints
POST /crm/create_user: Create user profile.

PUT /crm/update_user: Update user preferences.

GET /crm/conversations/{user_id}: Fetch chat logs.

🧠 Tech Stack
Layer	Tool
API Server	FastAPI
LLM	OpenAI GPT via API
Embedding	Sentence Transformers
Vector Store	FAISS
Memory	Session-based in Python
Storage	SQLite3

📌 Notes
Tested on Python 3.10 with Anaconda

Windows users may need to run terminal in Admin mode to avoid caching/symlink errors from HuggingFace

Compatible with .csv, .txt, and .pdf documents

🧪 Sample API Test
bash

curl -X POST http://127.0.0.1:8000/chat/ \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "demo-session",
    "message": "Summarize the uploaded document",
    "user_id": 1
}'
🧑‍💻 Author
Laxmi Sandya Sikharam
Data Analyst | AI Enthusiast | Builder

📃 License
MIT License © 2025 Laxmi Sandya Sikharam

yaml

---

Would you like a `.pdf` version or want this uploaded into your project directly?