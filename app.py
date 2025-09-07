import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Liver Disease Prediction",
    page_icon="🩺",
    layout="centered"
)

custom_css = """
<style>
/* Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #e0f7fa, #fce4ec);
    color: #000000;  /* default text black */
    font-family: 'Segoe UI', sans-serif;
}

/* Header */
[data-testid="stHeader"] { background-color: transparent; }

/* Sidebar */
[data-testid="stSidebar"] { background: #222831; color: black; }

/* Title */
h1 { color: #00c4b4; text-align: center; font-weight: 800; }

/* Force ALL labels to black */
label, .stSelectbox label, .stNumberInput label, .stTextInput label,
.css-10trblm, .css-16idsys, .css-qrbaxs { color: black !important; font-weight: 600; }

/* Input fields */
.stNumberInput input, .stTextInput input, .stSelectbox div[data-baseweb="select"] {
    border-radius: 8px;
    color: white !important;              
    background-color: #333333 !important; 
    font-weight: 600;
}

/* +/- buttons in number input */
.stNumberInput button { background-color: #555555 !important; color: white !important; border-radius: 6px; border: none; }
.stNumberInput button:hover { background-color: #777777 !important; }

/* Dropdown menu options */
div[data-baseweb="popover"] { background-color: #333333 !important; color: white !important; }

/* Buttons */
div.stButton > button {
    background-color: #87CEEB; color: black !important;
    border-radius: 10px; padding: 0.6em 1.2em; font-size: 1.1em; font-weight: 600;
    border: none; transition: 0.3s;
}

</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
class SerializablePipeline:
    def __init__(self, preprocessor, model, label_encoder):
        self.preprocessor = preprocessor
        self.model = model
        self.label_encoder = label_encoder
    
    def predict(self, X):
        X_processed = self.preprocessor.transform(X)
        return self.model.predict(X_processed)
    
    def predict_proba(self, X):
        X_processed = self.preprocessor.transform(X)
        return self.model.predict_proba(X_processed)


model = joblib.load("liver_disease_model.pkl")

st.title("🩺 Liver Disease Prediction")
st.write("Fill the details below and click **Predict** to know if the patient is at risk.")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age of the patient", min_value=1, max_value=120, value=45)
    total_bilirubin = st.number_input("Total Bilirubin", min_value=0.0, value=1.2, step=0.1)
    direct_bilirubin = st.number_input("Direct Bilirubin", min_value=0.0, value=0.3, step=0.1)
    alkphos = st.number_input("Alkaline Phosphotase", min_value=10.0, value=187.0, step=1.0)
    sgpt = st.number_input("Alamine Aminotransferase (SGPT)", min_value=5.0, value=25.0, step=1.0)
with col2:
    gender = st.selectbox("Gender of the patient", ["Male", "Female"])
    sgot = st.number_input("Aspartate Aminotransferase (SGOT)", min_value=5.0, value=30.0, step=1.0)
    total_proteins = st.number_input("Total Proteins", min_value=1.0, value=6.8, step=0.1)
    albumin = st.number_input("Albumin", min_value=0.5, value=3.5, step=0.1)
    ag_ratio = st.number_input("A/G Ratio", min_value=0.1, value=1.1, step=0.1)

if st.button("Predict"):
    
    input_data = pd.DataFrame({
    'Age of the patient': [age],
    'Gender of the patient': [gender],
    'Total Bilirubin': [total_bilirubin],
    'Direct Bilirubin': [direct_bilirubin],
    '\xa0Alkphos Alkaline Phosphotase': [alkphos],
    '\xa0Sgpt Alamine Aminotransferase': [sgpt],
    'Sgot Aspartate Aminotransferase': [sgot],
    'Total Protiens': [total_proteins],
    '\xa0ALB Albumin': [albumin],
    'A/G Ratio Albumin and Globulin Ratio': [ag_ratio]
})


    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]

    if prediction[0] == 1:
        st.error(f"The patient is **likely to have Liver Disease**. Probability: {probability:.2%}")
    else:
        st.success(f"The patient is **not likely to have Liver Disease**. Probability: {1 - probability:.2%}")
