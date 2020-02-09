from player import *
from board import *
class Game:
	def __init__(self, type_of_game, size):
		if type_of_game == "Human-Human":
			self.players = [HumanPlayer(21,1),HumanPlayer(21,1)]
		elif type_of_game == "Human-Computer":
			self.players = [HumanPlayer(21,1),ComputerPlayer(21,1)]
		elif type_of_game == "Computer-Computer":
			self.players = [ComputerPlayer(21,1),ComputerPlayer(21,1)]
		self.board = Board(size)
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


