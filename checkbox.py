import streamlit as st

st.title("Opcje zaawansowane")

show = st.checkbox("Pokaż szczegóły")

if show:
    st.write("🔍 Oto dodatkowe informacje")
    st.write("Możesz tu dodać więcej treści")