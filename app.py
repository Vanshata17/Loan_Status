import streamlit as st
import pandas as pd
import joblib

st.title("Loan Approval Predictor")

# Load model
model = joblib.load("model/final_model.pkl")

# Input form
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income")
coapplicant_income = st.number_input("Coapplicant Income")
loan_amount = st.number_input("Loan Amount")
loan_term = st.number_input("Loan Amount Term")
credit_history = st.selectbox("Credit History", [1.0, 0.0])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Predict
if st.button("Predict"):
    input_df = pd.DataFrame({...})  # construct input row
    prediction = model.predict(input_df)
    st.success("Loan Approved" if prediction[0] == 1 else "Loan Rejected")