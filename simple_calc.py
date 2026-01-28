import streamlit as st

st.title("Kalkulator")

a = st.number_input("Pierwsza liczba", value=0)
b = st.number_input("Druga liczba", value=0)

if st.button("Dodaj"):
    st.write(f"Wynik: {a + b}")