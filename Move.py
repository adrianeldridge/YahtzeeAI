
class Move:

	def __init__(self, roll, to_roll, turn):
		self.roll = roll
		self.to_roll = to_roll
		self.turn = turn

	def is_roll(self):
		return self.roll
