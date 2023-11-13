def process_weather_data(weather_data):
    if weather_data['cod'] != 404:
        main = weather_data['main']
        temperature = main['temp']
        humidity = main['humidity']
        weather_description = weather_data['weather'][0]['description']
        return f"Temperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {weather_description}"
    else:
        return "City not found!"
