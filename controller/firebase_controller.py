from flask import Blueprint, jsonify

import firebase_admin
from firebase_admin import credentials, firestore

from config import (
    FIREBASE_SECRET_PATH
)

recipt_url = Blueprint('recipt', __name__,url_prefix='/recipt')

# -------------------------- Init Firebase --------------------------
cred = credentials.Certificate(FIREBASE_SECRET_PATH)
firebase_admin.initialize_app(cred)
db = firestore.client()


# -------------------------- REST API --------------------------
# -------------------------- ADD --------------------------
@recipt_url.route("/user/<username>/value/<value>/add")
def add_recipt(username, value):
    db.collection('recipt').add({
        'name': username,
        'value': value
    })
    return jsonify({'message':'statusOK'}), 200