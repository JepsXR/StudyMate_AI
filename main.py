# 1. IMPORTS

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Literal
from dotenv import load_dotenv
from sqlalchemy import String, create_engine, Enum, CheckConstraint
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column
import json
import os
import google.generativeai as genai
import logging
import psycopg

# 2. SERVER ACTIVATION 

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
        min_length=20, 
        max_length=100)
    available_hours_per_day: float = Field(gt=0, lt=24)
    study_subjects: List[str] = Field(
        default_factory=list, 
        max_length=4
        )
    concentration_level: Literal["Low", "Moderate", "High"] = Field(...,)
    info_exam: str = Field(
        ...,
        min_length=10,
        max_length=100)

# 4. DATABASE CREATION

connection = psycopg.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

engine = create_engine("DATABASE_URL")
SessionLocal = sessionmaker(bind=engine)

base = DeclarativeBase()

session = SessionLocal()

class User(base):
    __tablename__ = "Users"
    id = Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    age: Mapped[int]
    strongest_learning_style: Mapped[Literal[
        "Visual", "Auditory", "Kinesthetic", "Reading/Writing", "Other"]] = mapped_column(
            Enum("Visual", "Auditory", "Kinesthetic", "Reading/Writing", "Other"), default="Other")
    info_learning_style: Mapped[str] = mapped_column(String(100))
    available_hours_per_day: Mapped[float]
    study_subjects: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)
    concentration_level: Mapped[Literal[
        "Low", "Moderate", "High"]] = mapped_column(
            Enum("Low", "Moderate", "High"), default="Moderate"
        )
    info_exam: Mapped[str] = mapped_column(String(100))

    __table_args__ = (
        CheckConstraint("age >= 10 AND age <= 100", name="chk_age_range"),
        CheckConstraint("available_hours_per_day >= 0 AND available_hours_per_day <= 24", name="chk_hours_range"),
        CheckConstraint("cardinality(study_subjects) <= 4", name="chk_subjects_max")
    )
