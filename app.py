import streamlit as st
import joblib

model = load('Sentiment-Analysis.joblib')

st.title('Sentiment Analysis')
text = st.text_input('Enter the message')

predict = float(model.predict([text])) 

category = 'Normal Category'

if predict == 1.0:
   category = 'Positive Category'
elif predict == -1.0:
   category = 'Negative Category'

st.write(category)
