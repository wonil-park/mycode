#!/usr/bin/env python3

from cheatdice import *

swapper = Cheat_Swapper()
improved_loaded_dice = Cheat_Loaded_Dice()
ultimate_cheater = Cheat_Ultimate()

swapper_score = 0
loaded_dice_score = 0
number_of_games = 5
game_number = 0
print("Simulation running")
print("==================")
while game_number < number_of_games:
  swapper.roll()
  improved_loaded_dice.roll()
  ultimate_cheater.roll()

  swapper.cheat()
  improved_loaded_dice.cheat()
  ultimate_cheater.cheat()
   #Remove # before print statements to see simulation running
   #Simulation takes approximately one hour to run with print
   #statements or ten seconds with print statements
   #commented out

 #print("Cheater 1 rolled" + str(swapper.get_dice()))
 #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
  if (sum(swapper.get_dice()) == sum(improved_loaded_dice.get_dice()) or sum(swapper.get_dice()) == sum(ultimate_cheater.get_dice())) or sum(improved_loaded_dice
                                                                                                                                             .get_dice()) == sum(ultimate_cheater.get_dice()):
      pass
  else:
      max(sum(swapper.get_dice()), sum(improved_loaded_dice.get_dice()), sum(ultimate_cheater.get_dice))

  if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()):
 #print("Draw!")
    pass
  elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()):
 #print("Dice swapper wins!")
   swapper_score+= 1

  else:
 #print("Loaded dice wins!")
    loaded_dice_score += 1
  game_number += 1
print("Simulation complete")
print("-------------------")
print("Final scores")
print("------------")
print("Swapper won: " + str(swapper_score))
print("Loaded dice won: " + str(loaded_dice_score))
if swapper_score == loaded_dice_score:
  print("Game was drawn")
elif swapper_score > loaded_dice_score:
  print("Swapper won most games")
else:
  print("Loaded dice won most games")
