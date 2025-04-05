import requests
from config import API_KEY

def weather_by_city(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key": API_KEY,
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    result = requests.get(weather_url, params=params)
    weather = result.json()
    print(weather)
    if 'data' in weather:
        if 'current_condition' in weather['data']:
            try:
                return weather['data']['current_condition'][0]
            except(IndexError, TypeError):
                return False
        try:
            result = requests.get(weather_url, params=params)
            weather = result.json()
        except(requests.RequestException):
            return False
        try:
            result = requests.get(weather_url, params=params)
            result.raise_for_status()
            weather = result.json()
        except(requests.RequestException):
            return False
        try:
            result = requests.get(weather_url, params=params)
            result.raise_for_status()
            weather = result.json()
        except(requests.RequestException, ValueError):
            return False
    return False


if __name__ == "__main__":
    weather = weather_by_city("Moscow,Russia")
    print(weather)