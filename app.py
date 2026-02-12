import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Loan Approval Predictor")

# -----------------------------
# Load trained model
# -----------------------------
model = joblib.load("model/final_model.pkl")

# -----------------------------
# User Inputs
# -----------------------------
st.subheader("Enter Applicant Details")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

applicant_income = st.number_input(
    "Applicant Income",
    min_value=0,
    step=1000
)

coapplicant_income = st.number_input(
    "Coapplicant Income",
    min_value=0,
    step=1000
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0,
    step=100
)

loan_term = st.number_input(
    "Loan Amount Term (in months)",
    min_value=0,
    step=12,
    value=360
)

credit_history = st.selectbox("Credit History", [1.0, 0.0])

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Loan Status"):
    input_df = pd.DataFrame([{
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Property_Area": property_area
    }])

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")