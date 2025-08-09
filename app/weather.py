import requests
import os
from fastapi import HTTPException
from dotenv import load_dotenv  # Nouvel import nécessaire

# Charge les variables d'environnement du fichier .env
load_dotenv()

def get_weather_data(city: str):
    # Récupération sécurisée de la clé API
    api_key = os.getenv("WEATHER_API_KEY")
    
    # 2. Utiliser votre vraie clé dans l'URL
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lève une exception si erreur HTTP
        data = response.json()
        
        # 3. Vérifier que la réponse contient les données attendues
        if "current" not in data:
            print(f"Réponse API: {data}")  # Pour debug
            raise HTTPException(
                status_code=400, 
                detail=f"Impossible d'obtenir les données météo pour {city}. Vérifiez le nom de la ville."
            )
        
        return {
            "Temperature": data["current"]["temp_c"],
            "RH": data["current"]["humidity"],
            "Ws": data["current"]["wind_kph"],
            "Rain": data["current"]["precip_mm"],
            "raw_data": data
        }
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erreur de connexion à l'API météo: {str(e)}")
    except KeyError as e:
        print(f"Données reçues: {data}")  # Pour debug
        raise HTTPException(status_code=500, detail=f"Données météo manquantes: {str(e)}")