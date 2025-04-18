import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# UI
st.set_page_config(page_title="Spam Detector", page_icon="📧")
st.title("📧 Email Spam Detector")
st.write("Paste the email text below and find out if it's spam!")

email_text = st.text_area("Email Content", height=200)

if st.button("Check for Spam"):
    if email_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        vectorized = vectorizer.transform([email_text])
        prediction = model.predict(vectorized)[0]
        result = "🚨 Spam!" if prediction == 1 else "✅ Not Spam"
        st.subheader(result)
