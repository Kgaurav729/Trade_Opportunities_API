from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils.auth import DUMMY_USER, create_access_token

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(request: LoginRequest):
    if request.username != DUMMY_USER["username"] or request.password != DUMMY_USER["password"]:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    token = create_access_token({"sub": request.username})
    return {"access_token": token, "token_type": "bearer"}
