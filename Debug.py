from Die import Die
from Dice import Dice
from Scorer import Scorer

dice = Dice(5)
dice.roll([0,1,2,3,4])
dice.print_dice()
scorer = Scorer()
dice_vec = scorer.convert(dice)
print dice_vec
