FROM python:3.12-slim

WORKDIR /app

# 1) installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2) copier l'API + le modèle
COPY app ./app
COPY artifacts ./artifacts

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]