# Imports

import os
from dotenv import load_dotenv

load_dotenv()

# VERIFICATION API KEYS

STUDYMATE_API_KEY = os.getenv("STUDYMATE_API_KEY")

if not STUDYMATE_API_KEY:
    raise("ERROR: API KEY NOT FOUNDED")
