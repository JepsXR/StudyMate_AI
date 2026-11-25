# 1. IMPORTS

from fastapi import FastAPI, HTTPException, APIRouter

# 2. SERVER ACTIVATION 

app = FastAPI(
    title="StudyMateAI",
    description="StudyMateAI is an AI agent that can help you with the design of your study strategies",
    version="1.0.0"
)

app.include_router()