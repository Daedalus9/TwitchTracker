import requests
from datetime import datetime

def search():
    us = open("list.txt", "r")
    print("Inizio analisi il " + str(datetime.now()))
    for line in us:
        url = "https://tmi.twitch.tv/group/user/"+line.lower()[:-1]+"/chatters"
        r=requests.get(url).json()
        chat=r.get('chatters')['viewers']
        st = open("list.txt", "r")
        for user in st:
            if(user[:-1] in chat):
                print(user[:-1] + " sta guardando " + line[:-1])
        st.close()
    us.close()
    print("Fine analisi il " + str(datetime.now()))