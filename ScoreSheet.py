
class ScoreSheet:

	def __init__(self):
		self.sheet = [-1]*14

	def take_turn(self, turn, points):
		self.sheet[turn] = points

	def total(self):
		total = sum(self.sheet)
		if sum(self.sheet[1:7]) >= 63:
			total += 35
		self.sheet[0] = total
		return total
