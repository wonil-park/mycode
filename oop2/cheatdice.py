from random import randint
import sys

class Player:
  def __init__(self):
    self.dice = []

  def roll(self):
    self.dice = [] # clears current dice
    for i in range(3):
      self.dice.append(randint(1,6))

  def get_dice(self):
    return self.dice

class Cheat_Swapper(Player):
  def cheat(self):
    self.dice[-1] = 6

class Cheat_Loaded_Dice(Player):
  def cheat(self):
    self.dice = [randint(4,6) if roll < 6 else roll for roll in self.dice]

class Cheat_Ultimate(Player):
  def cheat(self):
    self.dice = [6 if roll < 6 else roll for roll in self.dice]
    # for i, roll in enumerate(self.dice):
    #   if roll < 6:
    #     self.dice[i] = 6