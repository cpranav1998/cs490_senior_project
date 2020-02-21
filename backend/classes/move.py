import player
import copy
class Move(object):
	def __init__(self, player):
		self.player = player

class PlacePieceMove(Move):
	def __init__(self, player, x, y, type_of_piece,game):
		super().__init__(player)
		self.x = x
		self.y = y
		self.type_of_piece = type_of_piece
		self.game = game
	def apply_move(self):
		self.game.place_piece(self.type_of_piece, self.x, self.y)
		return self.game
	def apply_move_on_copy(self):
		game_copy = copy.deepcopy(self.game)
		game_copy.place_piece(self.type_of_piece, self.x, self.y)
		return game_copy

class MoveStackMove(Move):
	def __init__(self, number, locations_to_place, x, y, game):
		super().__init__(player)
		self.number = number
		self.locations_to_place = locations_to_place
		self.x = x
		self.y = y
		self.game = game
	def apply_move(self):
		self.game.move_piece(self.number, self.locations_to_place, self.x, self.y)
		return self.game
	def apply_move_on_copy(self):
		game_copy = copy.deepcopy(self.game)
		game_copy.move_piece(self.number, self.locations_to_place, self.x, self.y)
		return game_copy




	# 	self.x = x
	# 	self.y = y
	# 	self.pieces = []

	# def get_pieces(self, top_n):
	# 	items = []
	# 	for i in range(top_n):
	# 		items.append(self.pieces.pop())
	# 	return items[::-1]
	# def add_pieces(self, pieces: piece.Piece):
	# 	if len(self.pieces)==0 or self.pieces[-1].can_be_stacked():
	# 		self.pieces.extend(pieces)
	# 	else:
	# 		raise Exception('Error: Piece cannot be stacked on')
	# def add_piece(self, piece: piece.Piece):
	# 	if len(self.pieces)==0 or self.pieces[-1].can_be_stacked():
	# 		self.pieces.append(piece)
	# 	else:
	# 		raise Exception('Error: Piece cannot be stacked on')
	# def move_onto_possible(self):
	# 	return self.pieces[-1].can_be_stacked() if len(self.pieces)>0 else True
	# def place_possible(self):
	# 	return True if len(self.pieces)==0 else False
	# def owner(self):
	# 	return self.pieces[-1].get_player() if len(self.pieces)>0 else None
	# def serialize(self):
	# 	return {
	# 		'x': self.x, 
	# 		'y': self.y,
	# 		'pieces': [piece.serialize() for piece in self.pieces]
	# 	}
	# def __str__(self):
	# 	return str([str(p) for p in self.pieces])