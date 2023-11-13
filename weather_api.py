import requests

def get_weather(city_name):
    api_key = 'SUA_API_KEY'
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = f"{base_url}appid={api_key}&q={city_name}&units=metric"
    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data['cod'] != 404:
        main = weather_data['main']
        temperature = main['temp']
        humidity = main['humidity']
        weather_description = weather_data['weather'][0]['description']
        print(f"Temperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {weather_description}")
    else:
        print("City not found!")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
