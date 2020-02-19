import board
import piece
class Player(object):
	def __init__(self, number_of_normal_pieces, number_of_capstones,name):
		self.normal_pieces = number_of_normal_pieces
		self.capstone_pieces = number_of_capstones
		self.name = name

	def place_vertical_piece(self, x, y, board: board.Board):
		if self.normal_pieces==0:
			raise Exception('Error: No pieces left')
		else:
			loc = board.get_location(x,y)
			if loc.place_possible():
				p = piece.VerticalPiece(self)
				loc.add_piece(p)
				board.update_location(x,y,loc)
				self.normal_pieces-=1
				return board
			else:
				raise Exception('Error: Invalid placement')

	def place_horizontal_piece(self, x, y, board: board.Board):
		if self.normal_pieces==0:
			raise Exception('Error: No pieces left')
		else:
			loc = board.get_location(x,y)
			if loc.place_possible():
				p = piece.HorizontalPiece(self)
				loc.add_piece(p)
				board.update_location(x,y,loc)
				self.normal_pieces-=1
				return board
			else:
				raise Exception('Error: Invalid placement')

	def place_capstone_piece(self, x, y, board: board.Board):
		if self.normal_pieces==0:
			raise Exception('Error: No pieces left')
		else:
			loc = board.get_location(x,y)
			if loc.place_possible():
				p = piece.CapstonePiece(self)
				loc.add_piece(p)
				board.update_location(x,y,loc)
				self.capstone_pieces-=1
				return board
			else:
				raise Exception('Error: Invalid placement')

	def all_next_to(self,locations_to_place, orig_x, orig_y):
		x,y = locations_to_place[0][0]
		if (x,y) not in set([(orig_x+1,orig_y),(orig_x-1,orig_y),(orig_x,orig_y+1),(orig_x,orig_y-1)]):
			return False
		for element in locations_to_place[1:]:
			next_x,next_y = element[0]
			if (next_x,next_y) not in set([(x+1,y),(x-1,y),(x,y+1),(x,y-1)]):
				return False
		return True
	def move_piece(self, x, y, number, locations_to_place, board: board.Board):
		loc = board.get_location(x,y)
		print(self.all_next_to(locations_to_place,x,y))
		print(all(board.get_location(element[0][0],element[0][1]).move_onto_possible()==True for element in locations_to_place))
		if all(board.get_location(element[0][0],element[0][1]).move_onto_possible()==True for element in locations_to_place) and self.all_next_to(locations_to_place,x,y):
			top_pieces = loc.get_pieces(number)
			for element in locations_to_place:
				x,y = element[0]
				loc_to_place_at = board.get_location(x,y)
				number_of_pieces_to_place = element[1]
				pieces_to_place = top_pieces[:number_of_pieces_to_place]
				top_pieces = top_pieces[number_of_pieces_to_place:]
				loc_to_place_at.add_pieces(pieces_to_place)
				board.update_location(x,y,loc_to_place_at)
				return board
		else:
			raise Exception('Error: Invalid placement pattern')
	def number_of_normal_pieces(self):
		return self.normal_pieces
	def number_of_capstone_pieces(self):
		return self.capstone_pieces
	def number_of_pieces(self):
		return self.normal_pieces+self.capstone_pieces
	def serialize(self):
		return {
			'name': self.name,
			'normal_pieces': self.normal_pieces,
			'capstone_pieces': self.capstone_pieces
		}
	def get_name(self):
		return self.name

class HumanPlayer(Player):
	def __init__(self, number_of_normal_pieces, number_of_capstones,name):
		super().__init__(number_of_normal_pieces, number_of_capstones,name)
		self.human = True

class ComputerPlayer(Player):
	def __init__(self, number_of_normal_pieces, number_of_capstones,name):
		super().__init__(number_of_normal_pieces, number_of_capstones,name)
		self.human = False

	def choose_move(self, board):
		pass

