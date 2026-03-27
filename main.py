import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import redis.asyncio as redis

app = FastAPI()
# --- ADD THIS CORS BLOCK ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all websites to hit your API (good for testing)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ---------------------------

# Paste your EXTERNAL URL in the quotes on the right.
# This says: "Use the environment variable if it exists. If not, use my external URL."
REDIS_URL = os.getenv("REDIS_URL", "rediss://red-YOUR_EXTERNAL_URL_HERE:6379")

redis_client = redis.from_url(REDIS_URL, decode_responses=True)

@app.get("/counter")
async def countt():
    new_count = await redis_client.incr("mentalan-counter")
    return {"count": new_count}

@app.get("/bonks")
async def bonks():
    new_count = await redis_client.get("mentalan-counter")
    return {"count": new_count}
