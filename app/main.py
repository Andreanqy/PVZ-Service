from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime, timezone, timedelta
import jwt
from models import *

app = FastAPI(title="PVZ Service")

# Потом перенести в .env
JWT_SECRET = "34ebdcc9b666c69ec6013fa9d7eaec0d"
ALGORITHM = "HS256"


@app.post("/dummyLogin",
          responses={
              200: {"model": Token},
              400: {"model": Error}
          })
async def post_dummy_login(request: PostDummyLoginModel):
    try:
        #body = await request.json()
        #request_role = body.get("role")
        request_role = request.role
        role = Role(request_role)
        payload = {
            "role": role.value,
            "exp": datetime.now(timezone.utc) + timedelta(minutes=15)
        }
        return Token(jwt.encode(payload, JWT_SECRET, ALGORITHM))
    except Exception as e:
        return JSONResponse(status_code=400, content=Error(message=str(e)).model_dump())


@app.post("/register",
          responses = {
              201: {"model": User},
              400: {"model": Error}
          }, status_code = 201)
async def register_user(request: RegisterUserModel):
    try:
        request_email, request_password, request_role = request.email, request.password, request.role
        new_user = User(email=request_email)
        # TODO: Добавить пользователя в БД
    except Exception as e:
        return JSONResponse(status_code=400, content=Error(message=str(e)).model_dump())