\# Churn Prediction API (Docker)



API FastAPI pour prédire le churn client (Telco) à partir d'un modèle scikit-learn sauvegardé.



\## Lancer en local (Docker)

```bash

docker build -t churn-api:1.0 .

docker run --rm -p 8000:8000 churn-api:1.0

