FROM python

WORKDIR /app

COPY requirements.txt ./
COPY main.py ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "172.17.0.7", "--port", "8000"]