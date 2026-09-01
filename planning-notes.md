# This a short description about the AI StudyMate

This is a AI Agent that can give you a hyper-personalizated advice according with your study rythnm. The architecture of this backend consists in a AI that can receive a data of your study context, for example, your age, learning style, available study hours per day. ETC. We going to do this with Pydactic (specially BaseModel and Field for polish the data architecture and avoid that user writes No-Valid text) and we going to save this user data in PostgreSQL. 

Talking about the Frameworks, we going to use a FastAPI, 'cause is very useful for test the backend without Frontend, and has a great tools, for example HTTPException, that is excellent managing system errors. ETC. 

We going to use a many APIs, for example the AI Gemini for generate prompts and save resources, Notion