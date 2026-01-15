import requests

API_KEY = "00d777eeed59d5e0493401321e801466"  
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()

            print("\nWeather Details")
            print("---------------------")
            print("City:", data["name"])
            print("Temperature:", data["main"]["temp"], "°C")
            print("Humidity:", data["main"]["humidity"], "%")
            print("Weather:", data["weather"][0]["description"])

        elif response.status_code == 404:
            print("Error: City not found")

        else:
            print("Error: Failed to fetch data")

    except requests.exceptions.RequestException:
        print("Error: Network issue")

def main():
    city = input("Enter city name: ")
    get_weather(city)

main()
