import requests
from typing import List
from common.classes.standings import StandingsItem
from dotenv import load_dotenv
import os
load_dotenv()
API_URL = os.getenv("API_URL")
API_PASWORD = os.getenv("API_PASSWORD")

def getStandings():
    result = requests.get(API_URL+'/standings', timeout=5)
    games: List[StandingsItem] = result.json()
    return games