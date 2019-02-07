
class ScoreSheet:

	def __init__(self):
		self.sheet = [0]*13

	def take_turn(turn, points):
		self.sheet[turn] = points
