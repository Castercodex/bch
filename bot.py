from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import (
    GetHistoryRequest,
    GetBotCallbackAnswerRequest,
)
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from time import sleep
import json, re, sys, os
import requests
from bs4 import BeautifulSoup
from telethon.sessions.config import telebot_hash, telebot_id

if not os.path.exists("session"):
    os.makedirs("session")

author = "\n \n \033[1;32mAuthor: \033[1;31mBerthjone Redely Edward \n \033[1;32mContact: \033[0;93mhttps://codex-portfolio.netlify.app \n \033[1;32mInspiration: \033[1;31mJEJEKA TUTORIAL"
banner = (
    """\033[1;36m\n +++++++++ \t \t \t   +  \t + \n +  \t  +++++++  ++++++  ++++++   +   +\n + \t | \t | +  \t \ +__       + + \033[0;31m\n +   \t | \t | +  \t / +        +   +\n ++++++++ +++++++  ++++++  ++++++  + \t +"""
    + author
)


api_id = telebot_id
api_hash = telebot_hash
phone_number = sys.argv[1]
client = TelegramClient("session/" + phone_number, api_id, api_hash)
client.connect()
c = requests.Session()
os.system("clear")
print(banner)


def wait(x):
    sys.stdout.write("\r")
    sys.stdout.write("                                                               ")
    for reminder in range(x, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(" {:2d} seconds remaining \r".format(reminder))
        sys.stdout.flush()
        sleep(1)


ua = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"
}

if not client.is_user_authorized():

    def password():
        c = requests.Session()
        if not os.path.exists(".password"):
            os.makedirs(".password")

    try:
        client.send_code_request(phone_number)
        user = client.sign_in(phone_number, input("\n\033[1;32mEnter Your Code : "))
    except SessionPasswordNeededError:
        password = input("Your 2fa Password : ")
        user = client.start(phone_number, password)
        os.system("clear")
        print(banner)
myself = client.get_me()
print("\033[1;32mWelcome To BCH mining Bot",myself.first_name, " BCH Click Bot \n")        
print("\033[1;32mPlease Wait a moment LINKS LOADING")
try:
    channel_entity = client.get_entity("@BCH_clickbot")
    channel_username = "@BCH_clickbot"
    client.send_message(entity=channel_entity, message="🖥 Visit sites")
    for i in range(5000000):
        sys.stdout.write("\n")
        sys.stdout.write("\033[1;33mWaiting for available links")
        sys.stdout.flush()

        sleep(3)
        posts = client(
            GetHistoryRequest(
                peer=channel_entity,
                limit=1,
                offset_date=None,
                offset_id=0,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0,
            )
        )
        if (
            posts.messages[0].message.find("Sorry, there are no new ads available")
            != -1
        ):
            print("\r Ads Are Out Buddy Try Again Later \n")
            client.send_message(entity=channel_entity, message="Balance")
            sleep(5)
            posts = client(
                GetHistoryRequest(
                    peer=channel_entity,
                    limit=1,
                    offset_date=None,
                    offset_id=0,
                    max_id=0,
                    min_id=0,
                    add_offset=0,
                    hash=0,
                )
            )
            message = posts.messages[0].message
            print(message)
            sys.exit()
        else:
            try:
                url = posts.messages[0].reply_markup.rows[0].buttons[0].url
                sys.stdout.write("\r")
                sys.stdout.write("[\033[0;97m\] Visit " + url)
                sys.stdout.flush()
                id = posts.messages[0].id
                r = c.get(url, headers=ua, timeout=15, allow_redirects=True)
                soup = BeautifulSoup(r.content, "html.parser")
            finally:
                pass
        if (
            soup.find("div", class_="g-recaptcha") is None
            and soup.find("div", id="headbar") is None
        ):
            sleep(2)
            posts = client(
                GetHistoryRequest(
                    peer=channel_entity,
                    limit=1,
                    offset_date=None,
                    offset_id=0,
                    max_id=0,
                    min_id=0,
                    add_offset=0,
                    hash=0,
                )
            )
            message = posts.messages[0].message
        if (
            posts.messages[0].message.find("You must stay") != -1
            or posts.messages[0].message.find("Please stay on") != -1
        ):
            sec = re.findall("([\\d.]*\\d+)", message)
            wait(int(sec[0]))
            sleep(1)
            posts = client(
                GetHistoryRequest(
                    peer=channel_entity,
                    limit=2,
                    offset_date=None,
                    offset_id=0,
                    max_id=0,
                    min_id=0,
                    add_offset=0,
                    hash=0,
                )
            )
            msg = posts.messages[1].message
            sleep(2)
            sys.stdout.write("" + msg + "\n")
        else:
            pass
        if soup.find("div", id="headbar") is not None:
            for data_object in soup.find_all("div", class_="container-fluid"):
                code = data_object.get("data-code")
                timer = data_object.get("data-timer")
                token = data_object.get("data-token")
                wait(int(timer))
                r = c.post(
                    "https://dogeclick.com/reward",
                    data={"code": code, "token": token},
                    headers=ua,
                    timeout=15,
                    allow_redirects=True,
                )
                js = json.loads(r.text)
                sys.stdout.write(
                    "\r You earned " + js["reward"] + " BCH for visiting a site!"
                )
        else:
            pass
           

finally:
    client.disconnect()


# 🤖 Message bots
