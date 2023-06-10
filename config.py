import os
import json
from dotenv import load_dotenv

from os.path import (
    join,
    dirname
)

# /*-----------------------------------------------
#    Configure dotenv
# ------------------------------------------------*/
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# -------------------------- ENV --------------------------
ENV = os.getenv('ENV')

# -------------------------- LINE BOT --------------------------
CHANNEL_SECRET       = os.environ.get("CHANNEL_SECRET")# if ENV == "deplay" else json.load(open('credentials\linebot.json'))["CHANNEL_SECRET"]
CHANNEL_ACCESS_TOKEN = os.environ.get("CHANNEL_ACCESS_TOKEN")# if ENV == 'deplay' else json.load(open('credentials\linebot.json'))["CHANNEL_ACCESS_TOKEN"]

# -------------------------- Firebase --------------------------
FIREBASE_SECRET_PATH = "/etc/secrets/firebase_secrets.json" if ENV == "deploy" else "credentials\credentials.json"