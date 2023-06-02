from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

from flask import (
    Blueprint, 
    jsonify
)

from config import (
    CHANNEL_SECRET,
    CHANNEL_ACCESS_TOKEN,
)

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

ros_url = Blueprint('ros', __name__, url_prefix='/ros')

@ros_url.route('/message')
def send_message():
    try:
        line_bot_api.push_message('U982d176f83467bb2dc4ba5e432d81aa5', TextSendMessage(text='Parking is done'))
    except LineBotApiError as e:
        print(e)
    
    return jsonify({'message': 'statusOK'}, 200)