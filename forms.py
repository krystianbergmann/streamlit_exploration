import streamlit as st

st.title("Formularz użytkownika")

with st.form("user_form"):
    name = st.text_input("Imię")
    age = st.number_input("Wiek", min_value=0, max_value=120)
    submitted = st.form_submit_button("Wyślij")

if submitted:
    st.success(f"Cześć {name}, masz {age} lat 🎉")