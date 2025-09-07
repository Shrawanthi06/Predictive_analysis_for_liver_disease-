pip install streamlit
import streamlit as st
import pandas as pd
import joblib
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
model= joblib.load("liver_disease_model.pkl")
st.set_page_config(page_title= "Liver Disease Prediction", layout= "centered")
st.title("Liver Disease Prediction App")
st.write("Enter patient details to check the prediction")
age= st.number_input("Age of the patient", min_value= 1, max_value= 120, value= 45 )
gender= st.selectbox("Gender of the patient", ["Male", "Female"])
total_bilirubin= st.number_input("Total Bilirubin", min_value= 0.0, value= 1.2, step= 0.1)
direct_bilirubin= st.number_input("Direct Bilirubin", min_value= 0.0, value= 0.3, step= 0.1)
alkphos = st.number_input("Alkaline Phosphotase", min_value=10.0, value=187.0, step=1.0)
sgpt = st.number_input("Alamine Aminotransferase (SGPT)", min_value=5.0, value=25.0, step=1.0)
sgot = st.number_input("Aspartate Aminotransferase (SGOT)", min_value=5.0, value=30.0, step=1.0)
total_proteins = st.number_input("Total Proteins", min_value=1.0, value=6.8, step=0.1)
albumin = st.number_input("Albumin", min_value=0.5, value=3.5, step=0.1)
ag_ratio = st.number_input("A/G Ratio", min_value=0.1, value=1.1, step=0.1)
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
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f" Prediction: Liver Disease (Probability: {probability:.2f})")
    else:
        st.success(f" Prediction: No Liver Disease (Probability: {probability:.2f})")
streamlit run app.py