import streamlit as st
import pandas as pd
import pydeck as pdk
import pickle
import numpy as np

def load_model_and_scaler():
    with open('model_airflow.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    return model, scaler

@st.cache
def load_data():
    df = pd.read_csv('test_read_csv.csv')
    df.dropna(subset=['latitude', 'longitude', 'velocity', 'altitude'], inplace=True)
    return df

def preprocess_data(df, scaler):
    features = ['latitude', 'longitude', 'velocity', 'altitude']
    df_scaled = scaler.transform(df[features])
    return df_scaled

def main():
    st.title("Flight Data Visualization with Anomalies and Normals")
    model, scaler = load_model_and_scaler()
    df = load_data()
    df_scaled = preprocess_data(df, scaler)
    
    df['predicted_on_ground'] = model.predict(df_scaled)
    
    altitude_filter = st.slider("Filter altitude", 0, 10000, 500)
    df = df[df['altitude'] <= altitude_filter]
    
    on_ground_df = df[df['predicted_on_ground'] == 1]
    not_on_ground_df = df[df['predicted_on_ground'] == 0]

    st.write("Data Points Count:", df.shape[0])
    st.write("On Ground Count:", on_ground_df.shape[0])
    st.write("Not On Ground Count:", not_on_ground_df.shape[0])

    layer_on_ground = pdk.Layer(
        'ScatterplotLayer',
        data=on_ground_df,
        get_position='[longitude, latitude]',
        get_color='[255, 0, 0, 160]',
        get_radius=10000,
        pickable=True
    )

    layer_not_on_ground = pdk.Layer(
        'ScatterplotLayer',
        data=not_on_ground_df,
        get_position='[longitude, latitude]',
        get_color='[0, 0, 255, 160]',
        get_radius=10000,
        pickable=True
    )

    view_state = pdk.ViewState(
        latitude=np.mean(df['latitude']),
        longitude=np.mean(df['longitude']),
        zoom=1,
        pitch=0,
    )

    st.pydeck_chart(pdk.Deck(
        layers=[layer_on_ground, layer_not_on_ground],
        initial_view_state=view_state,
        tooltip={"html": "<b>Speed:</b> {velocity} m/s<br /><b>Altitude:</b> {altitude} meters", "style": {"backgroundColor": "steelblue", "color": "white"}}
    ))

if __name__ == "__main__":
    main()
