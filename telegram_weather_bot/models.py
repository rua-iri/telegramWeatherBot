
from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    ForeignKey,
    Table,
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


user_date = Table(
    "user_date",
    Base.metadata,
    Column("Timestamp", TIMESTAMP, default=datetime.now()),
    Column("user_id", Integer, ForeignKey("user.user_id")),
    Column("date_id", Integer, ForeignKey("date.date_id"))
)


class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String, unique=True)
    external_id = Column(Integer, unique=True)
    dates = relationship(
        "Date", secondary=user_date, back_populates="users"
    )


class Date(Base):
    __tablename__ = "date"
    date_id = Column(Integer, primary_key=True)
    datestring = Column(String, unique=True)
    users = relationship(
        "User", secondary=user_date, back_populates="dates"
    )
