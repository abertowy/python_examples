from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

WEATHER_API_KEY = "5eff2c57a6545c563ddbcd586aa6269a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/weather", methods=["GET"])
def get_weather():
    city_name = request.args.get("city")
    if not city_name:
        return jsonify({"error": "City name is required"}), 400

    params = {
        "q": city_name,
        "appid": WEATHER_API_KEY,
        "units": "metric"  # or "imperial" for Fahrenheit
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        weather_data = response.json()

        if weather_data.get("cod") == 200:
            temperature = weather_data["main"]["temp"]
            return jsonify({"city": city_name, "temperature": f"{temperature}°C"})
        else:
            return jsonify({"error": weather_data.get("message", "City not found or API error")}), 404

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error fetching weather data: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)