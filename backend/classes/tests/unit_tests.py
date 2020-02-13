import unittest
import sys
sys.path.append("..")
import location
import piece
import board
import player
import game

class LocationTestCase(unittest.TestCase):
	def test_creation(self):
		raised = False
		try:
			loc = location.Location(0,0)
		except:
			raised = True
		self.assertFalse(raised, 'Exception raised')
	def test_add_get_piece(self):
		loc = location.Location(0,0)
		p = piece.VerticalPiece(None)
		loc.add_piece(p)
		self.assertEqual(loc.get_pieces(1),[p])
	def test_add_get_pieces(self):
		loc = location.Location(0,0)
		p1 = piece.HorizontalPiece(None)
		p2 = piece.VerticalPiece(None)
		loc.add_pieces([p1,p2])
		self.assertEqual(loc.get_pieces(2),[p1,p2])
	def test_move_onto_possible(self):
		loc = location.Location(0,0)
		p = piece.VerticalPiece(None)
		loc.add_piece(p)
		self.assertEqual(loc.move_onto_possible(),False)
	def test_place_possible(self):
		loc = location.Location(0,0)
		p = piece.VerticalPiece(None)
		loc.add_piece(p)
		self.assertEqual(loc.place_possible(),False)
	def test_owner(self):
		loc = location.Location(0,0)
		p = piece.VerticalPiece(None)
		loc.add_piece(p)
		self.assertEqual(loc.owner(),None)

class PieceTestCase(unittest.TestCase):
	def test_creation(self):
		raised = False
		try:
			p = piece.HorizontalPiece(None)
		except:
			raised = True
		self.assertFalse(raised, 'Exception raised')
	def test_get_player(self):
		p = piece.HorizontalPiece(None)
		self.assertEqual(p.get_player(),None)
	def test_can_be_stacked(self):
		p = piece.VerticalPiece(None)
		self.assertEqual(p.can_be_stacked(),False)
	def test_can_form_bridge(self):
		p = piece.VerticalPiece(None)
		self.assertEqual(p.can_form_bridge(),False)

class BoardTestCase(unittest.TestCase):
	def test_creation(self):
		raised = False
		try:
			b = board.Board(5)
		except:
			raised = True
		self.assertFalse(raised, 'Exception raised')	
	def test_free(self):
		b = board.Board(5)
		self.assertEqual(b.free(),25)
		b = board.Board(4)
		self.assertEqual(b.free(),16)
		b = board.Board(3)
		self.assertEqual(b.free(),9)

class PlayerTestCase(unittest.TestCase):
	def test_creation(self):
		raised = False
		try:
			p = player.Player(21,1,"red")
		except:
			raised = True
		self.assertFalse(raised, 'Exception raised')
	def test_place_vertical_piece(self):
		p = player.Player(21,1,"red")
		b = board.Board(5)
		p.place_vertical_piece(0,0,b)
		self.assertEqual(b.get_location(0,0).owner(),p)
	def test_all_next_to(self):
		p = player.Player(21,1,"red")
		locs_to_place = [[(0,0),2],[(3,3),2]]
		self.assertEqual(p.all_next_to(locs_to_place),False)
	def test_move_piece(self):
		p = player.Player(21,1,"red")
		b = board.Board(5)
		p.place_horizontal_piece(0,0,b)
		p.place_horizontal_piece(0,0,b)
		p.place_horizontal_piece(0,0,b)
		p.place_horizontal_piece(0,0,b)
		locs_to_place = [[(0,1),2],[(0,2),1]]
		raised = False
		try:
			p.move_piece(0,0,3,locs_to_place,b)
		except:
			raised = True
		self.assertFalse(raised, 'Exception raised')	
		self.assertEqual(b.free(),25-3)


class GameTestCase(unittest.TestCase):
	def test_creation(self):
		raised = False
		try:
			g = game.HumanHumanGame(5, "red", "green")
		except:
			raised = True
		self.assertFalse(raised, 'Exception raised')
	def test_winner(self):
		g = game.HumanHumanGame(5, "red", "green")
		g.place_piece(0, "Horizontal", 0, 0)
		g.place_piece(0, "Horizontal", 0, 1)
		g.place_piece(0, "Horizontal", 0, 2)
		g.place_piece(0, "Horizontal", 0, 3)
		g.place_piece(0, "Horizontal", 0, 4)
		self.assertEqual(g.winner(),g.players[0])
		g = game.HumanHumanGame(5, "red", "green")
		g.place_piece(0, "Horizontal", 0, 0)
		g.place_piece(0, "Horizontal", 1, 0)
		g.place_piece(0, "Horizontal", 2, 0)
		g.place_piece(0, "Horizontal", 3, 0)
		g.place_piece(0, "Horizontal", 4, 0)
		self.assertEqual(g.winner(),g.players[0])
	def test_majority_owner(self):
		g = game.HumanHumanGame(5, "red", "green")
		g.place_piece(0, "Horizontal", 0, 0)
		g.place_piece(0, "Horizontal", 0, 1)
		g.place_piece(0, "Horizontal", 0, 2)
		g.place_piece(0, "Horizontal", 0, 3)
		g.place_piece(0, "Horizontal", 0, 4)

		g.place_piece(1, "Horizontal", 1, 0)
		g.place_piece(1, "Horizontal", 2, 1)
		g.place_piece(1, "Horizontal", 3, 2)
		g.place_piece(1, "Horizontal", 4, 3)

		self.assertEqual(g.majority_owner(),g.players[0])

if __name__ == '__main__':
    unittest.main()