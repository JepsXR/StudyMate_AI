# IMPORTS

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from dotenv import load_dotenv
import json
import os
import google.generativeai as genai
import psycopg
