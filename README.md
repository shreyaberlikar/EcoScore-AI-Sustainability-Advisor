# EcoScore AI – AI-Powered Sustainability Assessment System

> An end-to-end Machine Learning application that predicts a product's lifecycle carbon footprint and generates an EcoScore to support sustainable product evaluation and environmental decision-making.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20Application-red)
![License](https://img.shields.io/badge/License-Educational-green)

---

# Table of Contents

- Overview
- Problem Statement
- Objectives
- Solution
- Key Features
- System Architecture
- Machine Learning Workflow
- Technology Stack
- Project Structure
- Model Performance
- Installation
- Applications
- Future Enhancements
- Author
- License

---

# Overview

EcoScore AI is a Machine Learning-based sustainability assessment platform that estimates a product's environmental impact throughout its lifecycle.

The system predicts:

- Lifecycle Carbon Footprint (kg CO₂e)
- EcoScore (0–100 Sustainability Score)

The application enables users to analyze sustainability metrics, compare products, and make environmentally responsible decisions through an interactive web interface.

---

# Problem Statement

Assessing the environmental impact of a product requires detailed lifecycle analysis, which is often expensive, time-consuming, and requires domain expertise.

Organizations need an intelligent solution capable of:

- Estimating lifecycle carbon emissions
- Evaluating sustainability performance
- Supporting environmentally responsible product design
- Providing data-driven sustainability insights

---

# Objectives

- Predict lifecycle carbon footprint using Machine Learning.
- Generate an EcoScore representing overall sustainability.
- Provide interactive analytics for sustainability evaluation.
- Enable comparative analysis between products.
- Promote environmentally conscious decision-making.

---

# Proposed Solution

EcoScore AI automates sustainability assessment using a supervised Machine Learning model.

The system processes product lifecycle parameters, performs feature engineering and preprocessing, predicts lifecycle carbon emissions, and generates an EcoScore representing the environmental performance of a product.

---

# Key Features

## Sustainability Assessment

- Lifecycle carbon footprint prediction
- EcoScore generation
- Environmental impact analysis

## Machine Learning

- Data preprocessing
- Feature engineering
- Feature scaling
- Gradient Boosting Regression
- Model serialization using Joblib

## Interactive Dashboard

- Carbon footprint visualization
- Sustainability comparison
- Performance analytics
- Interactive charts

## Comparative Analysis

- Compare multiple products
- Sustainability benchmarking
- Carbon emission trends

---

# System Architecture

```text
               User Input
                    │
                    ▼
          Data Validation
                    │
                    ▼
        Feature Engineering
                    │
                    ▼
         Feature Scaling
                    │
                    ▼
     Gradient Boosting Model
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
Carbon Footprint         EcoScore Generation
        │                       │
        └───────────┬───────────┘
                    ▼
          Streamlit Dashboard
```

---

# Machine Learning Workflow

```text
Dataset Collection
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Feature Scaling
        │
        ▼
Train-Test Split
        │
        ▼
Gradient Boosting Regression
        │
        ▼
Hyperparameter Tuning
        │
        ▼
Model Evaluation
        │
        ▼
Model Deployment
```

---

# Input Features

The prediction model considers multiple sustainability indicators, including:

- Raw Material Energy
- Manufacturing Energy
- Water Consumption
- Transportation Distance
- Transportation Mode
- Logistics Energy
- Product Weight
- Recyclability Score
- Grid Carbon Intensity
- Disposal Emissions
- Manufacturing Efficiency
- Material Type

---

# Outputs

The application generates:

- Lifecycle Carbon Footprint Prediction
- EcoScore (0–100)
- Sustainability Assessment
- Comparative Product Analysis

---

# Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Framework | Streamlit |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib |
| Model Persistence | Joblib |
| Version Control | Git, GitHub |

---

# Model Performance

| Metric | Value |
|---------|-------|
| Learning Type | Supervised Learning |
| Algorithm | Gradient Boosting Regression |
| Feature Scaling | StandardScaler |
| Hyperparameter Optimization | GridSearchCV |
| Model Serialization | Joblib |

> Add your actual evaluation metrics such as R² Score, RMSE, MAE, and MSE if available.

---

# Project Structure

```text
EcoScore-AI-Sustainability-Advisor/
│
├── app.py
├── dataset/
│   └── product_lifecycle_carbon_dataset.csv
├── models/
│   ├── ecoscore_model.pkl
│   ├── scaler.pkl
│   ├── model_features.pkl
│   └── eco_range.pkl
├── images/
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/shreyaberlikar/EcoScore-AI-Sustainability-Advisor.git
```

Navigate to the project

```bash
cd EcoScore-AI-Sustainability-Advisor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# Applications

- Sustainable Product Assessment
- Carbon Footprint Estimation
- ESG Reporting
- Green Manufacturing
- Environmental Research
- Sustainability Analytics

---

# Future Enhancements

- Cloud deployment
- REST API integration
- Explainable AI (SHAP/LIME)
- Product barcode scanning
- Recommendation system for sustainable alternatives
- Integration with real-time environmental datasets

---

# Author

**Shreya Berlikar**

Computer Engineering Student | AI & Machine Learning Enthusiast

**GitHub:** https://github.com/shreyaberlikar

**LinkedIn:** https://linkedin.com/in/shreya-berlikar

---

# License

This project is developed for educational and research purposes.
