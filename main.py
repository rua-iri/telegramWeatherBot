
import logging
import os
import typing
import dotenv


dotenv.load_dotenv()
TOKEN: typing.Final = os.getenv("TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
