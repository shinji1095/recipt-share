from controller.firebase_controller import recipt_url
from controller.linebot_controller import linebot_url
from controller.ros_controller import ros_url
from flask import Flask

app = Flask(__name__)

app.register_blueprint(recipt_url)
app.register_blueprint(linebot_url)
app.register_blueprint(ros_url)
if __name__ == '__main__':
    app.run()