from typing import List
from common.classes.user import User
from common.methods.editMessage import editMessage
from common.methods.getCurrentGames import getTodayGames
from common.methods.getUser import addFollowing, getUsers
from common.classes.game import Game
from common.methods.gameToString import gameToString
from common.methods.sendMessage import sendMessage
from common.methods.updateFollowing import getMatchFromId


def updateSubscribers(token:str):
    today: List[Game] = getTodayGames()
    users: List[User] = getUsers(token)
    for user in users:
        chat_id = user['chat_id']
        subscribed = user['supports_team']
        for game in today:
            if game['teams']['home']['id'] == subscribed or game['teams']['away']['id'] == subscribed:
                return_msg=gameToString(game)
                message_response = sendMessage(chat_id,return_msg)
                message = message_response.json()
                msg_id = message['result']['message_id']
                addFollowing(match_id=game['id'],message_id=msg_id,chat_id=chat_id,token=token)