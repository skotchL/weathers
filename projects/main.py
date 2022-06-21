from cmath import exp
from operator import length_hint
import requests
from config import open_weather_token
import datetime
from pprint import pprint

def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)
        city = data["name"]
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        length_of_day = datetime.datetime.fromtimestamp(data['sys']['sunrise']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])

        print(f"----- {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}----- \n"
        f"{city}da ob-havo\nTemperatura: {cur_weather}C\n"
        f"Namlik: {humidity}%\nDavleniya:{pressure}  \nShamol:{wind}\nQuyosh vasxodi:{sunrise_timestamp}\n"
        f"Kuningiz yaxshi o'tsin! )"
        )

    except Exception as ex:
        print(ex)
        print("Qaytadan tekshirib koring shahar ismini")


def main():
    city = input("Shahar kiriting :D :")
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()