import requests
from common.classes.classes import GetUpdatesResponse

# retrieve tokens from .env file
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

telegram_url = f'https://api.telegram.org/bot{BOT_TOKEN}'

def getTelegramUpdates(last_update: int):
  r = requests.get(
      f'{telegram_url}/getUpdates',
      params={
        'offset': last_update,
        'allowed_updates':['message'],
        'timeout': 0
      }, timeout=5
    )
  response: GetUpdatesResponse = r.json()
  return response