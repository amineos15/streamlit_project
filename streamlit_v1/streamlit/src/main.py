import requests
import pandas as pd
import streamlit as st


def predict(data):

    url = "http://api:9000/predict"
    try:
        response = requests.post(url, json=data)
        prediction = response.json().get("prediction")
        st.write(f"Prediction: {prediction}")
        return prediction
    except requests.exceptions.ConnectionError:
        st.error("Failed to connect to the prediction server. Please ensure the server is running.")
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        st.error(f"An error occurred: {err}")
    return None


latitude = st.number_input("latitude")
longitude = st.number_input("longitude")
velocity = st.number_input("velocity")
altitude = st.number_input("altitude")

data = {
    "latitude": latitude,
    "longitude": longitude,
    "velocity": velocity,
    "altitude": altitude
}

# Bouton de prédiction
button = st.button("Predict")

if button:
    st.write("Predicting...")
    prediction = predict(data)

    if prediction is None:
        st.write("Prediction failed")

    if "error" in prediction:
        st.write("Error during prediction")
    elif "prediction" in prediction:
        prediction = prediction["prediction"]
        st.write(f"Prediction: {prediction}")

