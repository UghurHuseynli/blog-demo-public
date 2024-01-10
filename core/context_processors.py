import requests
from django.conf import settings

def weather(request):
    try:
        r = requests.get(f'http://api.weatherapi.com/v1/current.json?key={settings.WEATHER_API_KEY}&q=Baku&aqi=no')
        weather = {
            'temperature': r.json()['current']['temp_c'],
            'condition': r.json()['current']['condition']
        }
    except:
        weather = {}
    
    return {'weather': weather}
