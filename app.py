import streamlit as st
import pickle
import numpy as np

model=pickle.load(open('model.pkl' , 'rb'))
df=pickle.load(open('df.pkl' , 'rb'))
scaler=pickle.load(open('scaler.pkl' , 'rb'))

st.set_page_config("Crop Recommend")

st.title('Crop Recommended System')

Nitrogen = st.text_input("Nitrogen")
Phosphorus = st.text_input("Phosphorus")
Potassium  = st.text_input("Potassium")
Temperature = st.text_input("Temperature")
Humidity = st.text_input("Humidity")
pH_Value	=st.text_input("pH_Value	")
Rainfall = st.text_input("Rainfall")

input = []
input.append(Nitrogen)
input.append(Phosphorus)
input.append(Potassium)
input.append(Temperature)
input.append(Humidity)
input.append(pH_Value)
input.append(Rainfall)

submit=st.button('Show the Crop')
if submit:
    input = np.array(input).reshape(1, -1)
    input = scaler.transform(input)
    prediction = model.predict(input)
    st.write(df[df['crop_Encode']==prediction[0]].iloc[0].Crop)
