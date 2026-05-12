import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

data= pd.read_csv("C:/Users/ankit/OneDrive/Documents/Downloads/archive (1).zip")
print (data.head())
print(data.columns.tolist())

data['Rain'] = data['Precip Type'].str.lower().map({'rain': 1, 'snow': 0})
print(data['Rain'].value_counts())
data = data.dropna()

x= data[['Temperature (C)', 'Humidity', 'Wind Speed (km/h)', 'Pressure (millibars)']]
y = data['Rain']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
print("Accuracy:", accuracy_score(y_test,y_pred))
#check confusion matrix
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))
#use better metrics
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))


import streamlit as st
import numpy as np

st.title("Weather Prediction App 🌦️")

temp = st.slider("Temperature (C)", 0, 50)
humidity = st.slider("Humidity (0-1)", 0.0, 1.0)
wind = st.slider("Wind Speed (km/h)", 0, 100)
pressure = st.slider("Pressure (millibars)", 900, 1100)

pickle.dump(model,open("model.pkl","wb"))
print("model saved succesfully")