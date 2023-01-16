from typing import List
from common.classes.user import User
from common.methods.editMessage import editMessage
from common.methods.getCurrentGames import getTodayGames
from common.methods.getUser import getUsers
from common.classes.game import Game
from common.methods.gameToString import gameToString


def updateFollowing(token:str):
    today: List[Game] = getTodayGames()
    users: List[User] = getUsers(token)
    for user in users:
        chat_id = user['chat_id']
        followings = user['following']
        for follow in followings:
            match_id = follow['match_id']
            game:Game = getMatchFromId(today, match_id)
            if game!=None:
                msg_id = follow['message_id']
                return_msg = gameToString(game)
                editMessage(chat_id,msg_id,return_msg)

def getMatchFromId(games: List[Game], id: int):
    for game in games:
        game_id = game['id']
        if game_id == id:
            return game
    return None