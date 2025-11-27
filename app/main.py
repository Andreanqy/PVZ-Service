from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from datetime import datetime, timezone, timedelta
from .request_response_models import *
from .models import *
import jwt

app = FastAPI(title="PVZ Service")

# Потом перенести в .env
JWT_SECRET = "34ebdcc9b666c69ec6013fa9d7eaec0d"
ALGORITHM = "HS256"

@app.post("/dummyLogin")
async def postDummyLogin(request: Request):
    try:
        body = await request.json()
        request_role = body.get("role")
        role = Role(request_role)
        payload = {
            "role": role.value,
            "exp": datetime.now(timezone.utc) + timedelta(minutes=15)
        }
        return Token(jwt.encode(payload, JWT_SECRET, ALGORITHM))
    except Exception as e:
        return JSONResponse(status_code=400, content=Error(message=str(e)).model_dump())