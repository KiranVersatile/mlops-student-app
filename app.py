# app.py

import streamlit as st
import requests
from auth import login

st.set_page_config(page_title="🎓 Student Score Predictor", layout="centered")

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("🔐 You must be logged in to access this page.")

   
    st.markdown("Please login or register to continue:")
    if st.button("🔐 Go to Login"):
        try:
            st.switch_page("auth.py")
        except Exception:
            st.warning("⚠️ Navigation only works in multipage apps.")
    st.stop()


st.title("🎓 MLOps Student App - API Integrated 🚀")
st.markdown("Enter the details below to predict your score:")


study_time = st.slider("📚 Study Time (hours)", 0, 10)
attendance = st.slider("✅ Attendance (%)", 50, 100)
gender = st.selectbox("👤 Gender", ["Male", "Female"])


if st.button("🎯 Predict via API"):
    with st.spinner("Contacting FastAPI..."):
        try:
           
            payload = {
                "study_time": study_time,
                "attendance": attendance,
                "gender": gender
            }

          
            api_url = "https://mlops-fastapi-api.onrender.com/predict"  # Change this if deploying

            
            response = requests.post(api_url, json=payload)

           
            if response.status_code == 200:
                result = response.json()
                st.success(
                    f"📊 Predicted Score: **{result['predicted_score']}**")
            else:
                st.error(
                    f"❌ API Error: {response.status_code} - {response.text}")

        except Exception as e:
            st.error(f"🚨 Something went wrong: {e}")
