from common.classes.standings import StandingsItem
from common.methods.getStandings import getStandings
from common.methods.sendMessage import sendMessage
from typing import List
from common.classes.game import Game


def doStandings(chat_id: str, token: str):
    standings: List[StandingsItem] = getStandings()
    return_msg='''Standings:'''
    pos=1
    for team in standings:
        return_msg+=f'''
{pos}   {team["team"]["name"]}  {team["points"]}'''
        pos+=1
        
    sendMessage(chat_id,return_msg)
