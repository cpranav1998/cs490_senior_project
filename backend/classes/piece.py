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
	def __str__(self):
		return "P"+self.player.get_name()[0]

class VerticalPiece(Piece):
	def __init__(self, player: player.Player):
		super().__init__(player)
		self.stackable = False
		self.form_bridge = False
		self.type = "vertical"
	def __str__(self):
		return "V"+self.player.get_name()[0]

class HorizontalPiece(Piece):
	def __init__(self, player: player.Player):
		super().__init__(player)
		self.stackable = True
		self.form_bridge = True
		self.type = "horizontal"
	def __str__(self):
		return "H"+self.player.get_name()[0]

class CapstonePiece(Piece):
	def __init__(self, player: player.Player):
		super().__init__(player)
		self.stackable = False
		self.form_bridge = True
		self.type = "capstone"
	def __str__(self):
		return "C"+self.player.get_name()[0]
