import json
import time

from fastapi import FastAPI, Request

app = FastAPI()

LOG_FILE = "/logs/ingest.log"


@app.get("/health")
def health():
    return {"status": "monitoring running"}


@app.post("/ingest")
async def ingest(request: Request):
    try:
        payload = await request.json()
    except Exception:
        payload = {"raw": (await request.body()).decode(errors="replace")}
    entry = {"ts": time.time(), "data": payload}
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
    return {"status": "ok"}
