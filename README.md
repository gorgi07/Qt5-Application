# Qt5-Application
# PyQT проект – «Солянка»
Проект «Солянка» - приложение, которое включает в себя функционал нескольких других приложений. Оно умеет находить погоду на сегодня и на 4 дня в указанном городе и имеет систему заметок, хранящихся в базе данных SQLite. Имеется возможность создавать, редактировать и удалять заметки.

## Установка
Проект реализован на языке Python, поэтому для его работы необходим
[интерпретатор этого языка] (https://www.python.org/downloads/). После установки
интерпретатора необходимо установить внешние библиотеки с помощью команды
`pip install -r path_to_project_dir/requirements.txt`

## Запуск
Для запуска приложения достаточно исполнить сценарий `main.py` любым из
доступных в вашей операционной системе способов. Например, чтобы запустить
приложение из командной строки, можно выполнить команду
`python main.py`
находясь в директории проекта.

## Структура проекта
Проект включает в себя следующие файлы:
* notes_data_base.db -- база данных с информацией о заметках
* main.py -- основной исполняемый файл проекта
* notes.py -- файл, хранящий функции для работы с базой данных
* weather.py -- файл, хранящий класс Weather() для работы с погодой
* disaine.ui -- файл дизайна приложения
* city_name.txt и city_name_2.txt -- файлы, хранящие информацию о последних введенных городах для получения погоды
* картинка.jpg -- картинка, используемая в проекте
* requirements.txt -- список внешних зависимостей
* readme.md -- этот файл

### База данных
База данных состоит из 1 таблицы:
* notes – таблица с записанными заметками
Каждая заметка содержит id, название и содержание.

