import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
import sys
sys.path.append("./classes")
from classes import *
app = flask.Flask(__name__)
cors = CORS(app)

app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'

game = None
game_running = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Tak Backend API</h1>"

@app.route('/api/v1/new_game', methods=['GET'])
@cross_origin()
def new_game():
	try:
		global game
		global game_running
		if 'type_of_game' in request.args:
			type_of_game = request.args['type_of_game']
			p1_name = request.args['p1_name']
			p2_name = request.args['p2_name']
		else:
			return jsonify({"error":"Error: No game type provided"})
		if type_of_game=="Human-Human":
			game = HumanHumanGame(5,p1_name,p2_name)
		elif type_of_game=="Human-Computer":
			game = HumanComputerGame(5,p1_name,p2_name)
		elif type_of_game=="Computer-Computer":
			game = ComputerComputerGame(5,p1_name,p2_name)
		else:
			return jsonify({"error":"Error: Invalid Type of Game"})
		print(str(game))
		print(game.get_turn())
		return jsonify(game.serialize())
	except Exception as e:
		return jsonify({"error": str(e)})
	

@app.route('/api/v1/move', methods=['GET'])
@cross_origin()
def make_move():
	try:
		global game
		global game_running
		if game_running==False:
			raise Exception('Error: Game Over')
		if "player" in request.args:
			if "place_piece" in request.args:
				x = int(request.args["x"])
				y = int(request.args["y"])
				type_of_piece = request.args["type_of_piece"]
				game.place_piece(type_of_piece, x, y)
				print(str(game))
				print(game.get_turn())
				return jsonify(game.serialize())
			elif "move_stack" in request.args:
				x = int(request.args["x"])
				y = int(request.args["y"])
				locations_to_place_raw = request.args["locations_to_place"]
				locations_to_place = []
				for row in locations_to_place_raw.split("n"):
					locs_raw = row.split(",")
					locations_to_place.append([(int(locs_raw[0]),int(locs_raw[1])),int(locs_raw[2])])
				# locations_to_place = [(int(locs_raw[0]),int(locs_raw[1])),int(locs_raw[2])]
				print(locations_to_place)
				number = int(request.args["number"])
				game.move_piece(number, locations_to_place, x, y)
				print(str(game))
				print(game.get_turn())
				return jsonify(game.serialize())
			else:
				return jsonify({"error":"Error: Invalid Move"})
		else:
			return jsonify({"error":"Error: Invalid Player"})
	except Exception as e:
		return jsonify({"error": str(e)})

@app.route('/api/v1/computer_move', methods=['GET'])
@cross_origin()
def computer_move():
	try:
		global game
		global game_running
		game = game.choose_computer_move().apply_move()
		return jsonify(game.serialize())
	except Exception as e:
		return jsonify({"error": str(e)})

@app.route('/api/v1/game_won', methods=['GET'])
@cross_origin()
def game_won():
	try:
		global game
		global game_running
		winner = game.winner()
		if winner!=None:
			game_running = False
		return jsonify({"player_name": winner.get_name() if winner != None else "RUNNING"})
	except Exception as e:
		return jsonify({"error": str(e)})

app.run()