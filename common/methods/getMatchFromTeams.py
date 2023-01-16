import requests
from typing import List
from common.classes.game import Game, Team
from common.classes.user import User
from dotenv import load_dotenv
import os
load_dotenv()
API_URL = os.getenv("API_URL")
API_PASWORD = os.getenv("API_PASSWORD")

def getTeamId(name: str):
    result = requests.get(API_URL+'/team', timeout=5)
    teams: List[Team] = result.json()
    found=None
    name = name.strip().casefold()
    if name!="":
        for team in teams:
            team_name: str=team['name']
            team_name_stripped :str= team_name.strip().casefold()
            if name in team_name_stripped:
                found=team['id']
                break
    return found

def getMatchFromTeams(team1:int,team2:int):
    games1_res = requests.get(API_URL+'/team/'+str(team1)+'/games', timeout=5)
    games1: List[Game] = games1_res.json()
    match_id=None
    for game in games1:
        away_id = game['teams']['away']['id']
        if away_id == team2:
            match_id = game['id']
            break
    return match_id

def getMatchTeams(args: str):
    teams = args.split("-")
    team1 = getTeamId(teams[0])
    team2 = getTeamId(teams[1])
    return team1,team2