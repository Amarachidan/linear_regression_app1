import streamlit as st
import requests
import joblib
import numpy as np

# load model
model = joblib.load("model/model.pkl")
# app title and descripton
st. title("Power Output Prediction")
st.write("Enter the values for the following features to predict power output (PE).")

# User input for each features
ambient_temperature = st.number_input("Ambient Temperature (AT)", value=15.0)
exhaust_vacuum = st.number_input("Exhaust Vacuum (V)", value=40.0)
ambient_pressure = st.number_input("Ambient Pressure (AP)", value=1000)
relative_humidity = st.number_input("Relative Humidity (RH)", value=75)

if st.button("Predict"):
    input_data = np.array([[
        ambient_temperature, exhaust_vacuum, ambient_pressure, relative_humidity
    ]])
    prediction = model.predict(input_data)
    st.write(f"Predicted Power Output (PE): {prediction[0]}")

    # prepare data
    # input_data = {
    #     "ambient_temperature": ambient_temperature,
    #     "exhaust_vacuum": exhaust_vacuum,
    #     "ambient_pressure": ambient_pressure,
    #     "relative_humidity": relative_humidity
    # }
    #
    # # make api call
    # response = requests.post("http://0.0.0.0:8000/predict", json=input_data)
    #
    # if response.status_code == 200:
    #     prediction = response.json()["prediction"]
    #     st.write(f"Predicted Power Output (PE): {prediction}")
    # else:
    #     st.write("Error in prediction. Please try again.")

