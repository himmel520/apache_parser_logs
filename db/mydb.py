import logging
from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy.inspection import inspect
from sqlalchemy import create_engine, select, and_

from .models import Logs, Base
from app.choose import get_valid_date


def check_table(engine):
    inspector = inspect(engine)

    if not inspector.has_table('Logs'):
        Base.metadata.create_all(bind=engine)
        logging.info('CREATE TABLE LOGS')


def add_rows(re_data: list[str], engine):
    with Session(engine) as session:
        for row in re_data:
            session.add(
                Logs(
                    ip=row[0],
                    date=datetime.strptime(row[1], '%d/%b/%Y').date(),
                    time=datetime.strptime(row[2], '%H:%M:%S').time(),
                    timezone=row[3],
                    request_method=row[4],
                    path=row[5],
                    status=int(row[6]),
                    bytes_sent=int(row[7])
                )
            )

        session.commit()
        logging.info('ADD DATA TO DB')


def update_db(re_data: list[str], config):
    engine = create_engine(
        f"postgresql+psycopg2://{config['username']}:{config['password']}@{config['host_port']}/{config['db']}"
    )

    check_table(engine)
    add_rows(re_data, engine)


def get_data_from_db(parametr: str, config) -> list:
    engine = create_engine(
        f"postgresql+psycopg2://{config['username']}:{config['password']}@{config['host_port']}/{config['db']}"
    )

    with Session(engine) as session:
        match parametr:
            case '1':
                ip = input('\n\nВведите ip (255.255.255.255)\n>_ ').strip()
                stmt = select(Logs).where(Logs.ip == ip)
            case '2':
                date = get_valid_date()
                stmt = select(Logs).where(Logs.date == date)
            case _:
                start_date = get_valid_date()
                end_date = get_valid_date()
                stmt = select(Logs).where(
                    and_(Logs.date >= start_date, Logs.date <= end_date))

        return [log for log in session.scalars(stmt)]
