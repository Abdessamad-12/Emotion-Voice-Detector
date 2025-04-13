# Utilise une image Python officielle
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier tous les fichiers dans le conteneur
COPY . .

# Installer les dépendances
#RUN pip install --upgrade pip \
 #   && pip install -r requirements.txt

COPY wheels/ wheels/
RUN pip install --no-index --find-links=wheels -r requirements.txt


# Exposer le port utilisé par Streamlit
EXPOSE 8501

# Lancer l’application Streamlit
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
