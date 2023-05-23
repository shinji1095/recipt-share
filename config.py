import os
import json

# -------------------------- ENV --------------------------
ENV = os.getenv('ENV')

# -------------------------- LINE BOT --------------------------
CHANNEL_SECRET       = os.getenv("CHANNEL_SECRET")# if ENV == "deplay" else json.load(open('credentials\linebot.json'))["CHANNEL_SECRET"]
CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")# if ENV == 'deplay' else json.load(open('credentials\linebot.json'))["CHANNEL_ACCESS_TOKEN"]

# -------------------------- Firebase --------------------------
FIREBASE_SECRET_PATH = "/etc/secrets/firebase_secrets.json" if ENV == "deploy" else "credentials\credentials.json"
# FIREBASE_SECRET = json.load(open(FIREBASE_SECRET_PATH))