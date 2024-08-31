
import dotenv
import sqlite3

from .constants import DB_NAME
from .queries import SELECT_USER_DATE
from .classes.user import User

dotenv.load_dotenv()

con = sqlite3.Connection(database=DB_NAME)


def check_user_valid(user_data: User) -> bool:
    cur = con.cursor()
    res = cur.execute(SELECT_USER_DATE)
    res.fetchall()

    if len(res) > 0:
        return False
