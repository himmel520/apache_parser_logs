<h2>Функционал:</h2>
<ol>
  <li>Разбор и сохранение данных из access логов веб-сервера Apache в базу данных.</li>
  <li>Просмотр сохраненных данных в базе данных с возможностью группировки по IP и дате, а также выборки по промежутку дат.</li>
  <li>Предоставление API для получения данных в формате JSON с возможностью фильтрации и группировки по IP.</li>
  <li>Конфигурация приложения через файл настроек, включающая путь к логам, маску файлов и другие параметры.</li>
  <li>Функция авторизации пользователей, хранение пользователей в базе данных.</li>
</ol>

<h2> Использование: </h2>
<ol>
  <li>Установите Postgresql, создайте бд для работы</li>
  <li>
    Проверьте наличие библиотек:
    <ul>
      <li>re</li>
      <li>time</li>
      <li>logging</li>
      <li>yaml</li>
      <li>json</li>
      <li>datetime</li>
      <li>schedule</li>
      <li>pathlib</li>
      <li>sqlalchemy</li>
    </ul>
  </li>
  <li>
    Настройка config.yml:
    <dl>
      <dt>path:</dt>
      <dd>
        full_folder_path: полный путь до папки с логами (/var/logs)<br>
        mask: строка, которая содержится в названии файла (access.log)
      </dd>
    </dl>
    <dl>
      <dt>json:</dt>
      <dd>save_folder_path: полный путь до папки, в которую сохранятся логи.json</dd>
    </dl>
    <dl>
      <dt>cron:</dt>
      <dd>
        fstate: true - включен, false - выключен<br>
        repeat_minutes: повторение через n минут (1)
      </dd>
    </dl>
    <dl>
      <dt>file:</dt>
      <dd>
        access.log: 21<br>
        access.log.1: 11<br>
        access.log.2: 9
      </dd>
      <dd>Этот параметр появится автоматически, число - номер строки, с которой начнется парсинг. Для перезаписи данных измените на 0.</dd>
    </dl>
    <dl>
      <dt>postgresql:</dt>
      <dd>
        username: myusername<br>
        password: mypassword<br>
        host_port: localhost:5432<br>
        db: mydatabase<br>
      </dd>
    </dl>
    <dl>
  </li>
  <li> Начало парсинга - запустите в терминале python/python3 путь_до_файла/start_parse.py</li>
  <li> Получить file.json/просмотреть данные - запустите view.py, следуйте инструкциям </li>
</ol>
