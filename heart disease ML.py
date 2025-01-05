# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 14:01:38 2024

@author: Sneha Umbrajkar
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#chatbot libraries
import nltk
import nltk.chat.util 
from nltk.chat import util
from chat_patterns import patterns


n=0  

#loading the saved models

heart_model = pickle.load(open('D:/Project/Heart disease_chatbot/saved_models/heart_model_save.sav','rb'))

#sidebar for modules

with st.sidebar:
    
    selected = option_menu('Heart Disease prediction System',
                           
                           
                          ['Predicting from your Symptoms',
                           'Chat for your Heart',
                           'About Us'],
                          
                          icons=['heart-pulse-fill','chat-left-heart','info-circle-fill'],  
                          default_index = 0,
                          menu_icon=['clipboard2-pulse-fill'],
                          )
    
    #pages
    
if (selected == 'Predicting from your Symptoms'):
    st.title('Heart disease prediction using ML')
    
    
    age=st.text_input('Age:-')
    sex=st.text_input('Gender:-')
    cp=st.text_input('Chest pain in range 1-3:-')    
    trestbps=st.text_input('Resting Blood Pressure in mmHg:-')
    chol =st.text_input('Serum Cholesterol:-')
    fbs=st.text_input('Fasting Blood sugar:-')
    restecg=st.text_input('Resting ECG result:-')
    thalach=st.text_input('Maximum heart rate achieved:-')
    exang=st.text_input('Exercise induced Angina:-')
    oldpeak=st.text_input('Oldpeak:-')
    slope=st.text_input('Slope:-')
    ca=st.text_input('ca:-')
    thal=st.text_input('thal:-')
    
    #prediction
    
    dignose = ''
    
    #creating a button
    
    if st.button('Test Result'):
       pred = heart_model.predict([[int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs), int(restecg), int(thalach), int(exang), float(oldpeak), int(slope),int(ca), int(thal)]])

    
        #final result
       if(pred[0]==1):
           dignose = 'The person has heart disease'
            
        
        
       else:
           dignose='The person does not have heart disease'
            
       
        
  
    st.success(dignose)
 
if (selected == 'Chat for your Heart'):
    st.title('Welcome to our chatbot!')
    st.title('Feel free to ask anything...')
    
    #patterns=[(r'what is heart disease/?',['Heart disease, also known as cardiovascular disease, refers to a class of diseases that involve the heart or blood vessels. It is a broad term that encompasses various conditions, and the most common type is coronary artery disease.']),(r'what are the symptoms of heart disease/?',['nausea or vomiting,chest pain,muscle discomfort,dullness'])]
    chatbot = util.Chat(patterns, util.reflections)
    
    
    
    user_question = st.text_input('Ask a question:', key='user_input')
    button_clicked = st.button('Get Answer')
    
    responses = st.session_state.get('responses', [])
    
    def process_input(user_input):
        if user_input.lower() == 'quit':
            return 'Thank you for using our chatbot!'
        elif user_input.strip() == '':
            return 'Please enter a valid question.'
        else:
            return chatbot.respond(user_input)
    
    if button_clicked:
        response = process_input(user_question)
        
        # Append the new response to the list
        responses.append({'question': user_question, 'response': response})
        
        # Save the list in session state
        st.session_state.responses = responses
        
        # Display all responses
        for entry in responses:
            st.write(entry['question'])
            st.write(entry['response'])
            

if (selected == 'About Us'):  
    st.title('About Us')
    st.write("""
    Welcome to our Heart Disease Prediction and Chatbot System!
    
    This project aims to provide a user-friendly interface for predicting heart disease based on symptoms and providing information related to heart health through a chatbot.
    
    Our team consists of passionate individuals dedicated to leveraging technology to improve healthcare accessibility and awareness.
    
    For any inquiries or feedback, please contact us at heartcare24@gmail.com.
    
    Thank you for using our system!
    """)

           
            
            
                
                
           
                
            
    
    
        
        
        
        
        
        
        
        