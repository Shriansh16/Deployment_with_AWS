import streamlit as st
import requests
from scripts import s3

# Define the API endpoint
API_URL = "http://127.0.0.1:8502/api/v1/"
headers = {
  'Content-Type': 'application/json'
}

st.title("ML Model Serving Over REST API")

model = st.selectbox("Select Model",
                     ["Sentiment Classifier", 
                      "Disaster Classifier", "Pose Classifier"])

if model=="Sentiment Classifier":
    text = st.text_area("Enter Your Movie Review")
    user_id = st.text_input("Enter user id", "udemy@kgptalkie.com")

    data = {"text": [text], "user_id": user_id}
    model_api = "sentiment_analysis"

if st.button("Predict"):
    with st.spinner("Predicting... Please wait!!!"):
        response = requests.post(API_URL+model_api, headers=headers,
                                 json=data)
        
        output = response.json()

    st.write(output)