# telegramWeatherBot

<div align="center">
  <div>
    A bot for obtaining short term weather reports from multiple sources
  </div>
  <br/>
  <div>
    <img src="https://github.com/rua-iri/telegramWeatherBot/assets/117874491/358d0708-1ff9-4aed-a723-c9c465654a71" alt="telegramWeatherBot logo" width="35%" style="border-radius: 15%" />
  </div>
</div>



## Setup


```bash
git clone https://github.com/rua-iri/telegramWeatherBot.git

cd telegramWeatherBot

python3 -m venv .venv

source .venv

pip3 install -r requirements.txt

mkdir telegram_weather_bot/data

touch .env

```


Add the the Telegram Bot token and any required api keys for the weather

```
TOKEN=<telegram_token_here>

API_KEY=<api_key_here>
```


Then start the bot

```
python3 telegram_weather_bot/main.py
```
