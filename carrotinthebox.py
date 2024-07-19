import random
# Explain the rules of the game
print("""
Welcome to carrot in the box game.
This game is for 2 players.
Each will be given a box, one of which contains the carrot.
Player 1 can see the content of the their box while player 2 closes their eyes.
Player 1 then tells the player 2 whether or not there is a carrot in their box.
Player 2 makes a decision whether to make a swap or to keep their box.
The result is revealed when player 2 says YES to swap and NO to keep the box.
""")
# Names should be omitted as they are not necessary
p1Name: str = input("Player 1 name: ")
p2Name: str = input("Player 2 name: ")
# Format the 2 players names when displaying the box
playerNames = p1Name[:11].center(11) + '     ' + p2Name[:11].center(11)
print("""Here are your boxes
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   BLUE  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+
""")
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
# Where the carrot is placed using random
if random.randint(0, 1) == 1:
    isCarrotIn1stBox: bool = True
else:
    isCarrotIn1stBox = False
# haveCarrot is placed at the first box, in this case is the red box
if isCarrotIn1stBox:
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
# To hide the content of the red box to prevent cheating
print("\n" * 100)
print(f"{p1Name}, please tell {p2Name} to open their eyes.")
print(f"""{p1Name}, tell {p2Name} either of the following sentences:
1. There is a carrot in my box.
2. There is no carrot in my box.""")
input("Press Enter to continue....")
print(f"{p2Name}, please make a choice of swapping the boxes with {p1Name} (YES/NO)")
# Using 'if not' means no need to use 'continue' in the else statement
while True:
    response = input("> ").upper()
    if response.startswith("Y") or response.startswith("N"):
        break
    else:
        print("Please type YES or NO to continue the game.")
        continue

firstBox: str = "RED "
secondBox: str = "BLUE"
# Where the swapping happens if Y is the input
if response.startswith("Y"):
    # Where the actual carrot is swapped
    # IMPORTANT!!!
    isCarrotIn1stBox = not isCarrotIn1stBox
    # Just change the name tag on the box
    firstBox, secondBox = secondBox, firstBox
    print("The boxes are swapped.")
# Format the box label with format strings
# Using this is easier to design the box than using f strings
# The out of lines are to line with the rest when running the program
print("""
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   {}  | |  |   {}   | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/""".format(firstBox, secondBox))
print(playerNames)
input("Press Enter to reveal the result.....")
print()
if isCarrotIn1stBox:
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
if isCarrotIn1stBox:
    print(f"{p1Name} won this game.")
else:
    print(f"{p2Name} won this game.")
print("Thanks for playing! Goodbye.")
"""
1. The playerNames only displays a portion of their names. In this case, 11 characters.
2. The lines of the boxes are not in line.
3. Player 2 can see the inside of the box.
4. The loop continues.
"""