import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# File Upload Directory
UPLOAD_DIR = "data/uploads"

# Database path for CRM
DB_PATH = "db/database.db"

# Vector store paths
VECTOR_INDEX_PATH = "data/vector.index"
VECTOR_DATA_PATH = "data/vector_data.pkl"
