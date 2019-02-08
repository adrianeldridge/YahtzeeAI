from Dice import Dice

class Scorer:

	def calc_score(self, turn, dice):
		dice_vec = self.convert(dice)
		points = 0
		if turn >= 1 and turn <= 6:
			points = dice_vec[(turn - 1)] * turn
		elif turn == 7:
			if max(dice_vec) >= 3:
				points = sum(dice.get_values())
		elif turn == 8:
			if max(dice_vec) >= 4:
				points = sum(dice.get_values())
		elif turn == 9:
			if 2 in dice_vec and 3 in dice_vec:
				points = 25
		elif turn == 10 or turn == 11:
			max_run = 0
			curr_run = 0
			for d in dice_vec:
				if d != 0:
					curr_run += 1
				if d == 0:
					if curr_run > max_run:
						max_run = curr_run
					curr_run = 0
			if turn == 10 and max_run >= 4:
				points = 30
			elif turn == 11 and max_run >= 5:
				points =40
		elif turn == 12:
			if 5 in dice_vec:
				points = 50
		elif turn == 13:
			points = sum(dice.get_values())

		return points





	def convert(self, dice):
		dice_vec = [0]*6
		for d in dice.dice:
			dice_vec[d.get_value() - 1] += 1

		return dice_vec
