import requests
from colorama import Fore
import re
import datetime


class ApiError400(Exception):
    pass


class ApiError401(Exception):
    pass


class ApiError404(Exception):
    pass


class ApiError429(Exception):
    pass


class ApiError5XX(Exception):
    pass


class Weather:
    def __init__(self, api: str) -> None:
        self._api = api
        self._error_list = ["400", "401", "404", "429"]
        self.error_cod = ""

    def _check_error(self, value: str) -> None:
        """
        Функция для проверки возвращаемого значения на ошибки
        """
        try:
            if value in self._error_list or value[0] == "5":
                if value == "400":
                    raise ApiError400

                elif value == "401":
                    raise ApiError401

                elif value == "404":
                    raise ApiError404

                elif value == "429":
                    raise ApiError429

                elif re.fullmatch(r"5\d\d", value):
                    raise ApiError5XX
            else:
                raise Exception

        except ApiError400:
            self.error_cod = f"[ОШИБКА 400] Неверный запрос"
            print(Fore.RED + f"[ОШИБКА 400] Неверный запрос")

        except ApiError401:
            self.error_cod = f"[ОШИБКА 401] API не указан или " \
                              f"API недействителен"
            print(Fore.RED + f"[ОШИБКА 401] API не указан или "
                             f"API недействителен")

        except ApiError404:
            self.error_cod = f"[ОШИБКА 404] Данные о погоде не найдены"
            print(Fore.RED + f"[ОШИБКА 404] Данные о погоде не найдены")

        except ApiError429:
            self.error_cod = f"[ОШИБКА 429] Приносим извинения, " \
                              f"на сегодня закончились попытки доступа " \
                              f"к погоде"
            print(
                Fore.LIGHTRED_EX + f"[ОШИБКА 429] Приносим извинения, "
                                   f"на сегодня закончились попытки доступа "
                                   f"к погоде")

        except ApiError5XX:
            self.error_cod = f"[ОШИБКА 5XX] Непредвиденная ошибка сервиса"
            print(Fore.RED + f"[ОШИБКА 5XX] Непредвиденная ошибка сервиса")

        except Exception:
            self.error_cod = f"[ОШИБКА] Неизвестный код ошибки"
            print(Fore.RED + f"[ОШИБКА] Неизвестный код ошибки")

    def get_city_id(self, city: str) -> int | None:
        """
        Функция для получения ID указаннного города из базы данных сайта
        """
        self.error_cod = ""
        try:
            url = f"http://api.openweathermap.org/data/2.5/find?" \
                  f"q={city}&type=like&units=metric&appid={self._api}"
            data = requests.get(url).json()

            if str(data["cod"]) == "200" and data["list"]:
                city_id = data["list"][0]["id"]
                print(Fore.LIGHTGREEN_EX + "[УСПЕХ] ID города получен")
                return city_id

            return self._check_error(str(data["cod"]))

        except Exception:
            self.error_cod = f"[ОШИБКА] Не удалось получить ID города"
            print(Fore.RED + f"[ОШИБКА] Не удалось получить ID города")

    def get_current_weather(self, city_id: int) -> list | None:
        """
        Функция для получения погоды (Температура, Ощущаемая температура и
        Скорость ветра) в данный момент времени
        """
        url = f"https://api.openweathermap.org/data/2.5/weather?" \
              f"id={city_id}&units=metric&lang=ru&appid={self._api}"
        weather_data = requests.get(url).json()
        try:
            if str(weather_data["cod"]) == "200":
                temperature = round(weather_data["main"]["temp"], 1)
                temperature_feels = round(
                    weather_data["main"]["feels_like"], 1)
                wind_speed = round(weather_data["wind"]["speed"], 1)

                if abs(temperature) == 0.0:
                    temperature = 0

                if abs(temperature_feels) == 0.0:
                    temperature_feels = 0

                if abs(wind_speed) == 0.0:
                    wind_speed = 0

                print(Fore.LIGHTGREEN_EX + "[УСПЕХ] Данные о погоде получены")
                info = [str(datetime.datetime.today()).split()[0],
                        temperature,
                        temperature_feels,
                        wind_speed]
                return info

            return self._check_error(str(weather_data["cod"]))

        except Exception:
            self.error_cod = f"[ОШИБКА] Не удалось получить данные о погоде"
            print(Fore.RED + f"[ОШИБКА] Не удалось получить данные о погоде")

    def get_weather_forecast(self, city_id: int) -> list[list] | None:
        """
        Функция для получения прогноза погоды (Температура, Ощущаемая
        температура и Скорость ветра) на 4 дня
        """
        url = f"https://api.openweathermap.org/data/2.5/forecast?" \
              f"id={city_id}&units=metric&lang=ru&appid={self._api}"
        weather_data = requests.get(url).json()
        weather = [self.get_current_weather(city_id)]
        count = 0
        try:
            if str(weather_data["cod"]) == "200":
                for day in weather_data["list"][1:]:
                    if count != 4:
                        if day["dt_txt"].split()[1] == "15:00:00":

                            temperature = round(day["main"]["temp"], 1)
                            temperature_feels = round(
                                day["main"]["feels_like"], 1)
                            wind_speed = round(day["wind"]["speed"], 1)

                            if abs(temperature) == 0.0:
                                temperature = 0

                            if abs(temperature_feels) == 0.0:
                                temperature_feels = 0

                            if abs(wind_speed) == 0.0:
                                wind_speed = 0

                            info = [day["dt_txt"].split()[0], temperature,
                                    temperature_feels, wind_speed]

                            weather.append(info)
                            count += 1

                return weather

            return self._check_error(str(weather_data["cod"]))

        except Exception:
            self.error_cod = f"[ОШИБКА] Не удалось получить данные о погоде"
            print(Fore.RED + f"[ОШИБКА] Не удалось получить данные о погоде")
