

SELECT_USER_DATE = """
SELECT *
FROM users
INNER JOIN user_date
ON users.id=user_date.user_id
INNER JOIN dates
ON user_date.date_id=dates.id
WHERE users.telegram_id=?
AND dates.date=?;
"""


INSERT_USER = """
INSERT OR IGNORE
INTO users
(name, username, telegram_id)
VALUES
(?, ?, ?);
"""


INSERT_DATE = """
INSERT OR IGNORE
INTO date
(date)
VALUES
(?);
"""
