import streamlit as st

st.title("Aplikacja z menu")

option = st.sidebar.selectbox(
    "Wybierz widok:",
    ("Strona główna", "O aplikacji", "Kontakt")
)

if option == "Strona główna":
    st.write("🏠 Witaj na stronie głównej")
elif option == "O aplikacji":
    st.write("ℹ️ To jest aplikacja w Streamlit")
elif option == "Kontakt":
    st.write("📧 kontakt@example.com")