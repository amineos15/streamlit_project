# script2.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
import pickle

def function_from_script2():
    df = pd.read_csv('test_read_csv.csv')

    # Nettoyage des données
    df.dropna(subset=['latitude', 'longitude', 'velocity', 'altitude'], inplace=True)

    # Sélection des caractéristiques et de la cible
    X = df[['latitude', 'longitude', 'velocity', 'altitude']]
    y = df['on_ground'].astype(int)

    # Diviser les données
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Normaliser les caractéristiques
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Entraîner le modèle
    model = LogisticRegression()
    model.fit(X_train_scaled, y_train)

    # Prédire et évaluer
    y_pred = model.predict(X_test_scaled)
    print("Accuracy:", accuracy_score(y_test, y_pred))



    with open('model_airflow.pkl', 'wb') as file:
        pickle.dump(model, file)
