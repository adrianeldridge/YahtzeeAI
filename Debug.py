from Die import Die
from Dice import Dice
from Scorer import Scorer
from Game import Game
from Player import Player

player = Player("test")
game = Game(player)
score = game.play_game()
print "TOTAL SCORE: " + str(score)

