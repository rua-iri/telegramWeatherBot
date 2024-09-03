from importlib import resources
import time
from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    ForeignKey,
    Table,
    create_engine
)
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


user_date = Table(
    "user_date",
    Base.metadata,
    Column("Timestamp", TIMESTAMP),
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


def main():
    with resources.path("data", "database.db") as filepath:
        engine = create_engine(f"sqlite:///{filepath}")

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    current_time = int(time.time())
    user = User(
        name="Test Name",
        username=f"testusername_{current_time}",
        external_id=f"123_{current_time}"
    )
    date = Date(datestring=f"{current_time}")

    user.dates.append(date)
    date.users.append(user)
    
    print('adding user')
    session.add(user)
    session.add(date)

    print('committing')
    session.commit()


main()
