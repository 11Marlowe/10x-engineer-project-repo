"""PromptLab API Server

Run with: python main.py
"""

import uvicorn
from app.api import app
from fastapi import FastAPI

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust based on your frontend location or use ["*"] for development/testing
    allow_credentials=True,
    allow_methods=["*"],  # This allows all methods (GET, POST, etc.). Customize as needed.
    allow_headers=["*"],  # This allows all headers. Customize as needed.
)

# Start your application with uvicorn, or however the app is started
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
