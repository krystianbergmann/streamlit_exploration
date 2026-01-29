import streamlit as st
import requests

st.title("🌦️ Pogoda – teraz")

latitude = 52.417755
longitude = 16.644808

url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}&longitude={longitude}"
    "&current_weather=true"
    "&hourly=relativehumidity_2m"
)

response = requests.get(url)
data = response.json()

# TEMPERATURA (current)
temp = data["current_weather"]["temperature"]
time = data["current_weather"]["time"]

# WILGOTNOŚĆ (hourly – pierwsza wartość)
humidity = data["hourly"]["relativehumidity_2m"][0]

# DEBUG
print(f"Temperatura: {temp} °C")
print(f"Wilgotność: {humidity} %")
print(f"Czas: {time}")

# ---- LAYOUT ----
col1, col2 = st.columns(2)

with col1:
    st.metric("🌡️ Temperatura", f"{temp} °C")

with col2:
    st.metric("💧 Wilgotność", f"{humidity} %")

st.caption(f"Dane z godziny: {time}")