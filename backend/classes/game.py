import player
import board
class Game(object):
	def __init__(self, size):
		# if type_of_game == "Human-Human":
		# 	self.players = [player.HumanPlayer(21,1,p1_name),player.HumanPlayer(21,1,p2_name)]
		# elif type_of_game == "Human-Computer":
		# 	self.players = [player.HumanPlayer(21,1,p1_name),player.ComputerPlayer(21,1,p2_name)]
		# elif type_of_game == "Computer-Computer":
		# 	self.players = [player.ComputerPlayer(21,1,p1_name),player.ComputerPlayer(21,1,p2_name)]
		# else:
		# 	raise Exception('Error: Invalid type of game')
		self.board = board.Board(size)
		self.turn = 1
		self.first_move = True
	def majority_owner(self):
		p1 = 0
		p2 = 0
		for x in range(self.board.get_size()):
			for y in range(self.board.get_size()):
				if self.board.get_location(x,y).owner()==self.players[0]:
					p1+=1
				elif self.board.get_location(x,y).owner()==self.players[1]:
					p2+=1
		if p1>p2:
			return self.players[0]
		elif p2>p1:
			return self.players[1]
		else:
			return self.players
	def winner(self):
		def horizontal_dfs(player,x,y,board, visited):
			if x < 0 or x >= board.get_size() or y < 0 or (x,y) in visited:
				return 0
			elif y >= board.get_size():
				return 1
			else:
				loc = board.get_location(x,y)
				if loc.owner()==player:
					directions = [(-1,0),(1,0),(0,-1),(0,1)]
					visited.add((x,y))
					for d in directions:
						ret = horizontal_dfs(player,x+d[0],y+d[1],board, visited)
						if ret == 1:
							visited.remove((x,y))
							return 1
					visited.remove((x,y))
					return 0
				else:
					return 0
		def vertical_dfs(player,x,y,board, visited):
			if y < 0 or y >= board.get_size() or x < 0 or (x,y) in visited:
				return 0
			elif x >= board.get_size():
				return 1
			else:
				loc = board.get_location(x,y)
				if loc.owner()==player:
					directions = [(-1,0),(1,0),(0,-1),(0,1)]
					visited.add((x,y))
					for d in directions:
						ret = vertical_dfs(player,x+d[0],y+d[1],board, visited)
						if ret == 1:
							visited.remove((x,y))
							return 1
					visited.remove((x,y))
					return 0
				else:
					return 0
		for x in range(self.board.get_size()):
			loc = self.board.get_location(x,0)
			if loc.owner()!=None:
				if horizontal_dfs(loc.owner(),x,0,self.board,set())==1:
					return loc.owner()
		for y in range(self.board.get_size()):
			loc = self.board.get_location(0,y)
			if loc.owner()!=None:
				if vertical_dfs(loc.owner(),0,y,self.board,set())==1:
					return loc.owner()
		if self.board.free()==0 or self.players[0].number_of_pieces()==0 or self.players[1].number_of_pieces()==0:
			return self.majority_owner() 
		return None
	def is_end(self):
		return True if self.winner()!=None else False
	def place_piece(self, type_of_piece, x, y):
		player_index = self.turn
		if self.first_move==True and player_index==0:
			self.turn = 1
			self.first_move = False
		if type_of_piece=="Vertical":
			self.board = self.players[player_index].place_vertical_piece(x,y,self.board)
		elif type_of_piece=="Horizontal":
			self.board = self.players[player_index].place_horizontal_piece(x,y,self.board)
		elif type_of_piece=="Capstone":
			self.board = self.players[player_index].place_capstone_piece(x,y,self.board)
		else:
			raise Exception('Error: Invalid type of move')
		if self.turn==1:
			self.turn = 0
		elif self.turn==0:
			self.turn = 1
	def move_piece(self, number, locations_to_place, x, y):
		player_index = self.turn
		if number > self.board.get_carry_limit():
			raise Exception('Error: Move violates carry limit')
		else:
			self.board = self.players[player_index].move_piece(x,y,number,locations_to_place, self.board)
			if self.turn==1:
				self.turn = 0
			elif self.turn==0:
				self.turn = 1
	def serialize(self):
		return {
			'player_1': self.players[0].serialize(),
			'player_2': self.players[1].serialize(),
			'board': self.board.serialize(),
			"turn": self.turn,
			"first_move": self.first_move
		}
	def get_turn(self):
		return self.turn
	def __str__(self):
		return str(self.board)

class HumanHumanGame(Game):
	def __init__(self,size,p1_name,p2_name):
		super().__init__(size)
		self.players = [player.HumanPlayer(21,1,p1_name),player.HumanPlayer(21,1,p2_name)]

class HumanComputerGame(Game):
	def __init__(self,size,p1_name,p2_name):
		super().__init__(size)
		self.players = [player.HumanPlayer(21,1,p1_name),player.ComputerPlayer(21,1,p2_name)]

class ComputerComputerGame(Game):
	def __init__(self,size,p1_name,p2_name):
		super().__init__(size)
		self.players = [player.ComputerPlayer(21,1,p1_name),player.ComputerPlayer(21,1,p2_name)]

