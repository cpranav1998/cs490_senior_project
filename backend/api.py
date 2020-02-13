import flask
from flask import request, jsonify
from classes import game
from classes import player
from classes import board
app = flask.Flask(__name__)
app.config["DEBUG"] = True

game = None

@app.route('/', methods=['GET'])
def home():
    return "<h1>Tak Backend API</h1>"

@app.route('/api/v1/new_game', methods=['GET'])
def new_game():
    if 'type_of_game' in request.args:
        type_of_game = request.args['type_of_game']
        p1_name = request.args('p1_name')
        p2_name = request.args('p2_name')
    else:
        return "Error: No game type provided"
    game = game.Game(type_of_game,5,p1_name,p2_name)
    return jsonify(game.serialize())

@app.route('/api/v1/move', methods=['GET'])
def make_move():
	if "player" in request.args:
		if "place_piece" in request.args:
			x = int(request.args["x"])
			y = int(request.args["y"])
			type_of_piece = request.args["type_of_piece"]
			player_index = int(request.args["player_index"])
			game.place_piece(player_index, type_of_piece, x, y)
			return jsonify(game.serialize())
		elif "move_stack" in request.args:
			x = int(request.args["x"])
			y = int(request.args["y"])
			locations_to_place = request.args["locations_to_place"]
			number = int(request.args["number"])
			player_index = int(request.args["player_index"])
			game.move_piece(player_index, number, locations_to_place, x, y)
			return jsonify(game.serialize())
		else:
			return "Error: Invalid Move"
	else:
		return "Error: Invalid Player"

@app.route('/api/v1/game_won', methods=['GET'])
def game_won():
    return game.winner().name()

app.run()