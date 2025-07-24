import streamlit as st
import pandas as pd
import os
from auth import login

st.set_page_config(page_title="📝 Register", layout="centered")
st.title("📝 User Registration")


username = st.text_input("Choose a Username")
password = st.text_input("Choose a Password", type="password")
role = st.selectbox("Select Role", ["student", "admin"])


if st.button("Register"):
    if username and password:
        file_path = "data/users.csv"
        os.makedirs("data", exist_ok=True)  # ensure 'data' folder exists

        user_data = {"username": username,
                     "password": password, "role": role}

        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            try:
                users = pd.read_csv(file_path)

                if username in users["username"].values:
                    st.error(" Username already exists. Please choose another.")
                else:
                    users = pd.concat(
                        [users, pd.DataFrame([user_data])], ignore_index=True)
                    users.to_csv(file_path, index=False)
                    st.success(" Registration successful! Please login now.")
            except Exception as e:
                st.error(f" Failed to read user file: {e}")

        else:

            users = pd.DataFrame([user_data])
            users.to_csv(file_path, index=False)
            st.success("✅ Registration successful! Please login now.")
    else:
        st.warning("⚠️ Please enter both username and password.")
