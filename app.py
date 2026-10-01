from flask import Flask, jsonify, session
from game import BlackjackGame

app = Flask(__name__)
app.secret_key = "blackjack-secret-key"
games = {}

@app.after_request #after every request run this function
def cors(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:8000"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response

def get_game():
    if "id" not in session:
        session["id"] = str(id(session))
    if session["id"] not in games:
        games[session["id"]] = BlackjackGame()
    return games[session["id"]]

@app.route("/api/new-game", methods=["POST"])
def new_game():
    game = get_game()
    game.new_game()
    return jsonify(game.state())

@app.route("/api/state")
def state():
    return jsonify(get_game().state())

@app.route("/api/hit", methods=["POST"])
def hit():
    game = get_game()
    game.hit()
    return jsonify(game.state())

@app.route("/api/stand", methods=["POST"])
def stand():
    game = get_game()
    game.stand()
    return jsonify(game.state())

if __name__ == "__main__":
    app.run(debug=True)