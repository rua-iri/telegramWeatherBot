
from datetime import datetime
from importlib import resources
import time
import dotenv

from constants import DB_NAME
# from classes.user import User
from models import Date, User, user_date

from sqlalchemy import Date, create_engine
from sqlalchemy.orm import (
    sessionmaker,
    declarative_base
)


dotenv.load_dotenv()

Base = declarative_base()

with resources.path("data", "database.db") as filepath:
    engine = create_engine(f"sqlite:///{filepath}")


Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

Base.metadata.create_all(engine)


def add_user(user_data: dict) -> User:
    existing_user = session.query(User).filter_by(
        username=user_data["username"]).first()

    if not existing_user:
        new_user = User(
            name=user_data["name"],
            username=user_data["username"],
            external_id=user_data["external_id"]
        )
        session.add(new_user)
        session.commit()
        return new_user

    return existing_user


def add_date(datestring: str) -> Date:
    existing_date = session.query(Date).filter_by(
        datestring=datestring).first()

    if not existing_date:
        new_date = Date(datestring=datestring)
        return new_date

    return existing_date


def add_user_date(user_data, datestring):
    user = add_user(user_data=user_data)
    date = add_date(datestring=datestring)

    if date not in user.dates:
        user.dates.append(date)
        session.commit()


def check_user_valid(user_data: User) -> bool:
    datestring = "1/2/3"
    exists_query = (
        session.query(User)
        .join(Date, User.dates)
        .filter(Date.datestring == datestring)
        .filter(User.external_id == user_data['external_id'])
    ).first()

    print(exists_query)

    if not exists_query:
        print("not exists")
        add_user_date(user_data=user_data, datestring=datestring)


def main():
    print("starting main")
    user_data = {'username': 'test_user3',
                 'name': 'test name3', 'external_id': '1234'}

    # add_user_date(user_data=user_data, datestring=datestring)
    check_user_valid(user_data=user_data)


main()
