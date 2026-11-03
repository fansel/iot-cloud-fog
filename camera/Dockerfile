FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir requests

COPY camera.py .

CMD ["python", "camera.py"]