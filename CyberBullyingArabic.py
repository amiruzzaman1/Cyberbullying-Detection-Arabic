# app.py
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import joblib

# Load the SVM model and TF-IDF vectorizer
svm_model = joblib.load('svm_model.pkl')
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')

def preprocess_input(text):
    # Preprocess the input text (e.g., convert to lowercase, remove special characters, etc.)
    # Implement your specific preprocessing steps based on the training data
    processed_text = text.lower()
    # Add more preprocessing steps as needed
    
    return processed_text

def predict_bullying(text):
    # Preprocess input text
    processed_text = preprocess_input(text)
    
    # Convert text to numerical representation using TF-IDF
    text_tfidf = tfidf_vectorizer.transform([processed_text])
    
    # Make prediction using the SVM model
    prediction = svm_model.predict(text_tfidf)[0]
    
    return prediction

# Streamlit UI
def main():
    st.title("Cyberbullying Detection App (Arabic)")
    user_input = st.text_area("Enter a text for cyberbullying detection:")

    if st.button("Predict"):
        if user_input:
            prediction = predict_bullying(user_input)
            if prediction == "Bullying":
                st.write(f"<span style='color:red; font-weight:bold'>{prediction}</span>", unsafe_allow_html=True)
            else:
                st.write(f"<span style='color:cyan; font-weight:bold'>{prediction}</span>", unsafe_allow_html=True)
        else:
            st.warning("Please enter text for prediction.")

if __name__ == "__main__":
    main()
