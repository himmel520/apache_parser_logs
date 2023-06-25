from sqlalchemy import Integer, String, Date, Time
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Logs(Base):
    __tablename__ = 'Logs'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ip: Mapped[str] = mapped_column(String(16), nullable=False)
    date: Mapped[Date] = mapped_column(Date, nullable=False)
    time: Mapped[Time] = mapped_column(Time, nullable=False)
    timezone: Mapped[str] = mapped_column(String(20), nullable=False)
    request_method: Mapped[str] = mapped_column(String(20), nullable=False)
    path: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[int] = mapped_column(Integer, nullable=False)
    bytes_sent: Mapped[int] = mapped_column(Integer, nullable=False)
