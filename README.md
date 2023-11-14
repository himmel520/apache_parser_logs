<h2>Functionality:</h2>
<ol>
  <li>Parsing and saving data from Apache web server access logs into a database.</li>
  <li>Viewing saved data in the database with the ability to group by IP and date, as well as selecting within date ranges.</li>
  <li>Providing an API to retrieve data in JSON format with the ability to filter and group by IP.</li>
  <li>Application configuration through a settings file, including log path, file masks, and other parameters.</li>
  <li>User authentication function, storing users in the database.</li>
</ol>

<h2>Usage:</h2>
<ol>
  <li>Install Postgresql and create a database for operation.</li>
  <li>
    Check the presence of libraries:
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
    Configuration in config.yml:
    <dl>
      <dt>path:</dt>
      <dd>
        full_folder_path: full path to the log folder (/var/logs)<br>
        mask: a string contained in the filename (access.log)
      </dd>
    </dl>
    <dl>
      <dt>json:</dt>
      <dd>save_folder_path: full path to the folder where logs will be saved as .json</dd>
    </dl>
    <dl>
      <dt>cron:</dt>
      <dd>
        fstate: true - enabled, false - disabled<br>
        repeat_minutes: repeat every n minutes (1)
      </dd>
    </dl>
    <dl>
      <dt>file:</dt>
      <dd>
        access.log: 21<br>
        access.log.1: 11<br>
        access.log.2: 9
      </dd>
      <dd>This parameter will appear automatically, the number is the starting line for parsing. Change to 0 to overwrite data.</dd>
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
  </li>
  <li>Start parsing - run in the terminal python/python3 path_to_file/start_parse.py</li>
  <li>Retrieve file.json/view data - run view.py, follow the instructions.</li>
</ol>
