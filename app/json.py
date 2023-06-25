import json
import logging
from pathlib import Path
from datetime import datetime


parametrs = {
    '1': 'ip',
    '2': 'date',
    '3': 'between'
}


def save_json(logs: list, path: str, parametr: str):
    date_now = datetime.now().date()

    log_dump = []
    for log in logs:
        log_dump.append(
            {
                'id': log.id,
                'ip': log.ip,
                'date': str(log.date),
                'time': str(log.time),
                'timezone': log.timezone,
                'request_method': log.request_method,
                'path': log.path,
                'status': log.status,
                'bytes_sent': log.bytes_sent
            }
        )

    try:
        with open(Path(path) / f'{parametrs[parametr]}_{str(date_now)}.json', 'w') as fp:
            json.dump(log_dump, fp, ensure_ascii=True, indent=4)
    except Exception as e:
        logging.error(e)
