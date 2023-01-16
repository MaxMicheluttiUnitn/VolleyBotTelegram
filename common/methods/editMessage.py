import requests

from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

telegram_url = 'https://api.telegram.org/bot'+BOT_TOKEN

def editMessage(chat_id: int, message_id: int, return_msg: str, parse_mode='html'):
  '''send a message to a telegram chat'''
  response = requests.post(
    telegram_url+'/editMessageText', 
    json={
      'chat_id': chat_id, 
      'message_id': message_id,
      'text': return_msg,
      'parse_mode': parse_mode
    }, timeout=5
  )
  return response