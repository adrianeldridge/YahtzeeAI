from Dice import Dice

class Scorer:

	def calc_score(turn, dice):
		dice_vec = self.convert(dice)





	def convert(self, dice):
		dice_vec = [0]*6
		for d in dice.dice:
			dice_vec[d.get_value() - 1] += 1

		return dice_vec
