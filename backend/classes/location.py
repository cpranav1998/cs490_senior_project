from piece import *
class Location:
	def __init__(self, x, y, carry_limit):
		self.x = x
		self.y = y
		self.carry_limit = carry_limit

	def get_pieces(self, top_n):
		items = []
		for i in range(top_n):
			items.append(self.pieces.pop())
		return items[::-1]
	def add_pieces(self, pieces: Piece):
		self.pieces.extend(pieces)
	def add_piece(self, piece: Piece):
		self.pieces.append(piece)
	def move_onto_possible(self):
		return self.pieces.can_be_stacked() and len(self.pieces)<self.carry_limit
	def place_possible(self):
		return True if len(self.pieces)==0 else False
	def owner(self):
		return self.pieces[-1].get_player() if len(self.pieces)>0 else None