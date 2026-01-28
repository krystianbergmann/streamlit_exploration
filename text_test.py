import streamlit as st

st.title("Prezentacja tekstów w Streamlit")

st.header("Podstawowe teksty")
st.write("To jest st.write() – najbardziej uniwersalne")
st.text("To jest st.text() – surowy tekst")

st.subheader("Markdown")
st.markdown("""
**Pogrubienie**, *kursywa*, `kod inline`

- Punkt 1
- Punkt 2
- Punkt 3

[Link do Streamlit](https://streamlit.io)
""")

st.caption("To jest caption – mały opis")

st.subheader("Kod")
st.code("""
def hello():
    print("Hello Streamlit")
""", language="python")

st.subheader("Wzory matematyczne")
st.latex(r"a^2 + b^2 = c^2")

st.subheader("Komunikaty")
st.info("To jest informacja")
st.success("Operacja zakończona sukcesem ✅")
st.warning("Uwaga! Coś może pójść nie tak ⚠️")
st.error("Błąd! Coś się zepsuło ❌")