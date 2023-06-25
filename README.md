Функционал:
1) Разбор и сохранение данных из access логов веб-сервера Apache в базу данных.
2) Просмотр сохраненных данных в базе данных с возможностью группировки по IP и дате, а также выборки по промежутку дат.
3) Предоставление API для получения данных в формате JSON с возможностью фильтрации и группировки по IP.
4) Конфигурация приложения через файл настроек, включающая путь к логам, маску файлов и другие параметры.
5) Функция авторизации пользователей, хранение пользователей в базе данных.


Использование:
1) Установите Postgresql, создайте бд для работы

2) Проверьте наличие библиотек:
re
time
logging
yaml
json
datetime
schedule
pathlib
sqlalchemy

3) Настройка config.yml:
path:
  full_folder_path: полный путь до папки с логами (/var/logs)
  mask: строка, которая содержится в названии файла (access.log)

json:
  save_folder_path: полный путь до папки, в которую сохранятся логи.json

cron:
  state: true - включен, false - выключен
  repeat_minutes: повторение через n минут (1)

Этот параметр появится автоматически, число - номер строки, с которой начнется парсинг. Для перезаписи данных измените на 0.
file:
  access.log: 21
  access.log.1: 11
  access.log.2: 9

postgresql:
  username: myusername
  password: mypassword
  host_port: localhost:5432
  db: mydatabase

4) Начало парсинга - запустите в терминале python/python3 путь_до_файла/start_parse.py

5) Получить file.json/просмотреть данные - запустите view.py, следуйте инструкциям 

Пример проекта:
├── README.md
├── app
│   ├── choose.py
│   ├── json.py
│   └── parse.py
├── config
│   ├── config.py
│   └── config.yml
├── db
│   ├── models.py
│   └── mydb.py
├── json_file
│   ├── between_2023-06-25.json
│   └── ip_2023-06-25.json
├── requirements.txt
├── start_parse.py
├── test_data
│   ├── access.log
│   ├── access.log.1
│   └── access.log.2
└── view.py

Не меняйте названия файлов, не удаляйте файлы и не перемещайте.
