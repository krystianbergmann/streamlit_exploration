import streamlit as st

st.title("Przenoszenie tekstu")

# Pole do wpisania tekstu
tekst = st.text_area("Wpisz tekst tutaj")

# Wyświetlenie tego samego tekstu w innym miejscu
st.subheader("Wyświetlony tekst")
st.write(tekst)