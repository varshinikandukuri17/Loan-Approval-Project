import streamlit as st
import numpy as np
import joblib

model = joblib.load('loan_model.pkl')

st.title("🏦 Loan Approval Prediction App")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", [0, 1, 2, 3])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income")
coapplicant_income = st.number_input("Coapplicant Income")
loan_amount = st.number_input("Loan Amount")
loan_amount_term = st.number_input("Loan Amount Term (in days)")
credit_history = st.selectbox("Credit History", ["Good (1)", "Bad (0)"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

def predict():
    data = [
        1 if gender == "Male" else 0,
        1 if married == "Yes" else 0,
        dependents,
        1 if education == "Graduate" else 0,
        1 if self_employed == "Yes" else 0,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_amount_term,
        1 if credit_history == "Good (1)" else 0,
        0 if property_area == "Urban" else 1 if property_area == "Semiurban" else 2
    ]
    prediction = model.predict(np.array(data).reshape(1, -1))
    return "✅ Loan Approved" if prediction[0] == 1 else "❌ Loan Rejected"

if st.button("Predict"):
    st.success(predict())
