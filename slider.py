import streamlit as st

st.title("Suwak")

age = st.slider("Ile masz lat?", 0, 100, 25)
st.write(f"Masz {age} lat")