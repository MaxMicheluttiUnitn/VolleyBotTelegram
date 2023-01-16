from common.classes.game import Game
from common.classes.user import User
from common.methods.gameToString import gameToString
from common.methods.getCurrentGames import getGameById
from common.methods.getMatchFromTeams import getMatchFromTeams, getMatchTeams
from common.methods.getUser import addFollowing, addUser, changeSupport, getSupported, getUser, removeUser, isSubscribed
from common.methods.sendMessage import sendMessage

def doSubscription(chat_id: int, args: str, token: str):
    if isSubscribed(chat_id,token):
        sendMessage(chat_id,"You are already subscribed")
    else:
        addUser(chat_id, args, token)
        sendMessage(chat_id,"You are now subscribed. Welcome to our bot!")

def unsubscribe(chat_id: int, token: str):
    if not isSubscribed(chat_id,token):
        sendMessage(chat_id,"You are not subscribed")
    else:
        removeUser(chat_id, token)
        sendMessage(chat_id,"You are now unsubscribed")

def doSupport(chat_id:int, args:str, token:str):
    if not isSubscribed(chat_id, token):
        sendMessage(chat_id,"You need to subscribe to support a team. Subscribe and support now with /subscribe [team]")
    else:
        new_support = changeSupport(chat_id,args,token)
        if new_support==None:
            sendMessage(chat_id,"You are now not supporting any team")
        else:
            sendMessage(chat_id,"You are now supporting "+new_support)

def doWhoSupport(chat_id:int, token:str):
    if not isSubscribed(chat_id, token):
        sendMessage(chat_id,"You need to subscribe to support a team. Subscribe and support now with /subscribe [team]")
    else:
        supports = getSupported(chat_id,token)
        if supports==None:
            sendMessage(chat_id,"You are currently not supporting any team")
        else:
            sendMessage(chat_id,"You are currently supporting "+supports)


def follow(chat_id: int, args: str, token: str):
    if not isSubscribed(chat_id,token):
        sendMessage(chat_id,"You need to subscribe to follow matches. Subscribe now with /subscribe")
    else:
        team1_id,team2_id = getMatchTeams(args)
        if team1_id==None or team2_id==None:
            sendMessage(chat_id,"Sorry, one or both the teams you provided is not in this league. You can get the list of all teams in the league by checking the /standings")
        else:
            match = getMatchFromTeams(team1_id,team2_id)
            if match==None:
                sendMessage(chat_id, "No match between the given teams was found this season")
            else:
                game: Game = getGameById(match)
                return_msg=gameToString(game)
                message_response = sendMessage(chat_id,return_msg)
                message = message_response.json()
                msg_id =message['result']['message_id']
                addFollowing(match_id=match,message_id=msg_id,chat_id=chat_id,token=token)



