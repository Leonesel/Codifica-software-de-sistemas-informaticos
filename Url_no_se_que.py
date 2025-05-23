#Request: comucarse los sistemas por internet
#Get, Post, Put, Delete
#500 servidor, error 400 tu error, 300 diferentes parametros inspector
#pipinstall Requests2-1.py
#pytube for videos
import requests
import shutil
import json

class Llamadanoseque:

    def coso_coso(self):
        r = requests.get(url="https://youtu.be/wZY4TU7O1ao?t=48")
        print(r.content)
        print(r.status_code)

    def gogogo(self, url, file_name):
        res = requests.get(url,stream=True)
        if 200 == res.status_code:
            with open(file_name, "wb") as f:
                shutil.copyfileobj(res.raw,f)
            print("imagen descarga completamente")
        else:
            print("No se encontro nada")

    def get_ay_ora(self, city, api_key):
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        params = {"q": city, "appid": api_key, "units": "metric"} #Use "imperial" for Fahrenheit

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status() #Raise HTTPError for bad responses (4xx or 5xx)

            weather_data = response.json()

            if weather_data["cod"] == 200:
                print(f"Weather in {weather_data['name']}:")
                print(f"  Description: {weather_data['weather'][0]['description']}")
                print(f"  Temperature: {weather_data['main']['temp']}°C")
                print(f"  Humedity: {weather_data['main']['humidity']}%")
                print(f"  Wind Speed: {weather_data['wind']['speed']} m/s")
            else:
                print(f"Error: {weather_data['message']}")
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
        except json.JSONDecodeError:
            print("Error: Could not decode JSON response")
    
url_= 'https://youtu.be/3GWkoMM0IzU'
url = 'https://img.freepik.com/vector-gratis/hermosa-pareja-lesbianas-bandera-lgbt-ilustrada_23-2148882366.jpg'
api_key = "69ec8ca2037d63a120d31c59efd0f604"
city = "Zapopan"

ye = Llamadanoseque()
ye.get_ay_ora(city, api_key)