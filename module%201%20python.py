import requests
import matplotlib.pyplot as plt

city = input("Enter city name: ")

API_KEY = "YOUR_API_KEY"

url = (
    "https://api.openweathermap.org/data/2.5/weather"
    f"?q={city}&appid={API_KEY}&units=metric"
)

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print("\nWeather Report")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Weather:", description)

except Exception:
    print("API unavailable. Showing sample data.")

    temperature = 28
    humidity = 65

    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")

if temperature > 30:
    print("Weather Analysis: Hot")
elif temperature < 20:
    print("Weather Analysis: Cool")
else:
    print("Weather Analysis: Moderate")

labels = ["Temperature (°C)", "Humidity (%)"]
values = [temperature, humidity]

plt.bar(labels, values)
plt.title("Weather Data Analytics Dashboard")
plt.ylabel("Values")
plt.show()
