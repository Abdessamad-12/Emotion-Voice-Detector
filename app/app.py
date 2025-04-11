import streamlit as st
from predict import predict_emotion

st.title("🎤 Détection d'Émotions Vocales")
uploaded_file = st.file_uploader("Téléverse un fichier audio (.wav)", type=["wav"])

if uploaded_file:
    with open("temp.wav", "wb") as f:
        f.write(uploaded_file.read())
    emotion = predict_emotion("temp.wav")
    st.success(f"Émotion détectée : {emotion}")
