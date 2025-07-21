import time
from fastapi import HTTPException, status

# Config
RATE_LIMIT = 5  # Max 5 requests
TIME_WINDOW = 60  # Per 60 seconds

# In-memory store
rate_limits = {}

def rate_limiter(token: str):
    now = time.time()
    timestamps = rate_limits.get(token, [])

    # Keep only timestamps within the time window
    timestamps = [ts for ts in timestamps if now - ts < TIME_WINDOW]

    if len(timestamps) >= RATE_LIMIT:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded. Try again later."
        )

    # Update timestamps and save
    timestamps.append(now)
    rate_limits[token] = timestamps
