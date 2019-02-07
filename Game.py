from ScoreSheet import ScoreSheet
from Dice import Dice
from Move import Move
from Scorer import Scorer.calc_score

class Game:

	dice = Dice(5)
	score_sheet = ScoreSheet()
	roll_num = 0
	turn_num = 0

	def __init__(self, player):
		self.player = player

	def play_game():
		while turn_num <= 13:
			dice.roll([0,1,2,3,4])
			roll_number = 1
			while roll_number <= 3:
				move = player.get_move(dice, roll_number, score_sheet)
				if(move.roll()):
					dice.roll(move.to_roll)
					roll_number += 1
				else:
					take_turn(move.turn, dice)
					break

		return score_sheet.total()


	def take_turn(turn, dice):
		points = calc_score(turn, dice)
		self.score_sheet.take_turn(turn, point)
