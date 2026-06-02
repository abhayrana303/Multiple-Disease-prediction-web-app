# Multiple Disease Prediction Web App

A machine learning-powered web application built with Streamlit that predicts the likelihood of multiple diseases including Diabetes, Heart Disease, and Parkinson's Disease based on user input.

## 📋 Overview

This application uses pre-trained machine learning models to provide predictions for three common diseases. Users can input various health parameters through an interactive web interface and receive instant predictions about their health status.

## 🎯 Features

- **Diabetes Prediction**: Predicts diabetes risk based on 8 health parameters
  - Number of pregnancies
  - Glucose level
  - Blood pressure
  - Skin thickness
  - Insulin level
  - BMI (Body Mass Index)
  - Diabetes pedigree function
  - Age

- **Heart Disease Prediction**: Predicts heart disease risk using 13 clinical parameters
  - Age, Sex, Chest Pain type
  - Resting blood pressure
  - Serum cholesterol
  - Fasting blood sugar
  - Resting electrocardiogram results
  - Maximum heart rate achieved
  - Exercise-induced angina
  - ST depression
  - ST segment slope
  - Number of major vessels
  - Thalassemia

- **Parkinson's Disease Prediction**: Detects Parkinson's disease based on voice/speech characteristics
  - MDVP frequency parameters
  - Jitter and shimmer measurements
  - Harmonic-to-noise ratio
  - Non-linear dynamical features (spread, DFA, etc.)
  - And more acoustic parameters

- **Intuitive Navigation**: Easy-to-use sidebar menu for switching between different disease predictions
- **Real-time Results**: Get instant predictions with clear diagnosis messages

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language
- **Streamlit**: Web framework for building interactive ML applications
- **scikit-learn**: Machine learning algorithms
- **NumPy & Pandas**: Data manipulation and analysis
- **Pickle**: Model serialization and loading

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/abhayrana303/Multiple-Disease-prediction-web-app.git
cd Multiple-Disease-prediction-web-app
