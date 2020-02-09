from location import *

class Board:
	def __init__(self, size):
		self.locations = [[Location(x,y,size) for y in range(size)] for x in range(size)]
		self.size = size
	def get_location(self, x, y):
		return self.locations[x][y]
	def update_location(self, x, y, loc):
		self.locations[x][y] = loc
	def get_size(self):
		return self.size
	def free(self):
		total_free = 0
		for x in range(self.size):
			for y in range(self.size):
				if self.locations[x][y].owner()==None:
					total_free+=1
		return total_free
