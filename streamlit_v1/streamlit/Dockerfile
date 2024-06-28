# Utiliser une image de base officielle de Python
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers nécessaires dans le répertoire de travail
COPY src /app/src

# Exposer le port sur lequel l'application va fonctionner
EXPOSE 8501

# Lancer l'application
CMD ["streamlit", "run", "src/main.py"]
