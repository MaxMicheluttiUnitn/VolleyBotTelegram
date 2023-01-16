
from common.classes.classes import Update
from common.methods.sendMessage import sendMessage
from common.commands import start, currentGames, currentStandings, subscribe

def parseUpdate(update: Update, token: str):
    chat_id:int = update['message']['chat']['id']
    if('text' in update['message'].keys()):
        message:str = update['message']['text']
        print(f"{chat_id} says: {message}")
        if message.startswith('/'):
            command = message.split(' ')[0].lstrip('/')
            msg_args = message.replace('/'+command, '', 1)
            try:
                execute_command(chat_id, command, msg_args, token)
            except: 
                sendMessage(chat_id,"We are sorry, but there was an error in the execution of your command, please retry later")


def execute_command(chat: int, command: str, args: str, token: str):
    if command=="start":
        start.doStart(chat,token)
    elif command=="help":
        return_msg = '''
Welcome to SDE 2023 Volleybot
Available commands:
/start: start (or restart) the bot
/help: info about the bot
/current_games: get info about the games that are played right now
/today: get info about the games scheduled for today
/standings: view the current standings
/subscribe: subscribe to the bot without supporting any team
/subscribe [team name]: subscribe to the bot supporting the chosen team
/unsubscribe: unsubscribe from the bot
/follow [home team] - [away team]: follow the match between the two teams
/support: tells you which team you are supporting
/support [team]: change team you are supporting
'''
        sendMessage(chat,return_msg)
    elif command=="current_games":
        currentGames.doCurrentGames(chat,token)
    elif command=="subscribe":
        subscribe.doSubscription(chat_id=chat, args=args, token=token)
    elif command=="unsubscribe":
        subscribe.unsubscribe(chat_id=chat, token=token)
    elif command=="today":
        currentGames.doTodayGames(chat,token)
    elif command=="standings":
        currentStandings.doStandings(chat,token)
    elif command=="support":
        if args=="":
            subscribe.doWhoSupport(chat,token)
        else:
            subscribe.doSupport(chat,args,token)
    elif command=="follow":
        subscribe.follow(chat,args,token)
    else:
        return_msg="Sorry, I don't understand this command. Type (or click) /help to see the list of the available commands"
        sendMessage(chat, return_msg)


