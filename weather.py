import requests

def get_weather_forecast():
    url = 'http://api.openweathermap.org/data/2.5/find?q=Bangalore&units=metric&appid=<appid>'
    # create a free account and use the app id
    weather_request = requests.get(url)
    weather_data = weather_request.json()
    description = weather_data['list'][0]['weather'][0]['description']
    temp_min = weather_data['list'][0]['main']['temp_min']
    temp_max = weather_data['list'][0]['main']['temp_max']

    forecast = 'it looks like in Bangalore ' + description + ' with a minimum temperature of ' + str(temp_min) + 'C and a maximum temperature of ' + str(temp_max) + 'C'
    return forecast