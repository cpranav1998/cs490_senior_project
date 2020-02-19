import piece
class Location(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.pieces = []

	def get_pieces(self, top_n):
		items = []
		for i in range(top_n):
			items.append(self.pieces.pop())
		return items[::-1]
	def add_pieces(self, pieces: piece.Piece):
		if len(self.pieces)==0 or self.pieces[-1].can_be_stacked():
			self.pieces.extend(pieces)
		else:
			raise Exception('Error: Piece cannot be stacked on')
	def add_piece(self, piece: piece.Piece):
		if len(self.pieces)==0 or self.pieces[-1].can_be_stacked():
			self.pieces.append(piece)
		else:
			raise Exception('Error: Piece cannot be stacked on')
	def move_onto_possible(self):
		return self.pieces[-1].can_be_stacked() if len(self.pieces)>0 else True
	def place_possible(self):
		return True if len(self.pieces)==0 else False
	def owner(self):
		return self.pieces[-1].get_player() if len(self.pieces)>0 else None
	def serialize(self):
		return {
			'x': self.x, 
			'y': self.y,
			'pieces': [piece.serialize() for piece in self.pieces]
		}
	def __str__(self):
		return str([str(p) for p in self.pieces])