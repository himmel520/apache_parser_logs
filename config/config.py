import yaml


def get_config_data():
    try:
        with open('config/config.yml', 'r') as file:
            config = yaml.safe_load(file)

        return config
    except (FileNotFoundError, OSError) as e:
        print(f'Ошибка пути при чтении {e}')


def dump_config_data(config):
    try:
        with open('config/config.yml', 'w') as file:
            yaml.safe_dump(config, file, sort_keys=False)
    except (FileNotFoundError, OSError) as e:
        print(
            f'Ошибка пути при чтении {e}\nИзмените данные вручную\n{config["file"]}')
