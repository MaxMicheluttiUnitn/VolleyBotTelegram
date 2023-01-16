from common.methods.gameToString import gameToString
from common.methods.getCurrentGames import getCurrentGames, getTodayGames
from common.methods.sendMessage import sendMessage
from typing import List
from common.classes.game import Game

def doCurrentGames(chat_id: int, token: str):
    games: List[Game]=getCurrentGames()
    return_msg:str='''--------------------------------------------------
'''
    if len(games)==0:
        sendMessage(chat_id,"No game is being played at the moment")
    else:
        for game in games:
            return_msg+=gameToString(game)+'''
--------------------------------------------------
'''
        sendMessage(chat_id,return_msg)

def doTodayGames(chat_id:int,token:str):
    games: List[Game]=getTodayGames()
    return_msg:str='''--------------------------------------------------
'''
    if len(games)==0:
        sendMessage(chat_id,"No game is scheduled for today")
    else:
        for game in games:
            return_msg+=gameToString(game)+'''
--------------------------------------------------
'''
        sendMessage(chat_id,return_msg)
    