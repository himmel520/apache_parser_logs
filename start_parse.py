import time
import logging

import schedule

from db.mydb import update_db
from app.parse import get_log_paths, parse_file, read_file
from config.config import get_config_data, dump_config_data


def main():
    try:
        config = get_config_data()
        db_config = config['postgresql']

        folder = config['path']['full_folder_path']
        mask = config['path']['mask']

        for path in get_log_paths(folder, mask):
            file_name = path.name

            if not config.get('file'):
                config['file'] = {file_name: 0}
            else:
                if not config['file'].get(file_name):
                    config['file'][file_name] = 0

            logging.info(f"START PARSING {str(path)}")
            re_data, config = parse_file(read_file(path), file_name, config)

            dump_config_data(config)

            if re_data:
                update_db(re_data, db_config)

    except TypeError:
        ...
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - : %(message)s",
        level=logging.INFO
    )
    main()

    cron = get_config_data()['cron']
    if cron['state']:
        schedule.every(cron['repeat_minutes']).minutes.do(main)

        while True:
            schedule.run_pending()
            time.sleep(1)
