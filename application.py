
import firebase_admin
from flask import Flask
from firebase_admin import credentials, firestore

from config import FIREBASE_SECRET_PATH

# /*-----------------------------------------------
#    Define App                  
# ------------------------------------------------*/
app = Flask(__name__)

try:
    cred = credentials.Certificate(FIREBASE_SECRET_PATH)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    print(f' * Firebase is successfully connected')
except:
    import traceback
    traceback.print_exc()