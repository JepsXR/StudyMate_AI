# StudyMate_AI 📚🤖

**StudyMate_AI** is a backend AI agent designed to help users generate effective, personalized study methods tailored to their specific learning styles and academic context. 

Currently in active development, the project features a robust data architecture using **Pydantic** and **SQLAlchemy**, containerization via **Docker**, a persistent **PostgreSQL** database, asynchronous API execution with **FastAPI**, and secure configuration management using environment variables.

---

## 📌 Features & Architecture

* **Asynchronous RESTful API:** High-performance backend built with FastAPI and Uvicorn.
* **Data Validation & Persistence:** Data schemas defined with Pydantic v2 and mapped through SQLAlchemy ORM.
* **Production-Ready Database:** PostgreSQL integration managed via the `psycopg` driver.
* **Containerized Environment:** Fully isolated multi-container setup running Python and PostgreSQL via Docker Compose.
* **Secure Credentials:** Environment isolation and secrets management via `python-dotenv`.

---

## 🗺️ Roadmap

* **Google Gemini AI Integration:** Intelligent analysis of learning habits to generate tailored study strategies and recommendations.
* **Notion API Integration:** Automatic creation and organization of study blocks, task lists, and status updates directly in Notion workspaces (`notion-client`).
* **Google Calendar API Integration:** Automated scheduling for exams, assignment deadlines, and review sessions using OAuth2 authentication.

---

## 🛠️ Tech Stack

| Component | Technology | Version |
| :--- | :--- | :--- |
| **Framework** | FastAPI | `0.141.1` |
| **ASGI Server** | Uvicorn | `0.53.0` |
| **ORM** | SQLAlchemy | `2.0.54` |
| **Database Driver** | psycopg (PostgreSQL) | `3.3.6` |
| **Data Validation** | Pydantic | `2.13.5` |
| **Integrations** | Google Generative AI | `0.8.6` |
| | Notion Client | `3.1.0` |
| **Environment Vars** | python-dotenv | `1.2.3` |
| **Containerization** | Docker / Docker Compose | Latest |

---

## ⚙️ Local Setup & Installation

### Option 1: Running with Docker (Recommended)

Since PostgreSQL is configured within the containerized setup, Docker Compose manages both the application and the database.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/JepsXR/StudyMate_AI.git](https://github.com/JepsXR/StudyMate_AI.git)
   cd StudyMate_AI
