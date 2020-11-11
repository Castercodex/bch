from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from time import sleep 
import json,re,sys,os 
import requests   
from bs4 import BeautifulSoup

if not os.path.exists("session"):
    os.makedirs("session")
    print (banner)

banner = """
    '''''''''                   '''''''     --------   '''''''''      ''''''''
    //             ''''''       |              |       |              |        )   
    \\            /      \      |-----         |       | -----        | -----) 
    //           / ------ \           |        |       |              |       \
    \\          /          \     -----         |        ---------     |         \
    ''''''''''
"""

api_id = 2744021
api_hash = '4daa085139fa2f6524744e4c9c5516f1'
phone_number = sys.argv[1]
client = TelegramClient("session/"+phone_number, api_id, api_hash)
client.connect()
c = requests.Session()

def wait(x):
    sys.stdout.write("\r")
    sys.stdout.write("                                                               ")
    for remaining in range(x, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(" {:2d} seconds remaining".format(remaining))
        sys.stdout.flush()
        sleep(1)
ua={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"}

if not client.is_user_authorized():
    def password():  
        c = requests.Session()
        if not os.path.exists(".password"):
            os.makedirs(".password")
    try:
        client.send_code_request(phone_number)
        user = client.sign_in(phone_number, input('Enter Your Code : '))
    except SessionPasswordNeededError:
        passw = input("Your 2fa Password : ")
        user = client.start(phone_number,passw)
myself = client.get_me()
os.system("clear")
print(banner)
print ("Welcome To TeleBot",myself.first_name," BCH Click Bot \n")
print("Please Wait a moment this won't take long")
try:
    channel_entity=client.get_entity("@BCH_clickbot")
    channel_username="@BCH_clickbot"
    client.send_message(entity=channel_entity,message="🖥 Visit sites")
    for i in range(5000000):
        sys.stdout.write("\n")
        sys.stdout.write("                                 ")
        sys.stdout.write("\n")
        sys.stdout.write("Waiting for available links")
        sys.stdout.flush()
    
        sleep(3)
        posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
        if posts.messages[0].message.find("Sorry, there are no new ads available") != -1:    
            print ("\\n Adds Are Out Buddy Try Again Later \n")
            client.send_message(entity=channel_entity,message="Balance")
            sleep(5)
            posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
            message = posts.messages[0].message
            print (message)
            sys.exit()
        else:
            try:
                url = posts.messages[0].reply_markup.rows[0].buttons[0].url
                sys.stdout.write("\r")
                sys.stdout.write("[\033[0;97m\] Visit "+url)
                sys.stdout.flush()
                id = posts.messages[0].id
                r = c.get(url, headers=ua, timeout=15, allow_redirects=True)
                soup = BeautifulSoup(r.content,"html.parser")
            finally:
                pass    
        if soup.find("div",class_="g-recaptcha") is None and soup.find('div', id="headbar") is None:
            sleep(2)
            posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
            message = posts.messages[0].message
        if posts.messages[0].message.find("You must stay") != -1 or posts.messages[0].message.find("Please stay on") != -1:
            sec = re.findall( '([\\d.]*\\d+)', message)
            wait(int(sec[0]))
            sleep(1)
            posts = client(GetHistoryRequest(peer=channel_entity,limit=2,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
            messageres = posts.messages[1].message
            sleep(2)
            sys.stdout.write(""+messageres+"\\n")
        else:
            pass
        if soup.find('div', id="headbar") is not None:
           for dat in soup.find_all('div',class_="container-fluid"):
                code = dat.get('data-code')
                timer = dat.get('data-timer')
                tokena = dat.get('data-token')
                wait(int(timer)) 
                r = c.post("https://dogeclick.com/reward",data={"code":code,"token":tokena}, headers=ua, timeout=15, allow_redirects=True)
                js = json.loads(r.text)
                sys.stdout.write("You earned "+js['reward']+" BCH for visiting a site!")    
finally: 
    client.disconnect()



# 🤖 Message bots








