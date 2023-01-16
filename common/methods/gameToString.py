
from common.classes.game import Game

def gameToString(game: Game):
    away = 0
    starting = ""
    if game["status"]["short"]=="FT":
        home_set=compute_home_sets(game)
        away_set=compute_away_sets(game)
        home=game["scores"]["home"]
        away=game["scores"]["away"]
    elif game["status"]["short"]=="NS":
        home_set=""
        away_set=""
        home=0
        away=0
        starting="(starts at "+game["time"]+")"
    else:
        away=0
        if game["scores"]["away"]!=None:
            away = game["scores"]["away"]
        home = 0
        if game["scores"]["home"]!=None:
            home = game["scores"]["home"]
        current_set = home+away+1
        home_set, away_set = getSetScore(game,current_set)
    return_msg=f'''{game["status"]["long"]} {starting}
{home} - {game["teams"]["home"]["name"]}    {home_set}
{away} - {game["teams"]["away"]["name"]}    {away_set}'''
    return return_msg

def compute_home_sets(game:Game):
    total_sets:int=game["scores"]["home"]+game["scores"]["away"]
    sets=[]
    sets.append(game["periods"]["first"]["home"])
    sets.append(game["periods"]["second"]["home"])
    sets.append(game["periods"]["third"]["home"])
    if total_sets>3:
        sets.append(game["periods"]["fourth"]["home"])
    if total_sets>4:
        sets.append(game["periods"]["fifth"]["home"])
    return sets

def compute_away_sets(game:Game):
    total_sets:int=game["scores"]["home"]+game["scores"]["away"]
    sets=[]
    sets.append(game["periods"]["first"]["away"])
    sets.append(game["periods"]["second"]["away"])
    sets.append(game["periods"]["third"]["away"])
    if total_sets>3:
        sets.append(game["periods"]["fourth"]["away"])
    if total_sets>4:
        sets.append(game["periods"]["fifth"]["away"])
    return sets


def getSetScore(game: Game, set: int):
    if set<1 or set>5:
        return 0,0
    else:
        period = game["periods"]["first"]
        if set==2:
            period = game["periods"]["second"]
        elif set==3:
            period = game["periods"]["third"]
        elif set==4:
            period = game["periods"]["fourth"]
        elif set==5:
            period = game["periods"]["fifth"]
        return period["home"],period["away"]