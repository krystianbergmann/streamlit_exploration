import streamlit as st

st.title("Twoje imię")

name = st.text_input("Jak masz na imię?")

if name:
    st.write(f"Cześć, {name}! 👋")