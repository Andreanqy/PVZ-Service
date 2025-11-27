from fastapi import FastAPI, HTTPException
from datetime import datetime, timezone, timedelta
from models import *
import jwt

app = FastAPI(title="PVZ Service")

# Потом перенести в .env
JWT_SECRET = "34ebdcc9b666c69ec6013fa9d7eaec0d"
ALGORITHM = "HS256"


@app.post("/dummyLogin")
async def postDummyLogin(role: Role):
    payload = {
        "role": role.value,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=15)
    }
    return Token(jwt.encode(payload, JWT_SECRET, ALGORITHM))