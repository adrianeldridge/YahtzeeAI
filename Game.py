from ScoreSheet import ScoreSheet
from Dice import Dice
from Move import Move
from Scorer import Scorer

class Game:

	dice = Dice(5)
	score_sheet = ScoreSheet()
	roll_num = 1
	turn_num = 1

	def __init__(self, player):
		self.player = player

	def play_game(self):
		while self.turn_num <= 13:
			print "Scoresheet: " + str(self.score_sheet.sheet)
			print "Turn: " + str(self.turn_num)
			self.dice.roll([0,1,2,3,4])
			self.roll_number = 1
			while self.roll_number <= 3:
				print "\tRoll: " + str(self.roll_number)
				print "\t" + str(self.dice.print_dice())
				move = self.player.get_move(self.dice, self.roll_number, self.score_sheet)
				if move.is_roll():
					print "\t\troll dice: " + str(move.to_roll)
					self.dice.roll(move.to_roll)
					self.roll_number += 1
				else:
					print "\t\ttake turn: " + str(move.turn)
					self.take_turn(move.turn, self.dice)
					break

			self.turn_num += 1

		print "\n\n" + str(self.score_sheet.sheet) + "\n"
		return self.score_sheet.total()


	def take_turn(self, turn, dice):
		scorer = Scorer()
		points = scorer.calc_score(turn, dice)
		self.score_sheet.take_turn(turn, points)
