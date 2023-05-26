from flask import Blueprint, jsonify

import firebase_admin
from firebase_admin import credentials, firestore

from config import (
    FIREBASE_SECRET_PATH
)

import calendar
from datetime import datetime, date

def get_last_date(year, month):
    return datetime(year, month, calendar.monthrange(year, month)[1])


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
        'value': int(value),
        'timestamp':datetime.now()
    })
    return jsonify({'message':'statusOK'}), 200

# -------------------------- GET --------------------------
@recipt_url.route('/user/<username>/month/<month>')
def get_recipt_this_month(username, month):
    month = int(month)
    year = datetime.now().year
    last_date = calendar.monthrange(year, month)[1]
    start_date = datetime(year, month, 1)
    end_date   = datetime(year, month, last_date)
    print(start_date, end_date)

    docs = db.collection('recipt').where('name','==',username).where('timestamp', '>=', start_date).where('timestamp','<=',end_date).stream()
    # docs = db.collection('recipt').order_by('value').end_at({u'value':10000}).stream()
    sum_value = 0
    for doc in docs:
        sum_value += doc.to_dict()['value']
    return jsonify({'message':'statusOK', 'data':{'sum_value':sum_value}}), 200