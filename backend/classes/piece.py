import player
class Piece(object):
	def __init__(self, player: player.Player):
		self.player = player
		self.stackable = True
		self.form_bridge = True
		self.type = "piece"

	def get_player(self):
		return self.player

	def can_be_stacked(self):
		return self.stackable

	def can_form_bridge(self):
		return self.form_bridge

	def serialize(self):
		return {
			'player': self.player.serialize(), 
			'type': self.type
		}

class VerticalPiece(Piece):
	def __init__(self, player: player.Player):
		super().__init__(player)
		self.stackable = False
		self.form_bridge = False
		self.type = "vertical"

class HorizontalPiece(Piece):
	def __init__(self, player: player.Player):
		super().__init__(player)
		self.stackable = True
		self.form_bridge = True
		self.type = "horizontal"

class CapstonePiece(Piece):
	def __init__(self, player: player.Player):
		super().__init__(player)
		self.stackable = False
		self.form_bridge = True
		self.type = "capstone"
