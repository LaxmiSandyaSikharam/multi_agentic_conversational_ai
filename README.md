
# Multi-Agentic Conversational AI System

This project is a Python-based RESTful API application designed to enable natural language conversations with a Large Language Model (LLM). It integrates Retrieval-Augmented Generation (RAG) and a lightweight CRM system to store and retrieve user information during conversations.

---

## Features

- **Conversational Chatbot with RAG**
  - Accepts user messages via API.
  - Retrieves relevant documents dynamically from the internal knowledge base.
  - Integrates LLM (OpenAI GPT API) for contextual awareness.

- **CRM Integration**
  - Captures and stores user details like name, email, preferences.
  - Provides API endpoints to view, update, or delete CRM data.

- **API-first Design**
  - Swagger UI available at `/docs` for testing.

- **Scalable Structure**
  - Modular design for easy future integration of frontend (React/Vue).

---

## Folder Structure
```
multi_agentic_conversational_ai/
│
├── app/               # Backend API and logic
│   ├── routes/        # API route definitions
│   ├── services/      # Business logic for LLM, RAG, CRM
│   ├── utils/         # Utility scripts (e.g., vector store)
│   ├── main.py        # Entry point for the FastAPI server
│   ├── config.py      # Configuration and environment loading
│
├── data/              # Placeholder for datasets or static files
├── db/                # Placeholder for database files (SQLite, etc.)
├── requirements.txt   # Python dependencies
├── .env               # Environment variables (add your API keys here)
├── README.md          # Project documentation
```

---

## Getting Started

### Prerequisites
- Python 3.10+ installed ([Download Python](https://www.python.org/downloads/))
- pip package manager (comes with Python)
- (Optional for frontend) Node.js & npm ([Download Node.js](https://nodejs.org/))

---

### Backend Setup

1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/multi_agentic_conversational_ai.git
cd multi_agentic_conversational_ai
```

2. **Set up virtual environment**
```bash
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scriptsctivate
# On Mac/Linux:
source venv/bin/activate
```

3. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
- Rename `.env.example` (if exists) to `.env`.
- Add your OpenAI API key and other configurations.
```bash
OPENAI_API_KEY=sk-xxxxxxx
```

5. **Run the FastAPI server**
```bash
uvicorn app.main:app --reload
```

6. **Test API in Browser**
Open: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### Frontend Setup (Optional)
Currently, there is no frontend bundled. You can:
- Build a React or Vue frontend.
- Serve it in the `frontend/` directory.

**Example Placeholder Steps:**
```bash
cd frontend
npm install
npm run build
```

---

## API Endpoints

| Endpoint                  | Method | Description                               |
|---------------------------|--------|-------------------------------------------|
| `/chat`                   | POST   | Send a message to the LLM chatbot         |
| `/upload_docs`            | POST   | Upload documents for RAG context          |
| `/crm/create_user`        | POST   | Create a new CRM user                     |
| `/crm/conversations/{id}` | GET    | Retrieve user conversation history        |

Explore all endpoints at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## User Manual

This section provides additional details for interacting with the API.

### Features

- **Conversational Chatbot with RAG**
  - Accepts user messages via API.
  - Retrieves relevant documents dynamically from the internal knowledge base.
  - Integrates Large Language Models (LLM) for contextual awareness.

- **CRM Integration**
  - Captures and stores user details like name, email, and preferences.
  - Provides API endpoints to view, update, or delete CRM data.

- **Interactive API Documentation**
  - Swagger UI available at `/docs` for easy testing and exploration.

---

### Example API Usage

#### Chat API Example
**Request**
```json
POST /chat
{
  "message": "Hello, what can you do?"
}
```

**Response**
```json
{
  "response": "Hi! I can assist you with knowledge retrieval and user management. How can I help?"
}
```

---

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## License
This project is licensed under the MIT License.

---

## Acknowledgements
- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI](https://openai.com/)
- [HuggingFace Sentence Transformers](https://www.sbert.net/)
- [FAISS](https://faiss.ai/)

