# Predictive_analysis_for_liver_disease

Liver disease cases are continuously increasing due to:
🍺 Excessive alcohol consumption
😷 Inhalation of harmful gases
🍲 Contaminated food/pickles
💊 Prolonged drug usage

To support doctors with early diagnosis, I worked with a liver disease dataset (collected from North East Andhra Pradesh, India 🇮🇳) consisting of 583 patient records (416 positive, 167 negative).

⚖️ The dataset is imbalanced (~2.5:1), requiring proper handling during ML model training.

📑 Dataset Features include age, gender, bilirubin levels, enzyme counts (SGPT, SGOT, Alkaline Phosphatase), protein levels, albumin, and A/G ratio.

# Liver Disease Prediction – Phase 1

This repository contains the **Phase 1** work of my Liver Disease Prediction project, focusing on **data acquisition, preprocessing, and feature engineering**.

## 📌 Project Overview

The aim of this project is to build a predictive model for liver disease using patient health data. In **Phase 1**, the goal was to understand the dataset, perform initial cleaning, and prepare it for model training in the upcoming phases.

## 📂 Files in this Phase

* **`Liver Patient Dataset (LPD)_train.csv`** → Raw dataset containing patient records.
* **`cleaned_liver_data.csv`** → Preprocessed dataset with cleaned values, encoded features, and improved formatting.

## 🔍 Phase 1 Steps Completed

1. **Data Loading & Inspection**

   * Checked file structure, dimensions, and column descriptions.
   * Identified missing values and anomalies.

2. **Exploratory Data Analysis (EDA)**

   * Statistical summary of each feature.
   * Visualized distributions, correlations, and outliers.
   * Observed class distribution for imbalance detection.

3. **Data Cleaning**

   * Handled missing values and duplicates.
   * Standardized column names and data formats.
   * Converted categorical variables into numerical codes.

4. **Feature Engineering**

   * Created new derived features for better model representation.
   * Encoded categorical data using label encoding.
   * Scaled numerical features where required.

## 📊 Key Observations from Phase 1

* **Class imbalance**: Positive cases are significantly fewer than negative ones, requiring handling in later phases.
* **Correlation insights**: Certain features like bilirubin levels and liver enzyme counts show strong correlation with the target.
* **Outliers**: Some lab values fall far outside typical human ranges and will need careful treatment.

## 🚀 Next Steps (Phase 2)

* Implement machine learning models (XGBoost, Random Forest, etc.).
* Perform hyperparameter tuning.
* Evaluate with metrics like ROC-AUC, Precision, Recall, and F1-score.
* Consider class imbalance handling via SMOTE, class weights, or oversampling.

---

🚀 Phase 2 Work: Model Training & Deployment

✅ Trained and compared multiple ML models: Logistic Regression, Random Forest, and XGBoost.
🏆 Best model: XGBoost with:

Accuracy: 82.24%

F1-Score: 0.8298

ROC-AUC: 0.9406

✅ Saved the model and deployed it with Streamlit as an interactive web app.

🖥️ Liver Disease Prediction App allows users to input patient details (age, enzyme levels, proteins, etc.) and instantly get a prediction with probability scores.


