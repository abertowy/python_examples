import requests
import time

WEATHER_API_URL = "http://0.0.0.0:5000/weather"
CITY = "Belgrade"  # Change to your desired city

def fetch_weather():
    try:
        response = requests.get(WEATHER_API_URL, params={"city": CITY})
        if response.status_code == 200:
            print("Weather:", response.json())
        else:
            print("Error:", response.json())
    except Exception as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    while True:
        fetch_weather()
        time.sleep(120)  # Wait for 2 minutes