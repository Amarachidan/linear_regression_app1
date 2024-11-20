# power Output Prediction
Power Output Prediction using Sklearn, FastAPI and Streamlit App

## Table of contents
- [Discription](#description)
- [Requirement](#requirement)
- [Getting Started](#getting_startted)
   -[1. Train and save the model](#1-train-and-save-the-model)
   -[2. Deploy FastAPI](#2-deploy-fastapi)  
   -[3. Run streamlit](#3-streamlit)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Example Input and Output](#example-input-and-output)
- [File Structure](#file-structure)
- [License](#license)
## Discription
This project provides an API and a Streamlit application for predicting power output (PE) based on environmental factors. The model uses Linear Regression from Scikit-Learn, trained on features including:

Ambient Temperature (AT)
Exhaust Vacuum (V)
Ambient Pressure (AP)
Relative Humidity (RH)
The API is deployed using FastAPI, and a Streamlit app provides an interactive interface for users to input values and get predictions.