# Video game. Create a charachter and make it fight
import random
from time import sleep

def character():
  cname = input("Give a name to your newborn character: ")
  print()
  ctype = input("Write the type you want to assign to your character: Choose betweeen Human, Imp, Wizard or Elf: ")
  print()
  if ctype == "human" or ctype == "Human":
    print("Congratulations!",cname,"is a Human.")
    print("Well, that's not such a great new, but yeah...")
  elif ctype == "Imp" or ctype == "imp":
    print("Congratulations!",cname,"is an Imp.")
    print("«O impious imp, be ye turned to stone»!")
  elif ctype == "Wizard" or ctype == "wizard":
    print("Congratulations!",cname,"is a Wizard.")
    print("And no, it did not went to Hogwartz")
  elif ctype == "Elf" or ctype == "elf":
    print("Congratulations!",cname,"is a Elf.")
    print("«I’m very elf-sufficient»")

def diceRoll(X):
  roll = random.randint(1, X)
  int(roll)
  return roll

def healthStats():
  healthStats = ((diceRoll(6) * diceRoll(12)) / 2) + 10
  return healthStats

def strengthStats():
  strengthStats = ((diceRoll(6) * diceRoll(12)) / 2) + 12
  return strengthStats


def menu():
  print("⚔️ Character Builder ⚔️")
  print()
  sleep(1)
  character()
  sleep(1)
  print("HEALTH: ",healthStats(),)
  print("STRENGTH: ",strengthStats(),)
  print()

while True:
  menu()
  repeat = input("Again?...")
  if repeat == "yes" or repeat == "Yes":
    print()
    os.system("clear")
    sleep(1)
    continue
  else:
    os.system("clear")
    print("Ok, bye!")
    break