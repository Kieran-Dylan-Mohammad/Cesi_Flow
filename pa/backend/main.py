from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from moodle_automation import MoodleAutomation
from typing import Dict

# Création de l'application FastAPI
app = FastAPI()

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginData(BaseModel):
    username: str
    password: str

@app.get("/")
async def root():
    return {"message": "API Moodle Automation"}

@app.post("/api/login")
async def login(data: LoginData):
    try:
        automation = MoodleAutomation()
        success = automation.connexion_moodle(data.username, data.password)
        
        if success:
            return {
                "success": True,
                "message": "Connexion réussie",
                "user": {
                    "username": data.username
                }
            }
        else:
            return {
                "success": False,
                "message": "Échec de la connexion"
            }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Point d'entrée principal
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    