import requests
import time
import os
from pathlib import Path

SERVER_ADDR = os.getenv("SERVER_ADDR")
WEATHER_API_URL = f"http://{SERVER_ADDR}:5000/weather"
CITY = "Belgrade"  # Change to your desired city

def fetch_weather():
    file_path = Path("/data/weather.txt")
    file_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(WEATHER_API_URL, params={"city": CITY})
        if response.status_code == 200:
            with open ("/data/weather.txt", "a") as f:
                f.write(f"{time.ctime()}: {response.json()}\n")
            print("Weather:", response.json())
        else:
            print("Error:", response.json())
    except Exception as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    while True:
        fetch_weather()
        time.sleep(120)  # Wait for 2 minutes