import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
diabetes_model = pickle.load(open('D:/Desktop/DUCAT/multiple_disease_prediction/saved_model/Diabetes_model.sav', 'rb'))
Heartdisease_model = pickle.load(open('D:/Desktop/DUCAT/multiple_disease_prediction/saved_model/Heart_disease_model.sav', 'rb'))
Parkinson_model = pickle.load(open('D:/Desktop/DUCAT/multiple_disease_prediction/saved_model/Parkinson_disease_model.sav', 'rb'))

#sidebar for navigation
with st.sidebar:
    selected = option_menu("Multiple Diseases Prediction",
                           ['Diabetes Prediction',
                            "Heart Disease Prediction",
                            "Parkinson's Disease"],
                            icons=['prescription2', 'heart-pulse-fill', 'person-add'],
                            default_index=0)
    
#Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    #page tittle
    st.title('Diabetes Prediciton')

    # this is for the getting input data from the user
    #column for the input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of pregnancies')
    
    with col2:
        Glucose = st.text_input('Glucose level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin level')
    
    with col3:
        BMI = st.text_input('BMI value') 
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of person')


    #code for Prediction
    diab_diagnosis = ''

    #ceating a button for prediction
    if st.button('Diabetes Test Reuslts'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if diab_prediction[0] ==1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)

#Heart disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    #page tittle
    st.title('Heart Disease Prediciton')

    #columns for the input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age of the person')

    with col2:
        sex = st.text_input('Sex of the person (male or female)')

    with col3:
        cp = st.text_input('Chest Pain type')
    
    with col1:
        trestbps = st.text_input('Resting Blood Pressure value')
    
    with col2:
        chol = st.text_input('Serum Cholestoral value')
    
    with col3:
        fbs = st.text_input('Fasting Blood Sugar value')
    
    with col1:
        restecg = st.text_input('Resting Electrocardiogram Results')
    
    with col2:
        thalach = st.text_input('Maximum Heart Rate value')
    
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    
    with col1:
        oldpeak = st.text_input('ST Depression value')
    
    with col2:
        slope = st.text_input('ST Segment')
    
    with col3:
        ca = st.text_input('Number of Major Vessels colored by fluoroscopy')
    
    with col1:
        thal = st.text_input('Thalassemia')

    #code for prediction
    heart_diagnosis = ''
    
    #ceating a button for prediction
    if st.button('Heart Disease Test Reuslts'):
        heart_prediction = Heartdisease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if heart_prediction[0] ==1:
            heart_diagnosis = 'The person has heart disease'
        else:
            heart_diagnosis = 'The person does not have heart disease'
    st.success(heart_diagnosis)


#Parkinson Disease Prediction
if(selected == "Parkinson's Disease"):
    #page tittle
    st.title('Parkinson Disease Prediciton')

    #parkinson Disease Parameter
    #input fields for parkinson 
    #name,MDVP:Fo(Hz),MDVP:Fhi(Hz),MDVP:Flo(Hz),MDVP:Jitter(%),MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,Jitter:DDP,MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE
    col1, col2, col3 = st.columns(3)

    # with col1:
    #     name = st.text_input('Name of the person')
    
    with col1:
        mdvp_fo_hz = st.text_input('MDVP:Fo(Hz) value')

    with col2:
        mdvp_fhi_hz = st.text_input('MDVP:Fhi(Hz) value')

    with col3:
        mdvp_flo_hz = st.text_input('MDVP:Flo(Hz) value')
    
    with col1:
        mdvp_jitter_percent = st.text_input('MDVP:Jitter(%) value')

    with col2:
        mdvp_jitter_abs = st.text_input('MDVP:Jitter(Abs) value')
    
    with col3:
        mdvp_rap = st.text_input('MDVP:RAP value')
    
    with col1:
        mdvp_ppq = st.text_input('MDVP:PPQ value')
    
    with col2:
        jitter_ddp = st.text_input('Jitter:DDP value')

    with col3:
        mdvp_shimmer = st.text_input('MDVP:Shimmer value')
    
    with col1:
        mdvp_shimmer_dba = st.text_input('MDVP:Shimmer(dB) value')
    
    with col2:
        shimmer_apq3 = st.text_input('Shimmer:APQ3 value')
    
    with col3:
        shimmer_apq5 = st.text_input('Shimmer:APQ5 value')
    
    with col1:
        mdvp_apq = st.text_input('MDVP:APQ value')

    with col2:
        shimmer_dda = st.text_input('Shimmer:DDA value')

    with col3:
        nhr = st.text_input('NHR value')
    
    with col1:
        hnr = st.text_input('HFC value')
    
    with col2:
        rpde = st.text_input('RMSSD value')
    
    with col3:
        dfa = st.text_input("DFA value")
    
    with col1:
        spread1 = st.text_input('SD1 value')

    with col2:
        spread2 = st.text_input('SD2 value')

    with col3:
        d2 = st.text_input('Total Power value')

    with col1:
        PPE = st.text_input('Delta value')
    
    #code for prediction
    Parkinson_diagnosis = ""

    #ceating a button for prediction
    if st.button("Parkinson's Test Reuslts"):
        Parkinson_prediction = Parkinson_model.predict([[mdvp_fo_hz, mdvp_fhi_hz, mdvp_flo_hz, mdvp_jitter_percent, mdvp_jitter_abs, mdvp_rap, mdvp_ppq, jitter_ddp, mdvp_shimmer, mdvp_shimmer_dba, shimmer_apq3, shimmer_apq5, mdvp_apq, shimmer_dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, PPE]])
        if Parkinson_prediction[0] ==1:
            Parkinson_diagnosis = 'The person has heart disease'
        else:
            Parkinson_diagnosis = 'The person does not have heart disease'
    st.success(Parkinson_diagnosis)

    

