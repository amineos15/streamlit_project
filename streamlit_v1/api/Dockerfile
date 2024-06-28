# Utiliser une image de base officielle de Python
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers nécessaires dans le répertoire de travail
COPY src /app/src

COPY models /app/models

# Exposer le port sur lequel l'application va fonctionner
EXPOSE 9000

# Lancer l'application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "9000"]
