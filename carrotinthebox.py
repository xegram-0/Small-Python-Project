import random

print("""
Welcome to carrot in the box game.
This game is for 2 players.
Each will be given a box, one of which contains the carrot.
Player 1 can see the content of the their box while player 2 closes their eyes.
Player 1 then tells the player 2 whether or not there is a carrot in their box.
Player 2 makes a decision whether to make a swap or to keep their box.
The result is revealed when player 2 says YES to swap and NO to keep the box.
""")

p1Name: str = input("Player 1 name: ")
p2Name: str = input("Player 2 name: ")
playerNames = p1Name[:11].center(11) + '    ' + p2Name[:11].center(11)
print("""Here are your boxes
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   BLUE  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+
""")
print()
print(playerNames)
print()
print(f"{p1Name}, you have the RED ox in front of you.")
print(f"{p2Name}, you have the BLUE ox in front of you.")
print()
print(f"{p1Name}, time to look at the box.")
print(f"{p2Name}, time to close your eyes.")
input(f"Press Enter when {p2Name} has closed their eyes")
print()
print("The content of RED box is revealed.....")
if random.randint(1,2) == 1:
    haveCarrot: bool = True
else:
    haveCarrot = False
if haveCarrot:
    print("""
       ___VV____
      |   VV    |
      |   VV    |
      |___||____|    __________
     /    ||   /|   /         /|
    +---------+ |  +---------+ |
    |   RED   | |  |   BLUE  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/
     (carrot!)""")
    print(playerNames)
else:
    print("""
       _________
      |         |
      |         |
      |_________|    __________
     /         /|   /         /|
    +---------+ |  +---------+ |
    |   RED   | |  |   BLUE  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/
    (no carrot!)""")
    print(playerNames)
input("Press Enter to continue....")
print("\n" * 100)
print(f"{p1Name}, please tell {p2Name} to open their eyes.")
print(f"""{p1Name}, tell {p2Name} either of the following sentences:
1. There is a carrot in my box.
2. There is no carrot in my box.""")
input("Press Enter to continue....")
print(f"{p2Name}, please make a choice of swapping the boxes with {p1Name} (YES/NO)")
while True:
    response = input("> ").upper()
    if response.startswith("Y") or response.startswith("N"):
        break
    else:
        print("Please type YES or NO to continue the game.")
        continue
firstBox: str = "RED"
secondBox: str = "BLUE"
if response.startswith("Y"):
    haveCarrot = not haveCarrot
    firstBox, secondBox = secondBox, firstBox
    print("The boxes are swapped.")
print("""
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   {}  | |  |   {}   | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/""".format(firstBox, secondBox)
)
print(playerNames)
input("Press Enter to reveal the result.....")
print()
if haveCarrot:
    print('''
       ___VV____      _________
      |   VV    |    |         |
      |   VV    |    |         |
      |___||____|    |_________|
     /    ||   /|   /         /|
    +---------+ |  +---------+ |
    |   {}  | |  |   {}   | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/'''.format(firstBox, secondBox))
else:
    print('''
       _________      ___VV____
      |         |    |   VV    |
      |         |    |   VV    |
      |_________|    |___||____|
     /         /|   /    ||   /|
    +---------+ |  +---------+ |
    |   {}  | |  |   {}   | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/'''.format(firstBox, secondBox))
print(playerNames)
if haveCarrot:
    print(f"{p1Name} won this game.")
else:
    print(f"{p2Name} won this game.")
print("Thanks for playing! Goodbye.")