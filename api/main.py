import sys
import os

# Permet d'importer app/ même s'il est en dehors du dossier actuel
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from app.predict import predict_emotion
import shutil





app = FastAPI()

UPLOAD_DIR = "app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    emotion = predict_emotion(file_location)

    # Supprimer le fichier après traitement
    os.remove(file_location)

    return JSONResponse(content={"emotion": emotion})

