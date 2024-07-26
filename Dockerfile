FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
COPY app/ ./app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "127.0.0.7", "--port", "8000"]