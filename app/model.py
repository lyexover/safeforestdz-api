#model.py
import joblib
import os

def load_model():
    # Chemin relatif vers le modèle .pkl
    model_path = os.path.join(os.path.dirname(__file__), "../model/fire_prediction_model.pkl")
    return joblib.load(model_path)

def predict(features: dict):
    model = load_model()
    # Respecte l'ordre des features utilisé à l'entraînement
    input_features = [
        features["Temperature"],
        features["RH"],
        features["Ws"],
        features["Rain"]
    ]
    return model.predict([input_features])[0]  # Retourne la prédiction