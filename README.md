# Weather Prediction 

## Overview

The **Weather Prediction App** is a Machine Learning project that predicts whether the weather condition will be **Rain** based on environmental factors such as temperature, humidity, wind speed, and atmospheric pressure.

This project uses the **Logistic Regression Algorithm** for prediction and **Streamlit** to create an interactive web application interface.

---

## Features

✅ Predict weather condition (Rain)

✅ Interactive Streamlit web interface

✅ Uses real weather parameters:
- Temperature (°C)
- Humidity
- Wind Speed (km/h)
- Pressure (millibars)

✅ Machine Learning model using Logistic Regression

✅ Model saving using Pickle (`model.pkl`)

✅ Performance evaluation using:
- Accuracy Score
- Confusion Matrix
- Classification Report

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

---

## Dataset Information

The dataset contains weather-related data including:


**Feature**     :  **Description**
 Temperature (C) : Temperature in Celsius 
 Humidity : Humidity level 
 Wind Speed (km/h) : Speed of wind 
 Pressure (millibars) : Atmospheric pressure 
 Precip Type : Rain or Not Rain


## Machine Learning Workflow

The following steps are performed in this project:

### 1. Data Collection
Dataset loaded using Pandas.

### 2. Data Preprocessing
- Convert precipitation type into numerical values
- Remove missing values using `dropna()`

### 3. Feature Selection

The following input features are used:

```python
[
'Temperature (C)',
'Humidity',
'Wind Speed (km/h)',
'Pressure (millibars)'
]
