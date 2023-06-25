import re
from pathlib import Path


def get_log_paths(folder_path: str, mask: str) -> list[Path]:
    file_paths = sorted(Path(folder_path).glob(f'*{mask}*'))
    return file_paths


def read_file(path: Path) -> list[str]:
    try:
        with open(path, encoding='utf-8') as f:
            data = f.read().split('\n')
        return data

    except (FileNotFoundError, OSError) as e:
        print(f'Ошибка пути при чтении {e}')


def parse_file(data: list[str], file_name: str, config: dict) -> tuple[list[tuple, dict]]:
    r = r'^(?P<ip>\S+) \S+ \S+ \[(?P<timestamp>\d{2}/\w+/\d{4}):(?P<time>\d{2}:\d{2}:\d{2}) (?P<timezone>[\+\-]\d{4})\] "(?P<request_method>\S+?) (?P<path>\S+?) \S+" (?P<status>\d+) (?P<bytes_sent>\d+)'

    line_num = config['file'][file_name]
    line_num += 1 if line_num != 0 else line_num

    re_data = []
    for ind, line in enumerate(data[line_num:]):
        match = re.match(r, line)
        if match:
            re_data.append(match.groups())

        config['file'][file_name] = ind

    return re_data, config
