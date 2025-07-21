from fastapi import Header, HTTPException, status,Depends
from jose import JWTError,jwt
from datetime import datetime,timedelta
from typing import Optional
import os
from dotenv import load_dotenv
import json

load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

DUMMY_USER=json.loads(os.getenv("DUMMY_USER"))

def create_access_token(data:dict,expire_delta:Optional[timedelta]=None):
    to_encode=data.copy()
    expire=datetime.utcnow()+(expire_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

async def verify_token(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing or invalid token")
    
    token = authorization.split(" ")[1]
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username=payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401,detail="Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=401,detail="Invalid token")
    if token != API_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
