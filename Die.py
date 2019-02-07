import random


class Die:

	def __init__(self):
		self.value = -1

	def roll(self):
		self.value = random.randint(1, 6)

	def get_value(self):
		return self.value
