import logging
from datetime import datetime


def get_valid_date() -> datetime:
    while True:
        try:
            date_str = input(
                '\n\nВведите дату (Пример: 2023-01-1)'
                '\n>_ '
            )
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            logging.warning('Введите дату в формате год-месяц-день')


def is_valid_num(text: str, valid_list: list[str]) -> str:
    while True:
        num = input(text)

        if num in valid_list:
            return num
        else:
            logging.error(f'Введите число из списка: {valid_list}')


def get_user_choose(config) -> dict:
    status = is_valid_num(
        text=(
            'Выберите:'
            '\n1) Просмотр данных в консоли'
            f"\n2) Сохранить данные в json файл по пути {config['json']['save_folder_path']}"
            '\n>_ '
        ),
        valid_list=['1', '2']
    )

    parametr = is_valid_num(
        text=(
            '\nВыберите фильтр:'
            '\n1) IP'
            '\n2) дата в формате y-m-d'
            '\n3) Промежуток дат'
            '\n>_ '
        ),
        valid_list=['1', '2', '3']
    )

    return status, parametr
