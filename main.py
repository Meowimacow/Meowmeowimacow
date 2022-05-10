'''
Made by Meowmeowimacow / Meowimacow
Start date: 3-20-22
End date: -------
'''


import string
import math
import os
import sys
import time
import pickle
import random
import gzip


#Colors
Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m" 
black = "\033[0;30m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"
cyan_back = "\033[0;46m"
purple_back = "\033[0;45m"
white_back = "\033[0;47m"
blue_back = "\033[0;44m"
orange_back = "\033[0;43m"
green_back = "\033[0;42m"
pink_back = "\033[0;41m"
grey_back = "\033[0;40m"
grey = '\033[38;4;236m'
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
invisible='\033[08m'
reverse='\033[07m'
reset='\033[0m'
grey = "\x1b[90m"


def clearConsole():
  command = 'clear'
  if os.name in ('nt', 'dos'):
    command = 'cls'
  os.system(command)


class Player():
  def __init__(self, name):
    self.name = name
    self.lvl = 1
    self.exp = 0
    self.explvl = 100
    self.maxhp = 100
    self.hp = self.maxhp
    self.hpots = 0
    self.mpots = 0
    self.attack = 10 #physical
    self.mattack = 15 #mana
    self.maxmp = 100
    self.mp = self.maxmp
    self.gp = 0 #gold
    self.tr = 0 #total number of rests
    self.r = 2 #rest
    self.te = 0 #total enemies killed
    self.mis = round(self.attack / 2) - 2 #miss
    self.points = 0 #level up points
    self.bs = 0 #bs
    self.inv = [] #inventory
    self.equ = [] #equiped items
    self.swo = 0 #sword
    self.ar = 0 #armor
    self.arcls = 0 #defense
    self.mres = 0
    self.expsys = 0 


class Goblin():
  def __init__(self, name):
    self.name = name
    self.maxhp = 75
    self.hp = self.maxhp
    self.attack = 10
    self.mattack = 0
    self.gpgiv = 10
    self.expgiv = 10
    self.mis = round(self.attack / 2) - 2
    self.arcls = 2
    self.mres = 0
    self.weapon = False
    self.armor = False
GoblinIG = Goblin("Goblin")


class Skeleton():
  def __init__(self, name):
    self.name = name
    self.maxhp = 100
    self.hp = self.maxhp
    self.attack = 15
    self.mattack = 0
    self.gpgiv = 15
    self.expgiv = 15
    self.mis = round(self.attack / 2) - 2
    self.arcls = 5
    self.mres = 8
    self.weapon = False
    self.armor = False
SkeletonIG = Skeleton("Skeleton")


class Wolf():
  def __init__(self, name):
    self.name = name
    self.maxhp = 125
    self.hp = self.maxhp
    self.attack = 15
    self.mattack = 0
    self.gpgiv = 15
    self.expgiv = 15
    self.mis = round(self.attack / 2) - 1
    self.arcls = 7
    self.mres = 0
    self.weapon = False
    self.armor = False
WolfIG = Wolf("Wolf")


class Ghoul():
  def __init__(self, name):
    self.name = name
    self.maxhp = 150
    self.hp = self.maxhp
    self.attack = 30
    self.mattack = 40
    self.gpgiv = 25
    self.expgiv = 25
    self.mis = round(self.attack / 2) - 1
    self.arcls = 20
    self.mres = 40
    self.weapon = False
    self.armor = False
GhoulIG = Ghoul("Ghoul")


class Orge():
  def __init__(self, name):
    self.name = name
    self.maxhp = 250
    self.hp = self.maxhp
    self.attack = 25
    self.mattack = 0
    self.gpgiv = 35
    self.expgiv = 35
    self.mis = round(self.attack / 2)
    self.arcls = 15
    self.mres = 10
    self.weapon = False
    self.armor = False
OrgeIG = Orge("Orge")


class Mimic():
  def __init__(self, name):
    self.name = name
    self.maxhp = 150
    self.hp = self.maxhp
    self.attack = 15
    self.mattack = 20
    self.gpgiv = 50
    self.expgiv = 25
    self.mis = round(self.attack / 2) - 1
    self.arcls = 10
    self.mres = 15
    self.weapon = False
    self.armor = False
MimicIG = Mimic("Mimic")


class Slime():
  def __init__(self, name):
    self.name = name
    self.maxhp = 50
    self.hp = self.maxhp
    self.attack = 5
    self.mattack = 0
    self.gpgiv = 10
    self.expgiv = 5
    self.mis = round(self.attack / 2) - 2
    self.arcls = 0
    self.mres = 0
    self.weapon = False
    self.armor = False
SlimeIG = Slime("Slime")


class ASkeleton():
  def __init__(self, name):
    self.name = name
    self.maxhp = 200
    self.hp = self.maxhp
    self.attack = 35
    self.mattack = 0
    self.gpgiv = 15
    self.expgiv = 10
    self.mis = round(self.attack / 2)
    self.arcls = 35
    self.mres = 20
    self.weapon = False
    self.armor = False
ASkeletonIG = ASkeleton("Armored Skeleton")


class Giant():
  def __init__(self, name):
    self.name = name
    self.maxhp = 200
    self.hp = self.maxhp
    self.attack = 25
    self.mattack = 0
    self.gpgiv = 100
    self.expgiv = 50
    self.mis = round(self.attack / 2)
    self.arcls = 10
    self.mres = 20
    self.weapon = True
    self.armor = False
    self.weapgiv = "Giant Club"
GiantIG = Giant("Giant")


class Serpent():
  def __init__(self, name):
    self.name = name
    self.maxhp = 250
    self.hp = self.maxhp
    self.attack = 50
    self.mattack = 55
    self.gpgiv = 150
    self.expgiv = 150
    self.mis = round(self.attack / 2)
    self.arcls = 20
    self.mres = 25
    self.weapon = False
    self.armor = True
    self.armgiv = "Scale Armor"
SerpentIG = Serpent("Serpent")


class Glitch():
  def __init__(self, name):
    self.name = name
    self.maxhp = 100000
    self.hp = self.maxhp
    self.attack = 10000
    self.mattack = 10000
    self.gpgiv = 1000000
    self.expgiv = 1000000
    self.mis = round(self.attack / 1000)
    self.arcls = 10000
    self.mres = 10000
    self.weapon = True
    self.armor = True
    self.weapgiv = "God Slayer"
    self.armgiv = "Godly Armor"
GlitchIG = Glitch("?!2)&@")


m = 0
def smenu():
  clearConsole()
  print("   1.) Start\n\n   2.) Load\n\n   3.) Quit")
  option = input("\n--> "+Blue)
  print(reset+"")
  if option == "1" or option.lower().strip() == "start":
    main1()
  elif option == "2" or option.lower().strip() == "load":
    print("Name of the savefile?")
    savename = input("--> "+Blue)
    print(reset+"")
    if os.path.exists(savename) == True:
      clearConsole()
      with gzip.open(savename, "rb") as f:
        global PlayerIG
        PlayerIG = pickle.load(f)
      time.sleep(1)
      print(Green+"Loaded save state..."+reset)
      time.sleep(1)
      option = (" ")
      main()
    else:
      print("Couldn't find a savefile!")
      time.sleep(1)
      smenu()
  elif option == "3" or option.lower().strip() == "quit":
    sys.exit
  else:
    print("Please choose one of the options")
    time.sleep(1)
    smenu()


def main1():
  clearConsole()
  print(reset+"What is your name?")
  option = input("--> "+Blue)
  global PlayerIG
  PlayerIG = Player(option)
  print(reset+"\nDo you want to manually put points into stats, or do you want the game to auto put points into stats?")
  def s():
    print("1.) Manually")
    print("2.) Auto")
    op = input("--> "+Blue)
    if op == ("1") or op.lower().strip() == "manaully":
      PlayerIG.expsys = 1
    elif op == ("2") or op.lower().strip() == "auto":
      PlayerIG.expsys = 0
    else:
      print("Please choose one of the options")
      time.sleep(1)
      s()
  s()
  main()


def main():
  clearConsole()
  if PlayerIG.expsys == 1:
    if PlayerIG.exp >= PlayerIG.explvl:
      PlayerIG.exp -= PlayerIG.explvl
      PlayerIG.lvl +=1
      PlayerIG.explvl += 50
      PlayerIG.points = PlayerIG.points + 15
      print(Blue+"Level up!"+reset)
      print("Stat points:"+Orange, PlayerIG.points)
      print(reset+"Would you like to spend your points?")
      print("Please note that if you say no, then you can only spend your point after you level up again.")
      option = input("--> "+Blue)
      if option.lower().strip() == "yes" or option.lower().startswith("y"):
        def pointbuy():
          clearConsole()
          print(reset+"1.) Max HP + 10 per point")
          print("2.) Max MP + 10 per point")
          print("3.) Attack power + 5 per point")
          print("4.) Magic power + 5 per point")
          print("Q.) Quit")
          print("Total points avaiable:"+Orange, PlayerIG.points)
          time.sleep(1)
          print(reset+"What would you like to spend your points on?")
          option = input("--> "+Blue)
          if option.lower().strip() == "max hp" or option.lower().strip() == "hp" or option == ("1"):
            print(reset+"How many points would you like to spend?")
            option = int(input("--> "+Blue))
            if option > PlayerIG.points:
              print(reset+"Can't spend more than you have.")
            elif option == ("0"):
              print(reset+"Spend one or continue")
              time.sleep(1)
              pointbuy()
            else:
              PlayerIG.points -= option
              PlayerIG.maxhp += option * 15
              time.sleep(1)
              print(reset+"New max hp:", PlayerIG.maxhp)
              time.sleep(1)
              pointbuy()
          elif option.lower().strip() == "attack power" or option.lower().strip() == "attack" or option.lower().strip() == ("3"):
            print("How many points would you like to spend?")
            option = int(input("--> "+Blue))
            if option > PlayerIG.points:
              print(reset+"Can't spend more than you have.")
            elif option == ("0"):
              print(reset+"Spend one or continue")
              time.sleep(1)
              pointbuy()
            else:
              PlayerIG.points -= option
              PlayerIG.attack += option * 5
              time.sleep(1)
              print(reset+"New attack power:", PlayerIG.attack)
              time.sleep(1)
              pointbuy()
          elif option.lower().strip() == "magic power" or option.lower().strip() == "magic" or option.lower().strip() == ("4"):
            print("How many points would you like to spend?")
            option = int(input("--> "+Blue))
            if option > PlayerIG.points:
              print(reset+"Can't spend more than you have.")
            elif option == ("0"):
              print(reset+"Spend one or continue")
              time.sleep(1)
              pointbuy()
            else:
              PlayerIG.points -= option
              PlayerIG.mattack += option * 5
              time.sleep(1)
              print(reset+"New magic power:", PlayerIG.mattack)
              time.sleep(1)
              pointbuy()
          elif option.lower().strip() == "max mp" or option.lower().strip() == "mp" or option.lower().strip() == ("2"):
            print("How many points would you like to spend?")
            option = int(input("--> "+Blue))
            if option > PlayerIG.points:
              print(reset+"Can't spend more than you have.")
            elif option == ("0"):
              print(reset+"Spend one or continue")
              time.sleep(1)
              pointbuy()
            else:
              PlayerIG.points -= option
              PlayerIG.maxmp += option * 5
              time.sleep(1)
              print(reset+"New max mp:", PlayerIG.maxmp)
              time.sleep(1)
              pointbuy()
          elif option.lower().strip() == "quit" or option.lower().strip() == "q":
            main()
        pointbuy()
      elif option.lower().strip() == "no" or option.lower().strip().startswith("n"):
        main()
  else:
    if PlayerIG.exp >= PlayerIG.explvl:
      PlayerIG.exp -= PlayerIG.explvl
      PlayerIG.lvl += 1
      PlayerIG.explvl += 50
      PlayerIG.attack = PlayerIG.attack + 5
      PlayerIG.mattack = PlayerIG.mattack + 5
      PlayerIG.maxhp = PlayerIG.maxhp + 10
      PlayerIG.maxhp = PlayerIG.maxmp + 10
  print(reset+"Name:", PlayerIG.name)
  print("Level:", PlayerIG.lvl)
  print("Exp:"+Green, PlayerIG.exp ,"/", PlayerIG.explvl)
  print(reset+"Gold:"+Orange, PlayerIG.gp)
  print(reset+"Health:"+Red,PlayerIG.hp ,reset+"/"+Red, PlayerIG.maxhp)
  print(reset+"Mana:"+ Blue, PlayerIG.mp, reset+"/"+Blue, PlayerIG.maxmp)
  print(reset+"Defense:", PlayerIG.arcls)
  print(reset+"Magic Defense:", PlayerIG.mres)
  print(reset+"Physical Damage:", PlayerIG.attack)
  print(reset+"Magical Damage:", PlayerIG.mattack)
  print("You have rested"+cyan, PlayerIG.tr ,reset+"times")
  print("You have killed"+Red, PlayerIG.te ,reset+"enemies")
  if PlayerIG.bs >= 1:
    print("You have killed"+Red, PlayerIG.bs ,reset+"gods")
  else:
    pass
  print("Items Equiped", PlayerIG.equ)
  time.sleep(1)
  print("\nWhat would you like to do?")
  print("1.) Fight")
  print("2.) Rest")
  print("3.) Store")
  print("4.) Inventory")
  print("5.) Monster Wiki")
  print("6.) Save")
  if PlayerIG.bs >= 1:
    print("?.) Battle the Gods")
  else:
    pass
  option = input("--> "+Blue)
  print(reset+"")
  if option == "1" or option.lower().strip() == "fight":
    prefight()
  elif option == "2" or option.lower().strip() == "rest":
    rest(PlayerIG.hp, PlayerIG.mp)
  elif option == "3" or option.lower().strip() == "store":
    store()
  elif option == "4" or option.lower().strip() == "inventory":
    inventory()
  elif option == "5" or option.lower().strip() == "monster wiki" or option.lower().strip() == "monster":
    monsters()
  elif option == "6" or option.lower().strip() == "save":
    clearConsole()
    print("What name would you like the save to be?")
    savefile = input("--> "+Blue)
    print(reset+"")
    with gzip.open(savefile, "wb") as f:
      pickle.dump(PlayerIG, f)
      time.sleep(1)
      f.close()
      print("\nGame has been saved!\n")
      time.sleep(1)
      clearConsole()
      option = (" ")
      main()
  elif option == "?" or option.lower().strip() == "battle the gods" or option.lower().strip() == "gods":
    if PlayerIG.bs >= 1:
      Gods()
    else:
      clearConsole()
      print(reset+"You haven't met the requirements...")
      time.sleep(1)
      main()
  else:
    print("Please choose one of the options")
    time.sleep(1)
    main()


def inventory():
  clearConsole()
  print("Items:")
  for i in PlayerIG.inv:
    print(i)
    time.sleep(0.1)
  print("\nPotions:")
  print("Health Potions:", PlayerIG.hpots)
  print("\nWhat would you like to do?")
  print("1.) Equip")
  print("2.) Unequip")
  print("B.) Back")
  option = input("--> "+Blue)
  print(reset+"")
  if option.lower().strip() == "equip" or option == "1":
    print("1.) Sword")
    print("2.) Armor")
    print("\nWhat would you like to equip?")
    option = input("--> "+Blue)
    print(reset+"")
    if option.lower().strip() == "sword" or option == "1":
      print("What sword would you like to equip?")
      option = input("--> "+Blue)
      print(reset+"")
      if option in PlayerIG.inv:
        if option in PlayerIG.equ:
          print("You already have that item equiped!")
          time.sleep(1)
          inventory()
        elif PlayerIG.swo == 1:
          print("You already have a sword equiped!")
          time.sleep(1)
          inventory()
        else:
          if option == "Wood Sword":
            PlayerIG.attack += 5
          elif option == "Bronze Sword":
            PlayerIG.attack += 10
          elif option == "Iron Sword":
            PlayerIG.attack += 20
          elif option == "Steel Sword":
            PlayerIG.attack += 30
          elif option == "Giant Club":
            PlayerIG.attack += 35
          elif option == "God Slayer":
              PlayerIG.attack += 10000
          PlayerIG.inv.remove(option)
          PlayerIG.equ.append(option)
          PlayerIG.swo += 1
          print("You have equiped", option)
          time.sleep(1)
          inventory()
      else:
        print("Type the name of the item exactly as you see it.")
        time.sleep(1)
        inventory()
    elif option.lower().strip() == "armor" or option == "2":
        print("What armor would you like to equip?")
        option = input("--> "+Blue)
        print(reset+"")
        if option in PlayerIG.inv:
          if option in PlayerIG.equ:
            print("You already have that item equiped!")
            time.sleep(1)
            inventory()
          elif PlayerIG.ar == 1:
            print("You already have a armor equiped!")
            time.sleep(1)
            inventory()
          else:
            if option == "Wood Armor":
              PlayerIG.arcls += 5
            elif option == "Bronze Armor":
              PlayerIG.arcls += 15
            elif option == "Iron Armor":
              PlayerIG.arcls += 30
            elif option == "Steel Armor":
              PlayerIG.arcls += 40
            elif option == "Scale Armor":
              PlayerIG.arcls += 45
            elif option == "Godly Armor":
              PlayerIG.arcls += 10000
              PlayerIG.mres += 10000
            PlayerIG.inv.remove(option)
            PlayerIG.equ.append(option)
            PlayerIG.ar += 1
            print("You have equiped", option)
            time.sleep(1)
            inventory()
    else:
      print("Please choose one the options")
      time.sleep(1)
      inventory()
  elif option.lower().strip() == "unequip" or option == "2":
    print("Currently Equiped:")
    print(PlayerIG.equ)
    print("\n1.) Sword")
    print("2.) Armor")
    print("\nWhat would you like to unequip?")
    option = input("--> "+Blue)
    print(reset+"")
    if option.lower().strip() == "sword" or option == "1":
      print("\nWhat item you like to unequip?")
      option = input("--> "+Blue)
      print(reset+"")
      if option in PlayerIG.equ:
        if option == "Wood Sword":
          PlayerIG.attack -= 5
        elif option == "Bronze sword":
          PlayerIG.attack -= 10
        elif option == "Iron Sword":
          PlayerIG.attack -= 20
        elif option == "Steel Sword":
          PlayerIG.attack -= 30
        elif option == "Giant Club":
            PlayerIG.attack -= 35
        elif option == "God Slayer":
          PlayerIG.attack -= 1000
        PlayerIG.equ.remove(option)
        PlayerIG.inv.append(option)
        PlayerIG.swo -= 1
        print("You have unequiped", option)
        time.sleep(1)
        inventory()
    elif option.lower().strip() == "armor" or option == "2":
      print("\nWhat armor you like to unequip?")
      option = input("--> "+Blue)
      print(reset+"")
      if option in PlayerIG.equ:
        if option == "Wood Armor":
          PlayerIG.arcls -= 5
        elif option == "Bronze Armor":
          PlayerIG.arcls -= 15
        elif option == "Iron Armor":
          PlayerIG.arcls -= 30
        elif option == "Steel Armor":
          PlayerIG.arcls -= 40
        elif option == "Scale Armor":
              PlayerIG.attack -= 45
        elif option == "Godly Armor":
          PlayerIG.arcls -= 1000
        else:
          print("Plese choose one of the options")
          time.sleep(1)
          inventory()
        PlayerIG.equ.remove(option)
        PlayerIG.inv.append(option)
        PlayerIG.ar -= 1
        print("You have unequiped", option)
        time.sleep(1)
        inventory()
    else:
      print("Plese choose one of the options")
      time.sleep(1)
      inventory()
  elif option.lower().strip() == "b" or option.lower().strip() == "back":
    main()


def rest(hp, mp):
  clearConsole()
  if PlayerIG.hp >= PlayerIG.maxhp:
    print("You don't need to rest!")
    time.sleep(1)
    main()
  elif PlayerIG.r == 0:
    print("You can only rest twice after battle!")
    time.sleep(1)
    print("You have to win a battle in order to rest again!")
    time.sleep(2)
    main()
  elif PlayerIG.hp < PlayerIG.maxhp:
    bhp = PlayerIG.hp
    r = random.randint(10, 100)
    PlayerIG.hp += r
    ahp = PlayerIG.hp
    print("You have rested!")
    time.sleep(1)
    if PlayerIG.hp >= PlayerIG.maxhp:
      PlayerIG.hp = PlayerIG.maxhp
      ahp = PlayerIG.hp
    thp = ahp - bhp
    print("You have recovered"+Green, thp ,reset+"HP!")
    PlayerIG.r -= 1
    PlayerIG.tr += 1
    time.sleep(1)
  elif PlayerIG.mp < PlayerIG.maxmp:
    bmp = PlayerIG.mp
    rm = random.randint(10, 100)
    PlayerIG.mp += rm
    amp = PlayerIG.mp
    print("You have rested!")
    time.sleep(1)
    if PlayerIG.hp >= PlayerIG.maxhp:
      PlayerIG.hp = PlayerIG.maxhp
      amp = PlayerIG.hp
    thp = amp - bmp
    print("You have recovered"+Green, thp ,reset+"HP!")
    PlayerIG.r -= 1
    PlayerIG.tr += 1
    time.sleep(1)
  main()


def monsters():
  clearConsole()
  print(reset+"Which monster would you like to see the stats of?")
  print("Type the monster's name to get their stats")
  print("Type either B, or Back, to go back")
  time.sleep(0.1)
  print("\nGoblin")
  time.sleep(0.1)
  print("Wolf")
  time.sleep(0.1)
  print("Skeleton")
  time.sleep(0.1)
  print("Armored Skeleton")
  time.sleep(0.1)
  print("Ghoul")
  time.sleep(0.1)
  print("Mimic")
  time.sleep(0.1)
  print("Slime")
  time.sleep(0.1)
  print("Ghoul")
  time.sleep(0.1)
  print("Orge")
  time.sleep(0.1)
  print("Giant")
  time.sleep(0.1)
  print("Serpent")
  time.sleep(0.1)
  option = input("--> "+Blue)
  print(reset+"")
  if option.lower().strip() == "goblin":
    print("\nGoblin")
    print("Max Health:"+Red, GoblinIG.maxhp)
    print(reset+"Attack:"+Red, GoblinIG.attack)
    print(reset+"Magic Attack:", GoblinIG.mattack)
    time.sleep(1)
    print("Input anything to go back")
    option = input("--> "+Blue)
    if option.lower().strip() == "anything":
      print("Real funny")
      time.sleep(1)
      monsters()
    else:
      monsters()
  elif option.lower().strip() == "skeleton":
    print("\nSkeleton")
    print("Max Health:"+Red, SkeletonIG.maxhp)
    print(reset+"Attack:"+Red, SkeletonIG.attack)
    print(reset+"Magic Attack:", SkeletonIG.mattack)
    time.sleep(1)
    print("Input anything to go back")
    option = input("--> "+Blue)
    if option.lower().strip() == "anything":
      print("Real funny")
      time.sleep(1)
      monsters()
    else:
      monsters()
  elif option.lower().strip() == "ghoul":
    print("\nGhoul")
    print("Max Health:"+Red, GhoulIG.maxhp)
    print(reset+"Attack:"+Red, GhoulIG.attack)
    print(reset+"Magic Attack:", GhoulIG.mattack)
    time.sleep(1)
    print("Input anything to go back")
    option = input("--> "+Blue)
    if option.lower().strip() == "anything":
      print("Real funny")
      time.sleep(1)
      monsters()
    else:
      monsters()
  elif option.lower().strip() == "armored skeleton":
    print("\nArmored Skeleton")
    print("Max Health:"+Red, ASkeletonIG.maxhp)
    print(reset+"Attack:"+Red, ASkeletonIG.attack)
    print(reset+"Magic Attack:", ASkeletonIG.mattack)
    time.sleep(1)
    print("Input anything to go back")
    option = input("--> "+Blue)
    if option.lower().strip() == "anything":
      print("Real funny")
      time.sleep(1)
      monsters()
    else:
      monsters()
  elif option.lower().strip() == "orge":
    print("\nOrge")
    print("Max Health:"+Red, OrgeIG.maxhp)
    print(reset+"Attack:"+Red, OrgeIG.attack)
    print(reset+"Magic Attack:", OrgeIG.mattack)
    time.sleep(1)
    print("Input anything to go back")
    option = input("--> "+Blue)
    if option.lower().strip() == "anything":
      print("Real funny")
      time.sleep(1)
      monsters()
    else:
      monsters()
  elif option.lower().strip() == "ghoul":
    print("\nGhoul")
    print("Max Health:"+Red, GhoulIG.maxhp)
    print(reset+"Attack:"+Red, GhoulIG.attack)
    print(reset+"Magic Attack:", GhoulIG.mattack)
    time.sleep(1)
    print("Input anything to go back")
    option = input("--> "+Blue)
    if option.lower().strip() == "anything":
      print("Real funny")
      time.sleep(1)
      monsters()
    else:
      monsters()
  elif option.lower().strip() == "mimic":
    print("\nMimic")
    print("Max Health:"+Red, MimicIG.maxhp)
    print(reset+"Attack:"+Red, MimicIG.attack)
    print(reset+"Magic Attack:", MimicIG.mattack)
    time.sleep(1)
    print("Input anything to go back")
    option = input("--> "+Blue)
    if option.lower().strip() == "anything":
      print("Real funny")
      time.sleep(1)
      monsters()
    else:
      monsters()
  elif option.lower().strip() == "slime":
    print("\nSlime")
    print("Max Health:"+Red, SlimeIG.maxhp)
    print(reset+"Attack:"+Red, SlimeIG.attack)
    print(reset+"Magic Attack:", SlimeIG.mattack)
    time.sleep(1)
    print("Input anything to go back")
    option = input("--> "+Blue)
    if option.lower().strip() == "anything":
      print("Real funny")
      time.sleep(1)
      monsters()
    else:
      monsters()
  elif option.lower().strip() == "serpent":
    print("\nSerpent")
    print("Max Health:"+Red, SerpentIG.maxhp)
    print(reset+"Attack:"+Red, SerpentIG.attack)
    print(reset+"Magic Attack:", SerpentIG.mattack)
    time.sleep(1)
    print("Input anything to go back")
    option = input("--> "+Blue)
    if option.lower().strip() == "anything":
      print("Real funny")
      time.sleep(1)
      monsters()
    else:
      monsters()
  elif option.lower().strip() == "wolf":
    print("\nWolf")
    print("Max Health:"+Red, WolfIG.maxhp)
    print(reset+"Attack:"+Red, WolfIG.attack)
    print(reset+"Magic Attack:", WolfIG.mattack)
    time.sleep(1)
    print("Input anything to go back")
    option = input("--> "+Blue)
    if option.lower().strip() == "anything":
      print("Real funny")
      time.sleep(1)
      monsters()
    else:
      monsters()
  elif option.lower().strip() == "giant":
    print("\nGiant")
    print("Max Health:"+Red, GiantIG.maxhp)
    print(reset+"Attack:"+Red, GiantIG.attack)
    print(reset+"Magic Attack:", GiantIG.mattack)
    time.sleep(1)
    print("Input anything to go back")
    option = input("--> "+Blue)
    if option.lower().strip() == "anything":
      print("Real funny")
      time.sleep(1)
      monsters()
    else:
      monsters()
  elif option.lower().strip() == "?!2)&@" or option.lower().strip() == "glitch":
    print("\n?!2)&@")
    print("Max Health:"+Red, GlitchIG.maxhp)
    print(reset+"Attack:"+Red, GlitchIG.attack)
    print(reset+"Magic Attack:", GlitchIG.mattack)
    time.sleep(1)
    print("Input anything to go back")
    option = input("--> "+Blue)
    if option.lower().strip() == "anything":
      print("Real funny")
      time.sleep(1)
      monsters()
    else:
      monsters()
  elif option.lower().strip() == "back" or option.lower().strip().startswith("b"):
    main()
  else: 
    print("Choose one of the options")
    time.sleep(1)
    monsters()


def chest():
  clearConsole()
  c = random.randint(1, 10)
  print("You found a chest!")
  time.sleep(0.1)
  print("Do you want to open it?")
  option = input("\n--> "+Blue)
  print(reset+"")
  if option.lower().strip() == "yes" or option.lower().strip().startswith("y"):
    if c == 6 or c == 8:
      enemy = MimicIG
      print("It's a mimic!")
      time.sleep(1)
      fight()
    elif c == 7:
      print("You found a Iron Sword!")
      time.sleep(1)
      PlayerIG.inv.append("Iron Sword")
    else:
      print("It's a bunch of money!")
      time.sleep(1)
      if PlayerIG.lvl >= 1:
        m = random.randint(1, 100)
      elif PlayerIG.lvl >= 2:
        m = random.randint(2, 200)
      PlayerIG.gp += m
      print("You got"+Orange, m ,reset+"gold!")
      time.sleep(1)
      main()
  elif option.lower().strip() == "no" or option.lower().strip().startswith("n"):
    print("Perhaps it's best to not open the chest")
    time.sleep(1)
    main()
  else:
    print("Choose either yes or no")
    time.sleep(1)
    chest()
  

def prefight():
  global enemy
  op = random.randint(1, 100000)
  type = random.randint(1, 50)
  enemynum = random.randint(1, 4)
  if op == 69420:
    enemy = GlitchIG
    enemy.hp = enemy.maxhp
    glitchfight()
  else:
    if PlayerIG.lvl == 1:
      if type == 27 or type == 28 or type == 30:
        enemy = GiantIG
        enemy.hp = enemy.maxhp
        bossfight()
      elif type == 1 or type == 3:
        enemy = SerpentIG
        enemy.hp = enemy.maxhp
        bossfight()
      elif type == 7 or type == 14 or type == 21:
        chest()
      else:
        if enemynum == 1:
          enemy = GoblinIG
        elif enemynum == 2:
          enemy = SlimeIG
        elif enemynum == 3:
          enemy = WolfIG
        else:
          enemy = SkeletonIG
      enemy.hp = enemy.maxhp
      fight()
    elif PlayerIG.lvl == 2:
      if type == 7 or type == 14 or type == 21:
        chest()
      elif type == 1 or type == 3:
        enemy = SerpentIG
        enemy.hp = enemy.maxhp
        bossfight()
      else:
        if enemynum == 1: 
          enemy = SkeletonIG
        elif enemynum == 2:
          enemy = WolfIG
        elif enemynum == 3:
          enemy = OrgeIG
        else:
          enemy = GhoulIG
      enemy.hp = enemy.maxhp
      fight()
    elif PlayerIG.lvl == 3:
      if type == 7 or type == 14 or type == 21:
        chest()
      elif type == 1 or type == 3:
        enemy = SerpentIG
        enemy.hp = enemy.maxhp
        bossfight()
      else:
        if enemynum == 1: 
          enemy = GhoulIG
        elif enemynum == 2:
          enemy = SkeletonIG
        elif enemynum == 3:
          enemy = OrgeIG
        else:
          enemy = ASkeletonIG
      enemy.hp = enemy.maxhp
      fight()


def Gods():
  clearConsole()
  print("Which god?")
  print("Type B, or Back, to go back")
  time.sleep(0.1)
  print("Gl!tc4")
  time.sleep(0.1)
  print("Zeus")
  time.sleep(0.1)
  print("Cthulhu")
  time.sleep(0.1)
  print("Satan")
  time.sleep(0.1)
  print("God")
  time.sleep(0.1)
  option = input("--> "+Blue)
  if option.lower().strip() == "glitch" or option == "Gl!tch4":
    enemy = GlitchIG
    glitchfight()
  else:
    print("Choose one of the options")
    time.sleep(1)
    Gods()


def Gmagic():
  clearConsole()
  print("What spell would you like to use?")
  time.sleep(1)
  print("1.) Fire ball")
  option = input("-->"+Blue)
  print(reset+"")
  pm = PlayerIG.mattack - 5
  pm2 = PlayerIG.mattack + 5
  ma = random.randint(pm, pm2)
  em = enemy.attack - 5
  em2 = enemy.attack + 5
  ema = random.randint(pm, pm2)
  if option.lower().strip() == "fire ball" or option == "1":
    clearConsole()
    PlayerIG.mp -= 10
    pm = PlayerIG.mattack - 5
    pm2 = PlayerIG.mattack + 5
    ma = random.randint(pm, pm2)
    em = enemy.attack - 5
    em2 = enemy.attack + 5
    ema = random.randint(pm, pm2)
    if ma == pm:
      print("You miss!")
    elif ma == pm2:
      print("Critical Hit!")
      time.sleep(1)
      ma -= enemy.mres
      if ma <= 0:
        ma = 0 
      enemy.hp -= ma
      print("You deal", ma ,"to the enemy!")
      time.sleep(1)
    else:
      pattack -= enemy.arcls
    if pattack <= 0:
      pattack = 0 
    enemy.hp -= pattack
    print("You deal", pattack ,"to the enemy!")
    time.sleep(1)
    if enemy.hp <= 0:
      win(enemy.gpgiv, enemy.gpgiv)
      clearConsole()
    if ema == enemymiss:
      print("The enemy missed!")
      time.sleep(1)
    elif ema == enemy.attack + 5:
      print("The enemy did a critcal hit!")
      time.sleep(0.5)
      ema -= PlayerIG.arcls
      if ema <= 0:
        ema = 0 
      PlayerIG.hp -= ema
      print("The enemy delt", ema ,"damage to you!")
      time.sleep(1)
    else:
      ema -= PlayerIG.arcls
      if ema <= 0:
        ema = 0 
      PlayerIG.hp -= ema
      print("The enemy delt", ema ,"damage to you!")
      time.sleep(1)
    if PlayerIG.hp <= 0:
      die()
    else:
      GFight()


def Gattack(playerattack, enemyattack, playermiss, enemymiss):
  clearConsole()
  global pattack
  global eattack
  p = playermiss
  p2 = playerattack + 5
  e = enemymiss
  e2 = enemyattack + 10000 
  pattack = random.randint(p, p2)
  eattack = random.randint(e, e2)
  if pattack == playermiss:
    print("You Miss!")
  elif pattack == PlayerIG.attack + 5:
    print("Critical Hit!")
    time.sleep(0.5)
    pattack -= enemy.arcls
    if pattack <= 0:
      pattack = 0 
    enemy.hp -= pattack
    print("You deal", pattack ,"to the enemy!")
    time.sleep(1)
  else:
    pattack -= enemy.arcls
    if pattack <= 0:
      pattack = 0 
    enemy.hp -= pattack
    print("You deal", pattack ,"to the enemy!")
    time.sleep(1)
  if enemy.hp <= 0:
    PlayerIG.bs += 1
    win(enemy.gpgiv, enemy.gpgiv)
    clearConsole()
  if eattack == enemymiss:
    print("The enemy missed!")
    time.sleep(1)
  elif eattack >= enemy.attack:
    print("The enemy did a critcal hit!")
    time.sleep(0.5)
    eattack -= PlayerIG.arcls
    if eattack <= 0:
      eattack = 0 
    PlayerIG.hp -= eattack
    print("The enemy delt", eattack ,"damage to you!")
    time.sleep(1)
  else:
    eattack -= PlayerIG.arcls
    if eattack <= 0:
      eattack = 0 
    PlayerIG.hp -= eattack
    print("The enemy delt", eattack ,"damage to you!")
    time.sleep(1)
  if PlayerIG.hp <= 0:
    die()
  else:
    GFight()


def GFight():
  clearConsole()
  print(reset+"  ", PlayerIG.name ," vs ", enemy.name)
  print(PlayerIG.name ,"\b's Health:"+Red, PlayerIG.hp ,"/", PlayerIG.maxhp ,""+reset)
  print(enemy.name ,"\b's Health:"+Red, enemy.hp ,"/", enemy.maxhp ,""+reset)
  print("Health Potions:"+Red, PlayerIG.hpots)
  print(reset+"\n1.) "+Red+"Attack"+reset)
  print("2.) Magic")
  print("3.) Inspect Enemy")
  print("4.) Drink Health Potion")
  print("5.) Run")
  option = input("--> "+Blue)
  print(reset+"")
  if option == ("1"):
    Gattack(PlayerIG.attack, enemy.attack, PlayerIG.mis, enemy.mis)
  elif option == ("2"):
    clearConsole()
    print(
      "It's a monster that is both alive and dead. Some say it's a god, others say it's beyond that. But everyone agrees that once you see him, you can't escape, it's already too late."
    )
    print("Max Health:"+Red+"?!@!*AK@L"+reset)
    print("Attack:"+Red+">!<@(A?)P"+reset)
    time.sleep(1)
    GFight()
  elif option == ("3"):
    if PlayerIG.hpots > 0:
      clearConsole()
      print(
        "All your health potions have disappered... You can only pray to god now..."
      )
      time.sleep(1)
      GFight()
    else:
      print(
        "You have none..."
      )
      time.sleep(1)
      GFight()
  elif option == ("4"):
    clearConsole()
    print(
      "A powerful force is keeping you from leaving... It's already to late"
         )
    time.sleep(1)
    GFight()
  elif option.lower().strip() == "pray":
    pray = random.randint(0,10)
    if pray == 2:
      print("You pray to god...")
      time.sleep(1)
      clearConsole()
      print(".")
      time.sleep(0.5)
      clearConsole()
      print("..")
      time.sleep(0.5)
      clearConsole()
      print("...")
      time.sleep(0.5)
      clearConsole()
      print("Seems like god doesn't care for you...")
      time.sleep(1)
      GFight()
    elif pray == 6:
      pheal = random.randint(0, 1000)
      PlayerIG.hp += pheal
      if PlayerIG.hp >= PlayerIG.maxhp:
        pheal -= PlayerIG.maxhp
        PlayerIG.hp == PlayerIG.maxhp
      print("God heals you for", pheal)
      time.sleep(1)
      GFight()
    elif pray == 10:
      gmax = random.randint(0,1000)
      gamax = random.randint(0, 1000)
      PlayerIG.maxhp += gmax
      PlayerIG.attack += gamax
      print("God gives you more max hp! +", gmax, "maxhp!")
      time.sleep(1)
      print("God also gives you more attack! +", gamax,"attack!")
      time.sleep(1)
      GFight()
  else:
    GFight()
  option = (" ")


def glitched():
  clearConsole()
  print(black+"Boss Fight!"+reset)
  time.sleep(1)
  GFight()


def glitchfight():
  clearConsole()
  print("?!2A|%1@?,~")
  time.sleep(0.2)
  clearConsole()
  print("(A%< Fi:+_!")
  time.sleep(0.2)
  clearConsole()
  print(")&!s Fig?-=")
  time.sleep(0.2)
  clearConsole()
  print("*^ss Figh#@")
  time.sleep(0.2)
  clearConsole()
  print("?oss Fight$")
  time.sleep(0.2)
  clearConsole()
  glitched()


def bossfight2():
  clearConsole()
  print(Red+"Boss Fight!"+reset)
  time.sleep(1)
  fight()

  
def bossfight():
  clearConsole()
  print(reset+"|         |")
  time.sleep(0.2)
  clearConsole()
  print("||       ||")
  time.sleep(0.2)
  clearConsole()
  print("|||     |||")
  time.sleep(0.2)
  clearConsole()
  print("||||   ||||")
  time.sleep(0.2)
  clearConsole()
  print("||||| |||||")
  time.sleep(0.2)
  clearConsole()
  print("|||||||||||")
  time.sleep(0.2)
  clearConsole()
  print("|||||F|||||")
  time.sleep(0.2)
  clearConsole()
  print("|||| Fi||||")
  time.sleep(0.2)
  clearConsole()
  print("|||s Fig|||")
  time.sleep(0.2)
  clearConsole()
  print("||ss Figh||")
  time.sleep(0.2)
  clearConsole()
  print("|oss Fight|")
  time.sleep(0.2)
  clearConsole()
  bossfight2()

  
def fight():
  clearConsole()
  print(reset+"  ", PlayerIG.name ," vs ", enemy.name)
  print(PlayerIG.name ,"\b's Health:"+Red, PlayerIG.hp ,"/", PlayerIG.maxhp ,""+reset)
  print(PlayerIG.name ,"\b's Mana:"+Blue, PlayerIG.mp ,"/", PlayerIG.maxmp ,""+reset)
  print(enemy.name ,"\b's Health:"+Red, enemy.hp ,"/", enemy.maxhp ,""+reset)
  print("Health Potions:"+Red, PlayerIG.hpots)
  print(reset+"\n1.) "+Red+"Attack"+reset)
  print("2.) Magic")
  print("3.) Inspect Enemy")
  print("4.) Drink Health Potion")
  print("5.) Run")
  option = input("--> "+Blue)
  print(reset+"")
  if option.lower().strip() == "attack" or option == ("1"):
    attack(PlayerIG.attack, enemy.attack, PlayerIG.mis, enemy.mis)
  elif option.lower().strip() == "magic" or option == ("2"):
    magic(PlayerIG.attack, enemy.attack, PlayerIG.mis, enemy.mis)
  elif option.lower().strip() == "inspect enemy" or option.lower().strip() == "inspect" or option == ("3"):
    inspect()
  elif option.lower().strip() == "drink health potion" or option.lower().strip() == "health potion" or option == ("4"):
    drinkhpot()
  elif option.lower().strip() == "run" or option == ("5"):
    run(enemy.attack, enemy.mis)
  else:
    fight()
  option = (" ")


def magic(playerattack, enemyattack, playermiss, enemymiss):
  clearConsole()
  print("What spell would you like to use?")
  time.sleep(1)
  print("1.) Fire ball")
  option = input("-->"+Blue)
  print(reset+"")
  pm = PlayerIG.mattack - 5
  pm2 = PlayerIG.mattack + 5
  ma = random.randint(pm, pm2)
  em = enemy.attack - 5
  em2 = enemy.attack + 5
  ema = random.randint(pm, pm2)
  if option.lower().strip() == "fire ball" or option == "1":
    clearConsole()
    PlayerIG.mp -= 10
    pm = playermiss
    pm2 = PlayerIG.mattack + 5
    ma = random.randint(pm, pm2)
    em = enemymiss
    em2 = enemy.attack + 5
    ema = random.randint(pm, pm2)
    if ma == PlayerIG.mis:
      print("You miss!")
    elif ma == pm2:
      print("Critical Hit!")
      time.sleep(1)
      ma -= enemy.mres
      if ma <= 0:
        ma = 0 
      enemy.hp -= ma
      print("You deal", ma ,"to the enemy!")
      time.sleep(1)
    else:
      ma -= enemy.arcls
    if ma <= 0:
      ma = 0 
    enemy.hp -= ma
    print("You deal", ma ,"to the enemy!")
    time.sleep(1)
    if enemy.hp <= 0:
      win(enemy.gpgiv, enemy.gpgiv)
      clearConsole()
    if ema == enemymiss:
      print("The enemy missed!")
      time.sleep(1)
    elif ema == enemy.attack + 5:
      print("The enemy did a critcal hit!")
      time.sleep(0.5)
      ema -= PlayerIG.arcls
      if ema <= 0:
        ema = 0 
      PlayerIG.hp -= ema
      print("The enemy delt", ema ,"damage to you!")
      time.sleep(1)
    else:
      ema -= PlayerIG.arcls
      if ema <= 0:
        ema = 0 
      PlayerIG.hp -= ema
      print("The enemy delt", ema ,"damage to you!")
      time.sleep(1)
    if PlayerIG.hp <= 0:
      die()
    else:
      fight()


def inspect():
  clearConsole()
  print(reset+"Enemy:", enemy.name)
  print("HP:"+Red, enemy.hp ,"/", enemy.maxhp)
  print(reset+"Base Attack:"+Red, enemy.attack)
  print(reset+"Magic Attack:"+Blue, enemy.mattack)
  time.sleep(1)
  print(reset+"\n1.) Back")
  option = input("--> "+Blue)
  if option.lower().strip() == "back" or option == "1" or option == "b":
    fight()
  else:
    fight()

  
def attack(playerattack, enemyattack, playermiss, enemymiss):
  clearConsole()
  global pattack
  global eattack
  p = playermiss
  p2 = playerattack + 5
  e = enemymiss
  e2 = enemy.attack + 5
  pattack = random.randint(p, p2)
  eattack = random.randint(e, e2)
  if PlayerIG.mp < PlayerIG.maxmp:
    PlayerIG.mp += 5
    if PlayerIG.mp >= PlayerIG.maxmp:
      PlayerIG.mp = PlayerIG.maxmp
  if pattack == playermiss:
    print("You Miss!")
  elif pattack == PlayerIG.attack + 5:
    print("Critical Hit!")
    time.sleep(0.5)
    pattack -= enemy.arcls
    if pattack <= 0:
      pattack = 0 
    enemy.hp -= pattack
    print("You deal", pattack ,"to the enemy!")
    time.sleep(1)
  else:
    pattack -= enemy.arcls
    if pattack <= 0:
      pattack = 0 
    enemy.hp -= pattack
    print("You deal", pattack ,"to the enemy!")
    time.sleep(1)
  if enemy.hp <= 0:
    win(enemy.gpgiv, enemy.gpgiv)
    clearConsole()
  if eattack == enemymiss:
    print("The enemy missed!")
    time.sleep(1)
  elif eattack == enemy.attack + 5:
    print("The enemy did a critcal hit!")
    time.sleep(0.5)
    eattack -= PlayerIG.arcls
    if eattack <= 0:
      eattack = 0 
    PlayerIG.hp -= eattack
    print("The enemy delt", eattack ,"damage to you!")
    time.sleep(1)
  else:
    eattack -= PlayerIG.arcls
    if eattack <= 0:
      eattack = 0 
    PlayerIG.hp -= eattack
    print("The enemy delt", eattack ,"damage to you!")
    time.sleep(1)
  if PlayerIG.hp <= 0:
    die()
  else:
    fight()


def drinkhpot():
  clearConsole()
  if PlayerIG.hpots == 0:
    print("You don't have any Health Potions!")
    time.sleep(1)
    fight()
  else:
    bh = PlayerIG.hp
    PlayerIG.hpots -= 1
    PlayerIG.hp += 10
    ah = PlayerIG.hp
    if PlayerIG.hp > PlayerIG.maxhp:
      Player.hp = PlayerIG.hp
    print("You drank a Health Potion!")
    time.sleep(1)
    heal = bh - ah
    print("You recovered", heal,"hp!")
  fight()


def run(enemyattack, enemymiss):
  clearConsole()
  e = round(enemyattack / 2)
  e2 = enemyattack + 5
  eattack = random.randint(e, e2)
  runnum = random.randint(1, 3)
  if runnum == 1:
    print("You have successfully ran away!")
    time.sleep(1)
    main()
  else: 
    print("You failed to get away!")
    time.sleep(1)
    clearConsole()
    if eattack == enemymiss: 
      print("The enemy missed!")
      time.sleep(1)
    elif eattack == enemy.attack + 5:
      print(Red+"Critical hit!"+reset)
      time.sleep(1)
      PlayerIG.hp -= eattack
      print("The enemy deals"+Red, eattack ,reset+"damage!")
      time.sleep(1.5)
    else:
      PlayerIG.hp -= eattack
      print("The enemy deals"+Red, eattack ,reset+"damage!")
      time.sleep(1.5)
    if PlayerIG.hp <= 0: 
      die()
    else:
      fight()


def win(goldgiv, expgiv):
  clearConsole()
  g = round(expgiv / 2)
  g2 = expgiv
  gd =random.randint(g, g2)
  PlayerIG.gp += gd
  e = round(goldgiv / 2)
  e2 = goldgiv
  exp = random.randint(e, e2)
  PlayerIG.exp += exp
  PlayerIG.r = 2
  PlayerIG.te += 1
  print("You have defeated", enemy.name , "\b!")
  time.sleep(1)
  print("You found", gd ,"gold!")
  w = random.randint(0,10)
  if w == 7:
    if enemy.weapon == True:
      if enemy.weapgiv in PlayerIG.inv:
        print("You found a weapon! But you already have it")
        time.sleep(1)
      else:
        PlayerIG.inv.append(enemy.weapgiv)
        print("You found a weapon!", enemy.weapgiv)
        time.sleep(1)
    else:
      pass
  else:
    pass
  
  a = random.randint(0,10)
  if a == 7:
    if enemy.armor == True:
      if enemy.armgiv in PlayerIG.inv:
        print("You found armor! But you already have it")
        time.sleep(1)
      else:
        PlayerIG.inv.append(enemy.armgiv)
        print("You found a weapon!", enemy.armgiv)
        time.sleep(1)
    else:
      pass
  else: 
    pass
  
  print("+",exp ,"EXP!")
  time.sleep(3)
  main()


class Items():
  def __init__(self, name, cost, attack, defense):
    self.name = name
    self.cost = cost
    self.attack = attack
    self.defense = defense


def store():
  clearConsole()
  print("Your gold:", PlayerIG.gp)
  print(reset+"Welcome to Tim's shop!")
  time.sleep(0.1)
  print("What would you like to buy?")
  print("Type B, or Back, to go back")
  print("\n1.) Sword")
  print("2.) Potions")
  print("3.) Armor")
  time.sleep(1)
  option = input("--> "+Blue)
  print(reset+"")
  if option == "1" or option.lower().strip() == "sword":
    clearConsole()
    print("Your gold:", PlayerIG.gp)
    print("What sword?")
    print("Type B, or Back, to go back")
    print("1.) Wood Sword + 5 attack | Cost 5 Gold")
    print("2.) Bronze Sword + 10 attack | Cost 10 Gold")
    print("3.) Iron Sword + 20 attack | Cost 20 Gold")
    if PlayerIG.lvl >= 2:
        print("4.) Steel Sword + 30 attack | cost 50 Gold")
    time.sleep(1)
    option = input("--> "+Blue)
    print(reset+"")
    if option.lower().strip() == "wood sword" or option == "1":
      ItemsIG = Items("Wood Sword", 5, 5, 0)
      if PlayerIG.gp >= ItemsIG.cost:
        PlayerIG.gp -= ItemsIG.cost
        PlayerIG.inv.append(ItemsIG.name)
        print("Ok!")
        print("You have bought", ItemsIG.name ,"for", ItemsIG.cost ,"gold")
        time.sleep(1)
        store()
      elif PlayerIG.gp < ItemsIG.cost:
        print("Hmm, seems like you don't got enough buddy.")
        time.sleep(1)
        store()
    elif option.lower().strip() == "bronze sword" or option == "2":
      ItemsIG = Items("Bronze Sword", 10, 10, 0)
      if PlayerIG.gp >= ItemsIG.cost:
        PlayerIG.gp -= ItemsIG.cost
        PlayerIG.inv.append(ItemsIG.name)
        print("Ok!")
        print("You have bought", ItemsIG.name ,"for", ItemsIG.cost ,"gold")
        time.sleep(1)
        store()
      elif PlayerIG.gp < ItemsIG.cost:
        print("Hmm, seems like you don't got enough buddy.")
        time.sleep(1)
        store()
    elif option.lower().strip() == "iron sword" or option == "3":
      ItemsIG = Items("Iron Sword", 20, 20, 0)
      if PlayerIG.gp >= ItemsIG.cost:
        PlayerIG.gp -= ItemsIG.cost
        PlayerIG.inv.append(ItemsIG.name)
        print("Ok!")
        print("You have bought", ItemsIG.name ,"for", ItemsIG.cost ,"gold")
        time.sleep(1)
        store()
      elif PlayerIG.gp < ItemsIG.cost:
        print("Hmm, seems like you don't got enough buddy.")
        time.sleep(1)
        store()
    elif option.lower().strip() == "steel sword" or option == "4":
      if PlayerIG.lvl >= 2:
        ItemsIG = Items("Steel Sword", 40, 30, 0)
        if PlayerIG.gp >= ItemsIG.cost:
          PlayerIG.gp -= ItemsIG.cost
          PlayerIG.inv.append(ItemsIG.name)
          print("Ok!")
          print("You have bought", ItemsIG.name ,"for", ItemsIG.cost ,"gold")
          time.sleep(1)
          store()
        elif PlayerIG.gp < ItemsIG.cost:
          print("Hmm, seems like you don't got enough buddy.")
          time.sleep(1)
          store()
      elif option.lower().strip() == "b" or option.lower().strip() == "back":
        store()
    else:
      print("Choose one of the options")
      time.sleep(1)
      store()
  elif option.lower().strip() == "potions" or option == "2":
    clearConsole()
    global amount
    amount = 0
    print("Your gold:", PlayerIG.gp)
    print("What potion?")
    print("Type B, or Back, to go back")
    print("1.) Health Potion + 10 HP | 5 gold per potion")
    option = input("--> "+Blue)
    print(reset+"")
    if option.lower().strip() == "health potions" or option.lower().strip() == "health" or option == "1":
      ItemsIG = Items("Health Potion", 5, 0, 0)
      print("How many would you like?")
      amount = int(input("--> "+Blue))
      print(reset+"")
      TotalCost = amount * ItemsIG.cost
      if amount <= 0:
        print("Can't have 0 or a negaitve amount!")
        time.sleep(1)
        store()
      elif PlayerIG.gp < TotalCost:
        print("Hmm, seems like you don't got enough buddy.")
        time.sleep(1)
        store()
      else:
        PlayerIG.hpots += amount
        PlayerIG.gp -= TotalCost
        print("Ok!")
        print("You have bought", amount ,ItemsIG.name, "for", TotalCost ," gold")
        time.sleep(1)
        store()
    elif option.lower().strip() == "b" or option.lower().strip() == "back":
      store()
    else:
      print("Choose one of the options")
      time.sleep(1)
      store()
  elif option.lower().strip() == "armor" or option == "3":
    clearConsole()
    print("Your gold:", PlayerIG.gp)
    print("What armor?")
    print("Type B, or Back, to go back")
    print("1.) Wood Armor + 5 Defense | Cost 5 gold")
    print("2.) Bronze Armor + 15 Defense | Cost 10 gold")
    print("3.) Iron Armor + 30 Defense | Cost 25 gold")
    if PlayerIG.lvl >= 2:
      print("4.) Steel Armor + 40 Defense | Cost 60 Gold")
    option = input(reset+"--> "+Blue)
    print(reset+"")
    if option.lower().strip() == "wood armor" or option == "1":
      ItemsIG = Items("Wood Armor", 5, 0, 5)
      if PlayerIG.gp >= ItemsIG.cost:
        PlayerIG.gp -= ItemsIG.cost
        PlayerIG.inv.append(ItemsIG.name)
        print("Ok!")
        print("You have bought", ItemsIG.name ,"for", ItemsIG.cost ,"gold")
        time.sleep(1)
        store()
      elif PlayerIG.gp < ItemsIG.cost:
        print("Hmm, seems like you don't got enough buddy.")
        time.sleep(1)
        store()
    elif option.lower().strip() == "bronze armor" or option == "2":
      ItemsIG = Items("Bronze Armor", 10, 0, 15)
      if PlayerIG.gp >= ItemsIG.cost:
        PlayerIG.gp -= ItemsIG.cost
        PlayerIG.inv.append(ItemsIG.name)
        print("Ok!")
        print("You have bought", ItemsIG.name ,"for", ItemsIG.cost ,"gold")
        time.sleep(1)
        store()
      elif PlayerIG.gp < ItemsIG.cost:
        print("Hmm, seems like you don't got enough buddy.")
        time.sleep(1)
        store()
    elif option.lower().strip() == "iron armor" or option == "3":
      ItemsIG = Items("Iron Armor", 25, 0, 30)
      if PlayerIG.gp >= ItemsIG.cost:
        PlayerIG.gp -= ItemsIG.cost
        PlayerIG.inv.append(ItemsIG.name)
        print("Ok!")
        print("You have bought", ItemsIG.name ,"for", ItemsIG.cost ,"gold")
        time.sleep(1)
        store()
      elif PlayerIG.gp < ItemsIG.cost:
        print("Hmm, seems like you don't got enough buddy.")
        time.sleep(1)
        store()
    elif option.lower().strip() == "steel armor" or option == "4":
      if PlayerIG.lvl >= 2:
        ItemsIG = Items("Steel Armor", 60, 0, 30)
        if PlayerIG.gp >= ItemsIG.cost:
          PlayerIG.gp -= ItemsIG.cost
          PlayerIG.inv.append(ItemsIG.name)
          print("Ok!")
          print("You have bought", ItemsIG.name ,"for", ItemsIG.cost ,"gold")
          time.sleep(1)
          store()
        elif PlayerIG.gp < ItemsIG.cost:
          print("Hmm, seems like you don't got enough buddy.")
          time.sleep(1)
          store()
      elif option.lower().strip() == "b" or option.lower().strip() == "back":
        store()
    elif option.lower().strip() == "b" or option.lower().strip() == "back":
      store()
    else:
      print("Choose one of the options")
      time.sleep(1)
      store()
  elif option.lower().strip() == "b" or option.lower().strip() == "back":
    main()
  else:
    print("Choose one of the options")
    time.sleep(1)
    store()


def die():
  clearConsole()
  print("Player:", PlayerIG.name)
  print("Level:", PlayerIG.lvl)
  print("Gold:", PlayerIG.gp)
  print("You have killed"+Red, PlayerIG.te ,reset+"enemies")
  if PlayerIG.bs >= 1:
    print("You have killed"+Red, PlayerIG.bs ,reset+"gods")
  else:
    pass
  print(Red+"You have died"+reset)
  time.sleep(1)
  sys.exit()
  exit()
  quit()


while m == 0:
  smenu()
  m = 1
