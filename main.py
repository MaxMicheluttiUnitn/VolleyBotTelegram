import threading
import time
from common.methods.getTelegramUpdates import getTelegramUpdates
from common.methods.parseUpdate import parseUpdate
from common.methods.updateFollowing import updateFollowing
from common.methods.updateSubscribers import updateSubscribers
import schedule
import requests
from dotenv import load_dotenv
import os
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = os.getenv("API_URL")
API_PASWORD = os.getenv("API_PASSWORD")

token=""

def main():
    last_update=0
    # getting token at startup
    getToken()
    updateSubscribers(token)
    # refreshing token twice a day
    schedule.every().day.at("00:00").do(refreshToken)
    schedule.every().day.at("12:00").do(refreshToken)
    schedule.every().day.at("17:50").do(updateSubscribers,token)

    ticks=0

    while True:
        try:
            response = getTelegramUpdates(last_update)
            if len(response['result']) > 0:
                for update in response['result']:
                    new_thread = threading.Thread(target=parseUpdate, args=(update, token))
                    new_thread.start()
                    last_update = update['update_id']+1
        except:
            print("No Telegram response at tick "+str(ticks))

        time.sleep(1)
        if ticks%600==0: # try running pending every 10 minutes
            try:
                sched=threading.Thread(schedule.run_pending())
                sched.start()
            except:
                print("Error in token update")
        if ticks%20==0: # update followed matches every 60 seconds
            try:
                update =threading.Thread(updateFollowing(token))
                update.start()
            except:
                print("Error in match updates")
        ticks+=1
        print(ticks)

def refreshToken():
    thread=threading.Thread(getToken)
    thread.start()

def getToken():
    content={'password':API_PASWORD}
    res=requests.post(url=API_URL+'/login',json=content)
    response = res.json()
    global token 
    token =  response['token']

if __name__=="__main__":
    main()