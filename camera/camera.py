import os
import time
import requests

CAMERA_ID = os.getenv("CAMERA_ID")
FOG_URL = os.getenv("FOG_URL")

while True:
    try:
        response = requests.get(f"{FOG_URL}/health", timeout=5)

        print(
            f"{CAMERA_ID} -> "
            f"Fog response: {response.json()}"
        )

    except Exception as e:
        print(f"{CAMERA_ID}: Error: {e}")

    time.sleep(10)