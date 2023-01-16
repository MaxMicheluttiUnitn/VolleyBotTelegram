import requests
from typing import List
from common.classes.game import Game, Team
from common.classes.user import User
from dotenv import load_dotenv
import os
load_dotenv()
API_URL = os.getenv("API_URL")
API_PASWORD = os.getenv("API_PASSWORD")

def getUser(chat_id: int, token: str):
    result = requests.get(API_URL+'/users/'+str(chat_id), headers={"token": token})
    user: User = result.json()
    return user

def getUsers(token: str):
    result = requests.get(API_URL+'/users', headers={"token": token})
    users: List(User) = result.json()
    return users

def removeUser(chat_id: int, token: str):
    result = requests.delete(API_URL+'/users/'+str(chat_id), headers={"token": token})
    return result

def addUser(chat_id: int, args: str, token: str):
    result = requests.get(API_URL+'/team')
    teams: List[Team] = result.json()
    support=None
    if args!="":
        for team in teams:
            team_name: str=team['name']
            team_name= team_name.strip().casefold()
            team_support = args.strip().casefold()
            if team_support in team_name:
                support=team['id']
                break
    user = requests.post(API_URL+'/users', headers={"token": token}, json={
        'chat_id': chat_id,
        'supports_team': support
    })

def isSubscribed(chat_id:int, token:str):
    result = requests.get(API_URL+'/users/'+str(chat_id), headers={"token": token})
    return result.status_code == 200

def changeSupport(chat_id: int, args: str, token: str):
    result = requests.get(API_URL+'/team')
    teams: List[Team] = result.json()
    support=None
    support_name=None
    if args!="":
        for team in teams:
            team_name: str=team['name']
            team_name_stripped :str= team_name.strip().casefold()
            team_support :str= args.strip().casefold()
            if team_support in team_name_stripped:
                support=team['id']
                support_name=team_name
                break
    user = requests.put(API_URL+'/users/'+str(chat_id), headers={"token": token}, json={
        'supports_team': support
    })
    return support_name

def getSupported(chat_id: int, token: str):
    user = getUser(chat_id,token)
    team_id=user['supports_team']
    if team_id!=None:
        team_res = requests.get(API_URL+'/team/'+str(team_id), timeout=5)
        team :Team=team_res.json()
        return team['name'] 
    else:
        return None

def addFollowing(match_id: int, message_id: int, chat_id: int, token: str):
    user = requests.post(API_URL+'/follow', headers={"token": token}, json={
        'chat_id': chat_id,
        'follow': {
            'match_id': match_id,
            'message_id': message_id
        }
    }, timeout=5)
