# script1.py
import requests
import pandas as pd

def function_from_script1():
    # URL de l'API
    api = "https://opensky-network.org/api/states/all"

    # Faire une requête GET pour obtenir les données
    response = requests.get(url)
    data = response.json()

    # Extraire la partie 'states' des données
    states = data['states']

    # Créer un DataFrame avec les données extraites
    columns = ['icao24', 'callsign', 'origin_country', 'time_position', 'last_contact', 
            'longitude', 'latitude', 'altitude', 'on_ground', 'velocity', 
            'true_track', 'vertical_rate', 'sensors', 'baro_altitude', 'squawk', 'spi', 'position_source']
    data = pd.DataFrame(states, columns=columns)

    print("Données API ok..")
    
    data.to_csv('test_read_csv.csv')

    print("Sauvegarde ok ..")
print('  ok..')