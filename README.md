# weather_bot
# Телеграм бот для определения погоды в вашем городе

Определяет погоду по названию города:

<img src=/docs/photo_2022-08-11_00-08-20.jpg width=300>

## Как запустить свой

Для работы проекта необходим ключ https://openweathermap.org/. Его можно бесплатно получить на сайте.

Нужно скачать проект с помощью git clone. Далее создать в папке проекта файл config.py следующего содержания:

```
TOKEN='your_telegram_bot_token'
weather_key = 'your key for https://openweathermap.org/'
```

Далее, находясь в папке проекта, выполняем
```
python3 bot.py
```
# Где посмотреть
[Вот тут](https://t.me/weather_by_mary_bot)
