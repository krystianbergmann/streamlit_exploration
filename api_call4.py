import streamlit as st
import requests

st.title("🌤️ Pogoda – teraz i prognoza")

# -----------------------
# WSPÓŁRZĘDNE
# -----------------------
latitude = 52.417755
longitude = 16.644808

# -----------------------
# API URL
# -----------------------
url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}&longitude={longitude}"
    "&current_weather=true"
    "&hourly=apparent_temperature,cloudcover"
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
apparent_temp = data["hourly"]["apparent_temperature"][0]   # temperatura odczuwalna
wind_speed = data["current_weather"]["windspeed"]            # prędkość wiatru
clouds = data["hourly"]["cloudcover"][0]                     # zachmurzenie %

# -----------------------
# DANE „JUTRO / POJUTRZE”
# -----------------------
temp_tomorrow = data["daily"]["temperature_2m_max"][1]
temp_day_after = data["daily"]["temperature_2m_max"][2]

# -----------------------
# DEBUG (terminal)
# -----------------------
print("DEBUG:")
print(apparent_temp, wind_speed, clouds)
print(temp_tomorrow, temp_day_after)

# =======================
# LAYOUT – WIERSZ 1
# =======================
row1_col1, row1_col2, row1_col3 = st.columns(3)

with row1_col1:
    st.metric("🌡️ Odczuwalna", f"{apparent_temp} °C")

with row1_col2:
    st.metric("💨 Wiatr", f"{wind_speed} km/h")

with row1_col3:
    st.metric("☁️ Zachmurzenie", f"{clouds} %")

# =======================
# LAYOUT – WIERSZ 2
# =======================
row2_col1, row2_col2, row2_col3 = st.columns(3)

with row2_col1:
    st.metric("📅 Jutro", f"{temp_tomorrow} °C")

with row2_col2:
    st.metric("📅 Pojutrze", f"{temp_day_after} °C")

with row2_col3:
    st.write("")  # puste miejsce (świadomie)