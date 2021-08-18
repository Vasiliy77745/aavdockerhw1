from flask import Flask
import requests, os

app = Flask(__name__)

@app.route("/")
def weather():
    params = {'q': os.environ['MYAPP_CITY'], 'appid': os.environ['MYAPP_API_KEY'], 'units': 'metric'}
    receive = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    temp = receive.json()['main']['temp']
    desc = receive.json()['weather'][0]['description']
    name = os.environ['MYAPP_NAME']
    return f"Hi {name}, {temp}°C {desc}."
