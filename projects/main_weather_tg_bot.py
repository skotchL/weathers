from multiprocessing.spawn import _main
import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from main import main

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler()
async def get_weather(message:types.Message):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        data = r.json()
        city = data["name"]
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        length_of_day = datetime.datetime.fromtimestamp(data['sys']['sunrise']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])

        await message.reply(f"----- {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}----- \n"
        f"{city}da ob-havo\nTemperatura: {cur_weather}C\n"
        f"Namlik: {humidity}%\nDavleniya:{pressure}  \nShamol:{wind}\nQuyosh vasxodi:{sunrise_timestamp}\n"
        f"Kuningiz yaxshi o'tsin! )"
        )

    except:
        await message.reply("Qaytadan tekshirib koring shahar ismini")



@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Salom, menga shahar ismini yozing va men siz yozgan shahar ob-havosini sizga taqdim etaman")

if __name__ == '__main__':
    executor.start_polling(dp)