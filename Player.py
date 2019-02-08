from Game import Game
from Move import Move
from Dice import Dice
from ScoreSheet import ScoreSheet
from Scorer import Scorer
import itertools
import math

class Player:

	def __init__(self, name):
		self.name = name
		self.possible_rolls = [[0], [1], [2], [3], [4]]
		for i in range(2, 6):
			self.possible_rolls += list(itertools.combinations([0,1,2,3,4],i))

	
	def get_move(self, dice, roll_number, score_sheet):
		return self.dfs_simple_driver(dice, roll_number, score_sheet)

	
	def random_test(self, dice, roll_number, score_sheet):
		scorer = Scorer()
		if roll_number < 3:
			move = Move(True, [2, 4], -1)
		else:
			max_val = -1
			max_turn = 0
			for t in range(1,14):
				if score_sheet.sheet[t] == -1:
					score = scorer.calc_score(t, dice)
					if score > max_val:
						max_val = score
						max_turn = t

			move = Move(False, [], max_turn)

		return move


	def dfs_simple_driver(self, dice, roll_number, score_sheet):
		max_val, max_turn = self.dfs_simple(dice, roll_number, score_sheet)
		if type(max_turn) in [list, tuple]:
			move = Move(True, max_turn, -1)
		else:
			move = Move(False, [], max_turn)

		return move
		

	def dfs_simple(self, dice, roll_number, score_sheet):
		max_val, max_turn = self.select_max_move(dice, score_sheet)
		if roll_number >= 3:
			return max_val, max_turn
		else:
			for dice_rolled in self.select_possible_moves(dice, score_sheet):
				scores = []
				for i in range(20):
					new_dice = dice.clone()
					new_dice.roll(dice_rolled)
					score, _ = self.dfs_simple(new_dice, (roll_number + 1), score_sheet)
					scores += [score]

				score = sum(scores)/len(scores)
				if score > max_val:
					max_val = score
					max_turn = dice_rolled

			return max_val, max_turn


	def select_possible_moves(self, dice, score_sheet):
		n = 20
		selected_moves = dict()
		for move in range(len(self.possible_rolls)):
			score = 0
			for i in range(n):
				new_roll = dice.clone()
				new_roll.roll(self.possible_rolls[move])
				max_val, _ = self.select_max_move(new_roll, score_sheet)
				score += max_val
			score /= n
			selected_moves[move] = score
			
		moves = list(sorted(selected_moves, key = selected_moves.get, reverse = True))[0:3]
		selected = [self.possible_rolls[s] for s in moves]
		return selected


	def select_max_move(self, dice, score_sheet):
		scorer = Scorer()
		max_val = -100
		max_turn = 0
		for t in range(1,14):
			if score_sheet.sheet[t] == -1:
				score = scorer.calc_score(t, dice)
				if t >= 1 and t <= 6:
					adjust = math.copysign(math.pow((((score - (3 * t)) / 63.0) * 35), 2), (score - (3 * t)))
					score += adjust
				if t == 13:
					turns_taken = sum([0 if i == -1 else 1 for i in score_sheet.sheet])
					score = ((turns_taken + 1) / 13) * score
				if score > max_val:
					max_val = score
					max_turn = t



		return max_val, max_turn


