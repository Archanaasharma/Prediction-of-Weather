import streamlit as st
import pandas as pd
import pickle

# load model
model = pickle.load(open("model.pkl","rb"))

st.title("Weather Prediction App 🌦️")

temp = st.slider("Temperature (C)", 0, 50)
humidity = st.slider("Humidity (0-1)", 0.0, 1.0)
wind = st.slider("Wind Speed (km/h)", 0, 100)
pressure = st.slider("Pressure (millibars)", 900, 1100)

# input in correct format
input_data = pd.DataFrame([[temp, humidity, wind, pressure]],
    columns=['Temperature (C)', 'Humidity', 'Wind Speed (km/h)', 'Pressure (millibars)']
)

# prediction
result = model.predict(input_data)

# show prediction value
st.write("Prediction Value:", result[0])

# readable output
if result[0] == 1:
    st.success("🌧️ Rain Expected")
else:
    st.success("☀️ No Rain Expected")