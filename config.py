from os import environ 

class Config:
    API_ID = environ.get("API_ID", "20406918")
    API_HASH = environ.get("API_HASH", "45a7cdec1a4177ffde664c2639dfa203")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7521220766:AAFxzVgfjKJHY0RX_Rc8nPvEzHqgwUWWRio") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://telegram:telegram@secondobot.ytc81fz.mongodb.net/?retryWrites=true&w=majority&appName=secondobot")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6964148334').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
