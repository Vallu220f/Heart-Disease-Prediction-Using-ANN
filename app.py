import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

st.title("❤️ Heart Disease Prediction")

st.write("Enter the patient's information below.")

age = st.number_input("Age", min_value=1, max_value=120, value=50)

sex = st.selectbox("Sex", [0, 1])

cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])

trestbps = st.number_input("Resting Blood Pressure", min_value=50, max_value=250, value=120)

chol = st.number_input("Cholesterol", min_value=50, max_value=600, value=200)

fbs = st.selectbox("Fasting Blood Sugar", [0, 1])

restecg = st.selectbox("Resting ECG", [0, 1, 2])

thalach = st.number_input("Maximum Heart Rate", min_value=50, max_value=250, value=150)

exang = st.selectbox("Exercise Induced Angina", [0, 1])

oldpeak = st.number_input("ST Depression", min_value=0.0, max_value=10.0, value=1.0)

slope = st.selectbox("Slope", [0, 1, 2])

ca = st.selectbox("Number of Major Vessels", [0, 1, 2, 3, 4])

thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

if st.button("Predict"):

    input_data = np.array([[
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")
        