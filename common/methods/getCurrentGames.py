import requests
from typing import List
from common.classes.game import Game
from dotenv import load_dotenv
import os
load_dotenv()
API_URL = os.getenv("API_URL")
API_PASWORD = os.getenv("API_PASSWORD")

def getTodayGames():
    result = requests.get(API_URL+'/games', timeout=5)
    games: List[Game] = result.json()
    return games

def getCurrentGames():
    result = requests.get(API_URL+'/games', timeout=5)
    games: List[Game] = result.json()
    current=[]
    for game in games:
        if  isBeingPlayed(game):
            current.append(game)
    return current

def getGameById(match_id:int):
    result = requests.get(API_URL+'/season/'+str(match_id), timeout=5)
    game: Game =result.json()
    return game

def isBeingPlayed(game: Game):
    return game["status"]["short"]=="S1" or game["status"]["short"]=="S2" or game["status"]["short"]=="S3" or game["status"]["short"]=="S4" or game["status"]["short"]=="S5"