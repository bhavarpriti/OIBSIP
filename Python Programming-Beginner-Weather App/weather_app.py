
import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


def get_weather(city):
    url = (
        "https://wttr.in/"
        + city.replace(" ", "+")
        + "?format=j1"
    )

    try:
        with urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))

        current = data["current_condition"][0]
        location = data["nearest_area"][0]["areaName"][0]["value"]

        print("\n------ WEATHER REPORT ------")
        print("City:", location)
        print("Temperature:", current["temp_C"], "°C")
        print("Feels Like:", current["FeelsLikeC"], "°C")
        print("Weather:", current["weatherDesc"][0]["value"])
        print("Humidity:", current["humidity"] + "%")
        print("Wind Speed:", current["windspeedKmph"], "km/h")
        print("----------------------------")

    except (HTTPError, URLError, TimeoutError):
        print("Unable to retrieve weather data. Please check your internet connection.")
    except (KeyError, IndexError, json.JSONDecodeError):
        print("Unable to process weather data. Please try again.")


def main():
    print("Welcome to Python Weather App!")
    city = input("Enter city name: ").strip()

    if city:
        get_weather(city)
    else:
        print("Please enter a valid city name.")


if __name__ == "__main__":
    main()

