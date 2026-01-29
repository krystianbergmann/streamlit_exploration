import streamlit as st
import requests

st.title("🌦️ Pogoda – teraz i prognoza")

# -----------------------
# WSPÓŁRZĘDNE
# -----------------------
latitude = 52.417755
longitude = 16.644808
if st.button("🔄 Odśwież dane"):
    print("Odświeżenie danych...")
# -----------------------
# API URL
# -----------------------
url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}&longitude={longitude}"
    "&current_weather=true"
    "&hourly=apparent_temperature,relativehumidity_2m,cloudcover"
    "&daily=temperature_2m_max"
    "&timezone=auto"
)

# -----------------------
# POBRANIE DANYCH
# -----------------------
response = requests.get(url)
data = response.json()

# -----------------------
# DANE „TERAZ”
# -----------------------
temp_now = data["current_weather"]["temperature"]              # temperatura aktualna
apparent_temp = data["hourly"]["apparent_temperature"][0]      # odczuwalna
humidity = data["hourly"]["relativehumidity_2m"][0]            # wilgotność
clouds = data["hourly"]["cloudcover"][0]                       # zachmurzenie %
time = data["current_weather"]["time"]                          # czas pobrania

# -----------------------
# DANE „PROGNOZA”
# -----------------------
temp_tomorrow = data["daily"]["temperature_2m_max"][1]         # jutro
temp_day_after = data["daily"]["temperature_2m_max"][2]        # pojutrze

# -----------------------
# DEBUG (terminal)
# -----------------------
print("DEBUG:")
print("Temp teraz:", temp_now)
print("Odczuwalna:", apparent_temp)
print("Wilgotność:", humidity)
print("Zachmurzenie:", clouds)
print("Jutro:", temp_tomorrow)
print("Pojutrze:", temp_day_after)
print("Dane z godziny: ", time)

# =======================
# WIERSZ 1
# =======================
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🌡️ Temperatura teraz", f"{temp_now} °C")

with col2:
    st.metric("🤔 Odczuwalna", f"{apparent_temp} °C")

with col3:
    st.metric("💧 Wilgotność", f"{humidity} %")

# =======================
# WIERSZ 2
# =======================
col4, col5, col6 = st.columns(3)

with col4:
    st.metric("📅 Jutro", f"{temp_tomorrow} °C")

with col5:
    st.metric("📅 Pojutrze", f"{temp_day_after} °C")

with col6:
    st.metric("☁️ Zachmurzenie", f"{clouds} %")

st.caption(f"Dane z godziny: {time}")