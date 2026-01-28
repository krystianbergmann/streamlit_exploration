import streamlit as st
import requests

st.title("🌡️ Aktualna temperatura")

latitude = 52.417755
longitude = 16.644808

url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}&longitude={longitude}"
    "&current_weather=true"
)

response = requests.get(url)
data = response.json()

temp = data["current_weather"]["temperature"]
time = data["current_weather"]["time"]

st.metric("Temperatura teraz", f"{temp} °C")
st.caption(f"Dane z godziny: {time}")