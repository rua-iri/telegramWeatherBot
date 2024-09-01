from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


user_date = Table(
    "user_date",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("date_id", Integer, ForeignKey("date.id"))
)


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String, unique=True)
    external_id = Column(Integer, unique=True)
    dates = relationship("Date", secondary=user_date, back_populates="users")


class Date(Base):
    __tablename__ = "date"
    id = Column(Integer, primary_key=True)
    date = Column(String, unique=True)
    users = Column()
    users = relationship("User", secondary=user_date, back_populates="users")
