from flask import  (
    request, 
    abort, 
    Blueprint,
    jsonify
    )


from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from config import (
    CHANNEL_SECRET,
    CHANNEL_ACCESS_TOKEN,
)

linebot_url = Blueprint("linebot", __name__, '/linebot')

# -------------------------- LINE Bot Init --------------------------
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)



# -------------------------- LINE Bot Callback --------------------------
@linebot_url.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    linebot_url.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return jsonify({'message':'statusOK'}), 200


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))