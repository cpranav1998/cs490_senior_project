from player import *
class Piece:
	def __init__(self, player: Player):
		self.player = player
		self.stackable = True
		self.form_bridge = True

	def get_player(self):
		return self.player

	def can_be_stacked(self):
		return self.stackable

	def can_form_bridge(self):
		return self.form_bridge

class VerticalPiece < Piece:
	def __init__(self, player: Player):
		super().__init__(player)
		self.stackable = False
		self.form_bridge = False

class HorizontalPiece < Piece:
	def __init__(self, player: Player):
		super().__init__(player)
		self.stackable = True
		self.form_bridge = True

class CapstonePiece < Piece:
	def __init__(self, player: Player):
		super().__init__(player)
		self.stackable = False
		self.form_bridge = True
