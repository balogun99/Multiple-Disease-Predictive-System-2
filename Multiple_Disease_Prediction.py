#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:04:20 2025

@author: balogunishaq
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('/Users/balogunishaq/Desktop/Complete Machine Learning Course - Siddhardhan/Machine Learning/MLtuTs - Part 5 Model Deployment/Multiple Disease Prediction/saved_models/diabetes_trained_model.sav', 'rb'))

heart_disease_trained_model = pickle.load(open('/Users/balogunishaq/Desktop/Complete Machine Learning Course - Siddhardhan/Machine Learning/MLtuTs - Part 5 Model Deployment/Multiple Disease Prediction/saved_models/heart_disease_trained_model.sav', 'rb'))

parkinson_disease_trained_model = pickle.load(open('/Users/balogunishaq/Desktop/Complete Machine Learning Course - Siddhardhan/Machine Learning/MLtuTs - Part 5 Model Deployment/Multiple Disease Prediction/saved_models/parkinson_trained_model.sav', 'rb'))


# sidebar to navigate
with st.sidebar:
    
    selected = option_menu('Multiple Disease Predictive System',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinson Prediction'],
                           
                           icons = ['activity','heart','person'],
                           default_index = 0) # the choses the 1st index file to load on the sidebar
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # Page title
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user
    
    # columns from the user
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
        
    with col2:
        Glucose = st.text_input("Glucose Level")
        
    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")
        
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")
        
    with col2:
        Insulin = st.text_input("Insulin Level")
        
    with col3:
        BMI = st.text_input("BMI value")
        
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
        
    with col2:
        Age = st.text_input("Age of the person")
    
    # code for prediction
    
    diab_diagnosis = ''
    
    # creating button for prediction
    
    if st.button('Diabetes Test Result'):
        
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is Diabetic'
            
        else:
            diab_diagnosis = 'The person is not Diabetic'
            
            
    st.success(diab_diagnosis)
    
    
if (selected == 'Heart Disease Prediction'):
    
    # Page title
    st.title('Heart Disease Prediction using ML')
    
    # getting the input data from the user
    
    # columns from the user
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Age of the Person")
        
    with col2:
        sex = st.text_input("Gender of the Person")
        
    with col3:
        cp = st.text_input("Chest Pain Type")
        
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
        
    with col2:
        chol = st.text_input("Serum Cholesterol")
        
    with col3:
        fbs = st.text_input("Fasting Blood Sugar")
        
    with col1:
        restecg = st.text_input("Resting Cardiographic Result")
        
    with col2:
        thalach = st.text_input("Maximum Heart Rate Achieved")
        
    with col3:
        exang = st.text_input("Exercise Induced Vagina")
        
    with col1:
        oldpeak = st.text_input("Depression Induced by Exercise")
        
    with col2:
        slope = st.text_input("Slope of the Peak Exercise")
        
    with col3:
        ca = st.text_input("Colored Flouroscopy")
        
    with col1:
        thal = st.text_input("Normal")
    
    # code for prediction
    
    heart_diagnosis = ''
    
    # creating button for prediction
    
    # age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal	#oldpeak,
    
    if st.button('Heart Disease Test Result'):
        
        heart_prediction = heart_disease_trained_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if (heart_prediction[0] == 1):
            heart_diagnosis = 'This person is having heart disease'
        else:
            heart_diagnosis = 'This person does not have any heart disease' 
            
            
    st.success(heart_diagnosis)
    
if (selected == 'Parkinson Prediction'):
    
    # Page title
    st.title('Parkinson Disease Prediction using ML')
    
    # getting the input data from the user
    
    # columns from the user
    
    col1, col2, col3, col4, col5, = st.columns(5)
    
    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
        
    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
        
    with col3:
        flo = st.text_input("MDVP:Flo(Hz)y")
        
    with col4:

        Jitter_percent = st.text_input("MDVP:Jitter(%)")
        
    with col5:
        Jitter_Abs = st.text_input("SMDVP:Jitter(Abs)")
        
    with col1:
        RAP = st.text_input("MDVP:RAP")
        
    with col2:
        PPQ = st.text_input("MDVP:PPQ")
        
    with col3: 
        Jitter_DDP = st.text_input("itter:DDP")
        
    with col4:
        Shimmer = st.text_input("MDVP:Shimmer")
        
    with col5: 
        Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
        
    with col1:
        Shimmer_APQ3 = st.text_input("Shimmer:APQ3")
        
    with col2: 
        Shimmer_APQ5 = st.text_input("Shimmer:APQ5")
        
    with col3: 
        MDVP_APQ = st.text_input("MDVP:APQ")
        
    with col4: 
        Shimmer_DDA = st.text_input("Shimmer:DDA")
        
    with col5: 
        NHR = st.text_input("NHR")
        
    with col1: 
        HNR = st.text_input("HNR")
        
    with col2:
        RPDE = st.text_input("RPDE")
        
    with col3:
        DFA = st.text_input("DFA")
        
    with col4: 
        spread1 = st.text_input("spread1")
        
    with col5: 
        spread2 = st.text_input("spread2")
        
    with col1: 
        D2 = st.text_input("D2")
        
    with col2: 
        PPE = st.text_input("PPE")
    
    # code for prediction
    
    parkinson_diagnosis = ''
    
    # creating button for prediction
    
    
    if st.button('Parkinson Disease Test Result'):
        
        parkinson_prediction = parkinson_disease_trained_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, Jitter_DDP, Shimmer, Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        
        if (parkinson_prediction[0] == 1):
            parkinson_diagnosis = 'This person has Parkinson Disease'
        else:
            parkinson_diagnosis = 'This person does not have Parkinson Disease' 
            
            
    st.success(parkinson_diagnosis)