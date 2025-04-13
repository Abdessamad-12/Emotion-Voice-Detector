import librosa
import numpy as np
from keras.models import load_model
import os

# Dynamically get the base directory (project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Join it with the model path
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.h5")

# Load model
model = load_model(MODEL_PATH)

#model = load_model("../model/model.h5")
emotion_dict = {0: "angry", 1: "disgust", 2: "fear", 3: "happy", 4:"neutral", 5:"ps", 6:"sad"}


def predict_emotion(file_path):
    audio, sample_rate = librosa.load(file_path, duration=3, offset=0.5)
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs = mfccs.reshape(1, -1, 1)
    prediction = model.predict(mfccs)
    predicted_class = np.argmax(prediction)
    return emotion_dict[predicted_class]
#print(predict_emotion("../data/YAF_happy/YAF_base_happy.wav"))