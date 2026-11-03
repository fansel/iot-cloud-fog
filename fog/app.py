from fastapi import FastAPI
import os

app = FastAPI()

FOG_ID = os.getenv("FOG_ID", "unknown")
ZONE = os.getenv("ZONE", "unknown")


@app.get("/health")
def health():
    return {
        "status": "running",
        "fog_id": FOG_ID,
        "zone": ZONE
    }