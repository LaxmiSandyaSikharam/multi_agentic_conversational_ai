from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
import os

from app.routes import chat, upload, crm

# Disable FastAPI’s automatic Swagger docs
app = FastAPI(
    title="Multi-Agentic Conversational AI System",
    description="LLM + RAG + CRM chatbot",
    version="1.0.0",
    docs_url=None,  # Disable default /docs
    redoc_url=None  # Disable default /redoc
)

# Mount static directory for logo
current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(current_dir, "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Optional: Serve frontend (if added later)
if os.path.exists("frontend/index.html"):
    @app.get("/")
    def serve_homepage():
        return FileResponse(os.path.join("frontend", "index.html"))

    app.mount("/frontend_static", StaticFiles(directory="frontend"), name="frontend_static")

# Serve custom Swagger UI with large logo banner
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Multi-Agentic Conversational AI Docs</title>
        <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist/swagger-ui.css">
        <link rel="icon" href="/static/logo.png" type="image/png">
        <style>
            body {{
                margin: 0;
                font-family: Arial, sans-serif;
            }}
            .header {{
                background-color: #1E1E1E;
                color: white;
                text-align: center;
                padding: 30px 20px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            }}
            .header img {{
                height: 120px; /* 👈 Bigger logo */
                margin-bottom: 15px;
            }}
            .header h1 {{
                font-size: 2rem;
                margin: 0;
            }}
            #swagger-ui {{
                margin-top: 20px;
                padding: 0 15px;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <img src="/static/logo.png" alt="Logo">
            <h1>Multi-Agentic Conversational AI Docs</h1>
        </div>
        <div id="swagger-ui"></div>
        <script src="https://unpkg.com/swagger-ui-dist/swagger-ui-bundle.js"></script>
        <script>
            const ui = SwaggerUIBundle({{
                url: '{app.openapi_url}',
                dom_id: '#swagger-ui',
                deepLinking: true,
                presets: [
                    SwaggerUIBundle.presets.apis,
                    SwaggerUIBundle.SwaggerUIStandalonePreset
                ],
                layout: "BaseLayout"
            }});
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

# Include API routes
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(upload.router, prefix="/upload_docs", tags=["Document Upload"])
app.include_router(crm.router, prefix="/crm", tags=["CRM"])
