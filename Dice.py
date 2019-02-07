from Die import Die

class Dice:	

	def __init__(self, n):
		self.dice = [Die() for i in range(n)]

	def roll(self, dice_to_roll):
		for index in dice_to_roll:
			self.dice[index].roll()

	def print_dice(self):
		print [d.get_value() for d in self.dice]
	
