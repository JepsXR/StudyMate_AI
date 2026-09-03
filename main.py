# IMPORTS

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from dotenv import load_dotenv
import json
import os
import google.generativeai as genai
import logging
import psycopg

# SERVER ACTIVATION 

app = FastAPI(
    title="StudyMateAI",
    description="StudyMateAI is an AI agent that can help you with the design of your study strategies",
    version="1.0.0"
)

load_dotenv()

keyapi = os.getenv("STUDYMATE_API_KEY")
if not keyapi:
    print("ERROR: API KEY NOT FOUNDED")
else:
    genai.configure(api_key = keyapi)

# 3. USERDATA DEVELOPING

class UserData(BaseModel):

    name: str = Field(min_length=3, max_length=20)
    age: int = Field(...,gt=10, lt=100)
    learning_style: Literal["Visual", "Auditory", "Kinesthetic", "Reading/Writing"] = Field(...,)
    available_hours_per_day: float = Field(gt=0, lt=24)
