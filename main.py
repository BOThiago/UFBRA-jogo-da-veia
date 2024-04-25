from flask import Flask, render_template
from src.controllers.game import gameController

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

app.register_blueprint(gameController, url_prefix="/game")

if __name__ == '__main__':
    app.run(debug=True)