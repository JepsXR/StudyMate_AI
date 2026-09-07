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
    print("Sucessfull Connection with a API Key")

logging.basicConfig(level=logging.INFO)

# 3. USERDATA DEVELOPING

class StudentData(BaseModel):

    name: str = Field(...,min_length=3, max_length=20)
    age: int = Field(...,gt=10, lt=100)
    strongest_learning_style: Literal["Visual", "Auditory", "Kinesthetic", "Reading/Writing", "Other"] = Field(...,)
    info_learning_style: str = Field(...,
        min_lenght=20, 
        max_lenght=100)
    available_hours_per_day: float = Field(gt=0, lt=24)
    study_subjects: List[str] = Field(...,
        default_factory=list, 
        max_length=4
        )
    concentration_level: Literal["Low", "Moderate", "High"] = Field(...,)
    info_exam: str = Field(
        ...,
        min_length=10,
        max_length=100)
