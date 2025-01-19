import random, shutil, sys, time

PAUSE = 0.2
DENSITY = 0.1

DUCK_WIDTH = 5
LEFT = 'left'
RIGHT = 'right'
BEADY = 'beady'
WIDE = 'wide'
HAPPY = 'happy'
ALOOF = 'aloof'
CHUBBY = 'chubby'
VERY_CHUBBY = "very chubby"
OPEN = 'open'
CLOSED = 'closed'
OUT = 'out'
DOWN = 'down'
UP = 'up'
HEAD = 'head'
BODY = 'body'
FEET = 'feet'

WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1

def main():
    time.sleep(2)
    duckLanes = [None] * (WIDTH // DUCK_WIDTH)

    while True:
        for laneNum, duckObj in enumerate(duckLanes):
            if (duckObj == None and random.random() <= DENSITY):
                duckObj = Duckling()
                duckLanes[laneNum] = duckObj

            if duckObj != None:
                print(duckObj.getNextBodyPart(), end='')    
                if duckObj.partToDisplayNext == None:
                    duckLanes[laneNum] = None
            else:
                print(' ' * DUCK_WIDTH, end='')
        print()
        sys.stdout.flush()
        time.sleep(PAUSE)

class Duckling:
    def __init__(self):
        self.direction = random.choice([LEFT, RIGHT])
        self.body = random.choice([CHUBBY, VERY_CHUBBY])
        self.mouth = random.choice([OPEN, CLOSED])
        self.wing = random.choice([OUT, UP, DOWN])

        if self.body == CHUBBY:
            self.eyes = BEADY
        else:
            self.eyes = random.choice([BEADY, WIDE, HAPPY, ALOOF])
        
        self.partToDisplayNext = HEAD

    def getHeadStr(self):
        headStr = ''
        if self.direction == LEFT:
            if self.mouth == OPEN:
                headStr += '>'
            elif self.mouth == CLOSED:
                headStr += '='
            
            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += '" '
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'

            headStr += ') '  # Get the back of the head.

        if self.direction == RIGHT:
            headStr += ' ('  # Get the back of the head.

            # Get the eyes:
            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += ' "'
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'

            # Get the mouth:
            if self.mouth == OPEN:
                headStr += '<'
            elif self.mouth == CLOSED:
                headStr += '='

        if self.body == CHUBBY:
            # Get an extra space so chubby ducklings are the same
            # width as very chubby ducklings.
            headStr += ' '

        return headStr

    def getBodyStr(self):
        """Returns the string of the duckling's body."""
        bodyStr = '('  # Get the left side of the body.
        if self.direction == LEFT:
            # Get the interior body space:
            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

            # Get the wing:
            if self.wing == OUT:
                bodyStr += '>'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'

        if self.direction == RIGHT:
            # Get the wing:
            if self.wing == OUT:
                bodyStr += '<'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'

            # Get the interior body space:
            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

        bodyStr += ')'  # Get the right side of the body.

        if self.body == CHUBBY:
            # Get an extra space so chubby ducklings are the same
            # width as very chubby ducklings.
            bodyStr += ' '

        return bodyStr

    def getFeetStr(self):
        """Returns the string of the duckling's feet."""
        if self.body == CHUBBY:
            return ' ^^  '
        elif self.body == VERY_CHUBBY:
            return ' ^ ^ '

    def getNextBodyPart(self):
        """Calls the appropriate display method for the next body
        part that needs to be displayed. Sets partToDisplayNext to
        None when finished."""
        if self.partToDisplayNext == HEAD:
            self.partToDisplayNext = BODY
            return self.getFeetStr()
        elif self.partToDisplayNext == BODY:
            self.partToDisplayNext = FEET
            return self.getBodyStr()
        elif self.partToDisplayNext == FEET:
            self.partToDisplayNext = None
            return self.getFeetStr()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Bye")
        sys.exit()

"""
1. All ducks would face left instead of right and left.
2. All ducks would have face but no body.
3. All ducks would have infinite bodies.
4. Heads are replaced with feet.
"""