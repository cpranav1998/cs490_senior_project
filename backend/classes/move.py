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