import logging
from datetime import datetime

from app.json import save_json
from db.mydb import get_data_from_db
from app.choose import get_user_choose
from config.config import get_config_data


def main():
    config = get_config_data()

    status, parametr = get_user_choose(config)
    logs = get_data_from_db(parametr, config['postgresql'])

    match status:
        case '1':
            for log in logs:
                print(log.ip, log.date, log.time, log.timezone,
                      log.request_method, log.path, log.status, log.bytes_sent)
        case '2':
            json_folder = config['json']['save_folder_path']
            save_json(logs, json_folder, parametr)


if __name__ == '__main__':
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - : %(message)s",
        level=logging.INFO
    )

    main()
