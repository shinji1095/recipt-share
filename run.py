from application import app
from controller.firebase_controller import recipt_url
from controller.linebot_controller import linebot_url

# /*-----------------------------------------------
#    Define Blueprint
# ------------------------------------------------*/
app.register_blueprint(linebot_url)
app.register_blueprint(recipt_url)

if __name__ == "__main__":
    app.run(debug=True)