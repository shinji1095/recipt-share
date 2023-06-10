from flask import Blueprint, jsonify

import calendar
from datetime import datetime

from application import db

# /*-----------------------------------------------
#    Define URL
# ------------------------------------------------*/
recipt_url = Blueprint('recipt', __name__,url_prefix='/recipt')

# /*-----------------------------------------------
#    ADD
# ------------------------------------------------*/
@recipt_url.route('/')
def get():
    docs = db.collection('recipt').stream()
    sum_value = 0
    for doc in docs:
        sum_value += int(doc.to_dict()['value'])
    return jsonify({'message':'statusOK', 'data':{'sum_value':sum_value}}), 200

@recipt_url.route("/user/<username>/value/<value>", methods=["POST"])
def add_recipt(username, value):
    db.collection('recipt').add({
        'name': username,
        'value': int(value),
        'timestamp':datetime.now()
    })
    return jsonify({'message':'statusOK'}), 200

# /*-----------------------------------------------
#    GET
# ------------------------------------------------*/
@recipt_url.route('/user/<username>/month/<month>')
def get_recipt_this_month(username, month):
    month = int(month)
    year  = datetime.now().year
    start = 1
    last  = calendar.monthrange(year, month)[1]

    start_date = datetime(year, month, start)
    end_date   = datetime(year, month, last)

    docs = db.collection('recipt').where('name','==',username).where('timestamp', '>=', start_date).where('timestamp','<=',end_date).stream()
    sum_value = 0
    for doc in docs:
        sum_value += doc.to_dict()['value']
    return jsonify({'message':'statusOK', 'data':{'sum_value':sum_value}}), 200