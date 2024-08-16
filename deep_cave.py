import random, sys, time
#WIDTH must be larger than the sum of leftWidth and gapWidth
WIDTH = 100
PAUSE_AMOUNT = 0.5 #For delaying time, take no negative value

time.sleep(1)

leftWidth = 20
gapWidth = 10

while True:
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))

    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()

    diceRoll = random.randint(2, 2)
    #Just 2 values for the changes of the diving process
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth - 1
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth = leftWidth + 1
    else:
        pass
    #The same as the block code above
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and gapWidth > 1:
       gapWidth = gapWidth - 1
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
       gapWidth = gapWidth + 1
    else:
       pass

"""
1. The blankspace now becomes (.)
2. The dive will steer toward the left side until there is only 1 (#) left.
3. The dive will go toward right side.
4. NameError since leftWidth is mentioned throughout the program.
5. There will be just a block of (#) since the left side is negative, making the calculation appears like that.
6. ValueError since time.sleep takes non-negative value.
"""