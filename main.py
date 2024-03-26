import io
import sys
from art import tprint
from colorama import init
from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem,
                             QHeaderView)
from weather import *
from notes import *

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>600</width>
    <height>400</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Солянка</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTabWidget" name="tab_widget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>600</width>
      <height>400</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>11</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>ArrowCursor</cursorShape>
    </property>
    <property name="currentIndex">
     <number>0</number>
    </property>
    <widget class="QWidget" name="tab">
     <attribute name="title">
      <string>Главная</string>
     </attribute>
     <widget class="QLabel" name="picture">
      <property name="geometry">
       <rect>
        <x>50</x>
        <y>5</y>
        <width>480</width>
        <height>360</height>
       </rect>
      </property>
      <property name="text">
       <string/>
      </property>
      <property name="pixmap">
       <pixmap>картинка.jpg</pixmap>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="tab_weather">
     <attribute name="title">
      <string>Погода</string>
     </attribute>
     <widget class="QTabWidget" name="tab_weather_widget">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>0</y>
        <width>600</width>
        <height>370</height>
       </rect>
      </property>
      <property name="currentIndex">
       <number>0</number>
      </property>
      <widget class="QWidget" name="current_weather">
       <attribute name="title">
        <string>Погода сегодня</string>
       </attribute>
       <widget class="QLabel" name="temperature_label">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>90</y>
          <width>100</width>
          <height>40</height>
         </rect>
        </property>
        <property name="text">
         <string>Температура:</string>
        </property>
       </widget>
       <widget class="QLabel" name="date_label">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>40</y>
          <width>45</width>
          <height>40</height>
         </rect>
        </property>
        <property name="text">
         <string>Дата:</string>
        </property>
       </widget>
       <widget class="QLabel" name="temperature_feels_label">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>140</y>
          <width>120</width>
          <height>40</height>
         </rect>
        </property>
        <property name="text">
         <string>Ощущается как:</string>
        </property>
       </widget>
       <widget class="QLabel" name="wind_speed_label">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>190</y>
          <width>120</width>
          <height>40</height>
         </rect>
        </property>
        <property name="text">
         <string>Скорость ветра:</string>
        </property>
       </widget>
       <widget class="QLabel" name="data_label_text">
        <property name="geometry">
         <rect>
          <x>65</x>
          <y>40</y>
          <width>150</width>
          <height>40</height>
         </rect>
        </property>
        <property name="text">
         <string>00-00-0000</string>
        </property>
       </widget>
       <widget class="QLabel" name="temperature_label_text">
        <property name="geometry">
         <rect>
          <x>120</x>
          <y>90</y>
          <width>150</width>
          <height>40</height>
         </rect>
        </property>
        <property name="text">
         <string>0 °С</string>
        </property>
       </widget>
       <widget class="QLabel" name="temperature_feels_label_text">
        <property name="geometry">
         <rect>
          <x>140</x>
          <y>140</y>
          <width>150</width>
          <height>40</height>
         </rect>
        </property>
        <property name="text">
         <string>0 °С</string>
        </property>
       </widget>
       <widget class="QLabel" name="wind_speed_label_text">
        <property name="geometry">
         <rect>
          <x>140</x>
          <y>190</y>
          <width>150</width>
          <height>40</height>
         </rect>
        </property>
        <property name="text">
         <string>0 м/с</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="city_name_line_edit">
        <property name="geometry">
         <rect>
          <x>200</x>
          <y>10</y>
          <width>200</width>
          <height>30</height>
         </rect>
        </property>
        <property name="text">
         <string>Москва</string>
        </property>
       </widget>
       <widget class="QPushButton" name="update_info_button">
        <property name="geometry">
         <rect>
          <x>200</x>
          <y>260</y>
          <width>200</width>
          <height>30</height>
         </rect>
        </property>
        <property name="text">
         <string>Обновить информацию</string>
        </property>
       </widget>
       <widget class="QLabel" name="error_label">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>290</y>
          <width>300</width>
          <height>40</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">QLabel {color: rgb(255, 0, 0)}</string>
        </property>
        <property name="text">
         <string/>
        </property>
       </widget>
      </widget>
      <widget class="QWidget" name="weather_forecast">
       <attribute name="title">
        <string>Прогноз на 4 дня</string>
       </attribute>
       <widget class="QLineEdit" name="city_name_line_edit_2">
        <property name="geometry">
         <rect>
          <x>200</x>
          <y>10</y>
          <width>200</width>
          <height>30</height>
         </rect>
        </property>
        <property name="text">
         <string>Москва</string>
        </property>
       </widget>
       <widget class="QPushButton" name="update_info_button_2">
        <property name="geometry">
         <rect>
          <x>200</x>
          <y>260</y>
          <width>200</width>
          <height>30</height>
         </rect>
        </property>
        <property name="text">
         <string>Обновить информацию</string>
        </property>
       </widget>
       <widget class="QLabel" name="error_label_2">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>290</y>
          <width>300</width>
          <height>40</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">QLabel {color: rgb(255, 0, 0)}</string>
        </property>
        <property name="text">
         <string/>
        </property>
       </widget>
       <widget class="QTableWidget" name="weather_table">
        <property name="geometry">
         <rect>
          <x>30</x>
          <y>70</y>
          <width>540</width>
          <height>160</height>
         </rect>
        </property>
        <row>
         <property name="text">
          <string>Дата</string>
         </property>
        </row>
        <row>
         <property name="text">
          <string>Температура</string>
         </property>
        </row>
        <row>
         <property name="text">
          <string>Ощущается как</string>
         </property>
        </row>
        <row>
         <property name="text">
          <string>Скорость ветра</string>
         </property>
        </row>
        <column>
         <property name="text">
          <string>1</string>
         </property>
        </column>
        <column>
         <property name="text">
          <string>2</string>
         </property>
        </column>
        <column>
         <property name="text">
          <string>3</string>
         </property>
        </column>
        <column>
         <property name="text">
          <string>4</string>
         </property>
        </column>
       </widget>
      </widget>
     </widget>
    </widget>
    <widget class="QWidget" name="tab_notes">
     <attribute name="title">
      <string>Заметки</string>
     </attribute>
     <widget class="QTableWidget" name="notes_table">
      <property name="geometry">
       <rect>
        <x>350</x>
        <y>0</y>
        <width>240</width>
        <height>360</height>
       </rect>
      </property>
      <property name="minimumSize">
       <size>
        <width>10</width>
        <height>10</height>
       </size>
      </property>
      <column>
       <property name="text">
        <string>id</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>Название</string>
       </property>
      </column>
     </widget>
     <widget class="QTabWidget" name="tabWidget">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>0</y>
        <width>340</width>
        <height>370</height>
       </rect>
      </property>
      <property name="currentIndex">
       <number>0</number>
      </property>
      <widget class="QWidget" name="create_tab">
       <attribute name="title">
        <string>Создать</string>
       </attribute>
       <widget class="QLabel" name="name">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>10</y>
          <width>220</width>
          <height>30</height>
         </rect>
        </property>
        <property name="text">
         <string>Введите название заметки:</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="title">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>50</y>
          <width>300</width>
          <height>30</height>
         </rect>
        </property>
       </widget>
       <widget class="QLabel" name="content_label">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>90</y>
          <width>220</width>
          <height>30</height>
         </rect>
        </property>
        <property name="text">
         <string>Введите содержание заметки:</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="content">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>130</y>
          <width>300</width>
          <height>120</height>
         </rect>
        </property>
       </widget>
       <widget class="QPushButton" name="create_save_button">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>260</y>
          <width>300</width>
          <height>30</height>
         </rect>
        </property>
        <property name="text">
         <string>Создать заметку</string>
        </property>
       </widget>
       <widget class="QLabel" name="error_label_create">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>310</y>
          <width>300</width>
          <height>20</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">QLabel {color: rgb(255, 0, 0)}</string>
        </property>
        <property name="text">
         <string/>
        </property>
       </widget>
      </widget>
      <widget class="QWidget" name="edit_tab">
       <attribute name="title">
        <string>Изменить</string>
       </attribute>
       <widget class="QLabel" name="id_edit_label">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>0</y>
          <width>250</width>
          <height>30</height>
         </rect>
        </property>
        <property name="text">
         <string>Введите ID изменяемой заметки:</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="id_edit">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>40</y>
          <width>300</width>
          <height>30</height>
         </rect>
        </property>
       </widget>
       <widget class="QLabel" name="title_edit_label">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>120</y>
          <width>220</width>
          <height>30</height>
         </rect>
        </property>
        <property name="text">
         <string>Название заметки:</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="title_edit">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>160</y>
          <width>300</width>
          <height>30</height>
         </rect>
        </property>
       </widget>
       <widget class="QLabel" name="content_edit_label">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>200</y>
          <width>220</width>
          <height>30</height>
         </rect>
        </property>
        <property name="text">
         <string>Содержание заметки:</string>
        </property>
       </widget>
       <widget class="QLabel" name="error_label_edit">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>310</y>
          <width>300</width>
          <height>20</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">QLabel {color: rgb(255, 0, 0)}</string>
        </property>
        <property name="text">
         <string/>
        </property>
       </widget>
       <widget class="QPushButton" name="edit_save_button">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>275</y>
          <width>300</width>
          <height>30</height>
         </rect>
        </property>
        <property name="text">
         <string>Сохранить</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="content_edit">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>240</y>
          <width>300</width>
          <height>30</height>
         </rect>
        </property>
       </widget>
       <widget class="QPushButton" name="search_for_note_button">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>80</y>
          <width>300</width>
          <height>30</height>
         </rect>
        </property>
        <property name="text">
         <string>Найти заметку</string>
        </property>
       </widget>
      </widget>
      <widget class="QWidget" name="delete_tab">
       <attribute name="title">
        <string>Удалить</string>
       </attribute>
       <widget class="QLabel" name="id_delete_label">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>10</y>
          <width>220</width>
          <height>30</height>
         </rect>
        </property>
        <property name="text">
         <string>Введите ID заметки:</string>
        </property>
       </widget>
       <widget class="QPushButton" name="delete_button">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>90</y>
          <width>300</width>
          <height>30</height>
         </rect>
        </property>
        <property name="text">
         <string>Удалить заметку</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="id_delete">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>50</y>
          <width>300</width>
          <height>30</height>
         </rect>
        </property>
       </widget>
       <widget class="QLabel" name="error_label_delete">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>300</y>
          <width>300</width>
          <height>30</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">QLabel {color: rgb(255, 0, 0)}</string>
        </property>
        <property name="text">
         <string/>
        </property>
       </widget>
      </widget>
     </widget>
    </widget>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
init()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        file = io.StringIO(template)
        uic.loadUi(file, self)

        # Активация кнопки на странице "Погода сегодня" и получение
        # названия последнего введенного города
        with open("city_name.txt", "r", encoding="utf-8") as read_file:
            self.city_name = read_file.read().split("\n")[0]
        self.weather = Weather(API)
        self.city_name_line_edit.setText(self.city_name)
        self.update_info_button.clicked.connect(self.update_info)

        # Активация кнопки на странице "Прогноз на 4 дня" и получение
        # названия последнего введенного города
        with open("city_name_2.txt", "r", encoding="utf-8") as read_file_2:
            self.city_name_2 = read_file_2.read().split("\n")[0]
        self.weather_2 = Weather(API)
        self.city_name_line_edit_2.setText(self.city_name_2)
        self.update_info_button_2.clicked.connect(self.update_info_2)

        # Ввод данных в таблицу заметок
        self.filling_table()

        # Обработка кнопки "Создать заметку"
        self.create_save_button.clicked.connect(self.create_new_note)

        # Обработка кнопки "Найти заметку"
        self.search_for_note_button.clicked.connect(self.search_note)

        # Обрабока кнопки "Сохранить"
        self.edit_save_button.clicked.connect(self.save_edit_note)

        # Обработка кнопки "Удалить заметку"
        self.delete_button.clicked.connect(self.delete_note_in_bd)

    def filling_table(self) -> None:
        """
        Функция для заполнения таблицы с заметками
        """
        lines_count = 0
        data = get_notes_for_table(DATA_BASE)
        self.notes_table.setRowCount(len(data))
        if not (data is None):
            for this_id, this_title in data:
                self.notes_table.setItem(lines_count, 0,
                                         QTableWidgetItem(str(this_id)))
                self.notes_table.setItem(lines_count, 1,
                                         QTableWidgetItem(str(this_title)))
                lines_count += 1
            self.notes_table.horizontalHeader().setSectionResizeMode(
                QHeaderView.ResizeToContents)
            self.notes_table.horizontalHeader().setMinimumSectionSize(0)
            print(Fore.LIGHTGREEN_EX + "[УСПЕХ] Таблица заполнена")
        else:
            print(Fore.RED + "[ОШИБКА] Не удалось заполнить таблицу")

    def create_new_note(self) -> None:
        """
        Функция для создания новой заметки
        """
        title = self.title.text()
        content = self.content.text()
        if title:
            if content:
                self.error_label_create.setText("")
                new_id = find_missing_id(DATA_BASE)
                create_note(DATA_BASE, new_id=new_id, title=title,
                            content=content)
                self.title.setText("")
                self.content.setText("")
                self.filling_table()
        else:
            self.error_label_create.setText("Не все поля заполнены")
            print(Fore.RED + "[ОШИБКА] Не удалось создать таблицу")

    def search_note(self) -> None:
        """
        Функция для поиска заметки по id
        """
        entered_id = self.id_edit.text()
        self.title_edit.setText("")
        self.content_edit.setText("")
        new_data = get_id_list(DATA_BASE)
        if int(entered_id) in new_data:
            data = get_note(DATA_BASE, entered_id)
            if not (data is None):
                self.error_label_edit.setText("")
                self.title_edit.setText(data[0])
                self.content_edit.setText(data[1])
                print(Fore.LIGHTGREEN_EX + f"[УСПЕХ] Запись с ID {entered_id} "
                                           f"найдена")
            else:
                self.error_label_edit.setText("ID записи введен не верно")
                print(Fore.RED + f"[ОШИБКА] Запись с ID {entered_id} "
                                 f"не существует")
        else:
            self.error_label_edit.setText("ID записи введен неверно")
            print(Fore.RED + "[ОШИБКА] ID записи введен неверно")

    def save_edit_note(self) -> None:
        """
        Функция для сохранения измений в заметке
        """
        entered_id = self.id_edit.text()
        new_data = get_id_list(DATA_BASE)
        if int(entered_id) in new_data:
            new_title = self.title_edit.text()
            new_content = self.content_edit.text()
            edit_note(DATA_BASE, entered_id, new_title=new_title,
                      new_content=new_content)
            self.id_edit.setText("")
            self.title_edit.setText("")
            self.content_edit.setText("")
            print(Fore.LIGHTGREEN_EX + f"[УСПЕХ] Запись с ID {entered_id} "
                                       f"сохранена")
            self.filling_table()
        else:
            self.error_label_edit.setText("ID записи введен неверно")
            print(Fore.RED + "[ОШИБКА] ID записи введен неверно")

    def delete_note_in_bd(self) -> None:
        """
        Функция для удаления заметки
        """
        entered_id = self.id_delete.text()
        new_data = get_id_list(DATA_BASE)
        if int(entered_id) in new_data:
            self.error_label_delete.setText("")
            delete_note(DATA_BASE, entered_id)
            self.id_delete.setText("")
            print(Fore.LIGHTGREEN_EX + f"[УСПЕХ] Запись с ID {entered_id} "
                                       f"удалена")
            self.filling_table()
        else:
            self.error_label_delete.setText("ID записи введен неверно")
            print(Fore.RED + "[ОШИБКА] ID записи введен неверно")

    def update_info(self) -> None:
        """
        Функция для обновления информации о погоде на сегодня
        """
        self.city_name = self.city_name_line_edit.text()
        with open("city_name.txt", "w", encoding="utf-8") as write_file:
            write_file.write(self.city_name)

        temperature_data = self.weather.get_current_weather(
            self.weather.get_city_id(self.city_name))

        if self.weather.error_cod != "":
            self.error_label.setText(self.weather.error_cod)
        else:
            self.error_label.setText("")
            self.data_label_text.setText(str(temperature_data[0]))
            self.temperature_label_text.setText(str(temperature_data[1])
                                                + " °С")
            self.temperature_feels_label_text.setText(str(temperature_data[2])
                                                      + " °С")
            self.wind_speed_label_text.setText(str(temperature_data[3])
                                               + " м/с")

    def update_info_2(self) -> None:
        """
        Функция для обновления информации о погоде на 4 дня
        """
        self.city_name_2 = self.city_name_line_edit_2.text()
        with open("city_name_2.txt", "w", encoding="utf-8") as write_file_2:
            write_file_2.write(self.city_name_2)

        data = self.weather_2.get_weather_forecast(
            self.weather_2.get_city_id(self.city_name_2))

        if self.weather_2.error_cod != "":
            self.error_label_2.setText(self.weather_2.error_cod)
        else:
            self.error_label_2.setText("")
            for i in range(4):
                self.weather_table.setItem(0, i, QTableWidgetItem(
                    str(data[i][0])))
                self.weather_table.setItem(1, i, QTableWidgetItem(
                    f"{data[i][1]} °С"))
                self.weather_table.setItem(2, i, QTableWidgetItem(
                    f"{data[i][2]} °С"))
                self.weather_table.setItem(3, i, QTableWidgetItem(
                    f"{data[i][3]} м/с"))


if __name__ == '__main__':
    print(Fore.LIGHTBLUE_EX + "")
    tprint("SOLYANKA")
    API = "bd9da7aba0c072b65abef58742537fc8"
    DATA_BASE = "notes_data_base.db"
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
