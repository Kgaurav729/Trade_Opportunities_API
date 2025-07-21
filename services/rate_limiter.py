import time
from fastapi import HTTPException, status
import os
from dotenv import load_dotenv

load_dotenv()

# Config
RATE_LIMIT = int(os.getenv("RATE_LIMIT"))
TIME_WINDOW = int(os.getenv("TIME_WINDOW"))


rate_limits = {}

def rate_limiter(token: str):
    now = time.time()
    timestamps = rate_limits.get(token, [])

    timestamps = [ts for ts in timestamps if now - ts < TIME_WINDOW]

    if len(timestamps) >= RATE_LIMIT:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded. Try again later."
        )

    timestamps.append(now)
    rate_limits[token] = timestamps
