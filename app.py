# importing Important Liberaries
import pickle
import streamlit as st
import numpy as np

# Load model
model_diabetes = pickle.load(open('linear_model.pkl', 'rb'))

# Web Title
st.title('Diabetes Prediction')

# Split Columns
col1, col2 = st.columns(2)

with col1 :
  Pregnancies = st.number_input('Enter the Pregnancies value (0-17)')

with col2 :
  Glucose = st.number_input('Enter the Glucose value (44-199)')
  
with col1 :
  BloodPressure = st.number_input('Enter the Blood Pressure value(24-122)')

with col2 :
  SkinThickness = st.number_input('Enter the Skin Thickness value(7-99)')

with col1 :
  Insulin = st.number_input('Enter the Insulin value(14-846)')

with col2 :
  BMI = st.number_input('Enter the BMI value (18-67)')

with col1 :
  DiabetesPedigreeFunction = st.number_input('Enter the Diabetes Pedigree Function value (0.078-2.42)')

with col2 :
  Age = st.number_input('Enter the Age value(21-81)')
  
# Prediction
diabetes_diagnosis = ''

if st.button('Diabetes Prediction Test'):
  diabetes_prediction = model_diabetes.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
  
  if(diabetes_prediction[0]==1):
    diabetes_diagnosis = 'The patient is probably diabetic.'
  else :
    diabetes_diagnosis = 'The patient is probably not diabetic.'

st.success(diabetes_diagnosis)

