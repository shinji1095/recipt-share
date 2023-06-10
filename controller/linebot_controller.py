import re
import sys
import requests
from flask import  (
    request, 
    abort, 
    Blueprint,
    jsonify
    )


from linebot.exceptions import (
    InvalidSignatureError,
    LineBotApiError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from linebot import (
    LineBotApi, WebhookHandler
)

from config import (
    CHANNEL_ACCESS_TOKEN,
    CHANNEL_SECRET
)

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

from application import db

from datetime import datetime

# /*-----------------------------------------------
#    Define URL
# ------------------------------------------------*/
linebot_url = Blueprint('linebot', __name__,url_prefix='/linebot')


# -------------------------- LINE Bot Callback --------------------------
@linebot_url.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return jsonify({'message':'statusOK'}), 200


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # -------------------------- ユーザ情報の取得 --------------------------
    profile = line_bot_api.get_profile(event.source.user_id)
    print(' * name:', profile.display_name,', id:', profile.user_id)

    # -------------------------- メッセージによって処理を分岐 --------------------------
    message = event.message.text
    pattern_add = "登録"
    pattern_get = "合計"
    pattern_val = ".*?(\d+)"
    print(f" * message : {message}")

    if message[:2] == pattern_add:
        matched = re.match(pattern_val, message)
        value   = matched.group(1)
        print(f' * value : {value}')

        try:
            db.collection('recipt').add({
                'name': profile.display_name,
                'value': int(value),
                'timestamp':datetime.now()
            })
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='登録完了しました')
                )
        except:
            import traceback
            traceback.print_exc()
    elif message[:2] == pattern_get:
        pass
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=message))
    
    return jsonify({'message':'statusOK'}), 200