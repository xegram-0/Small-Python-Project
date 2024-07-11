import random, sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = "backside"

def main():

    money = int(input("Insert your money: $ "))
    while True:
        if money <= 0:
            print("No money left!")
            print("Goodbye!")
            sys.exit()
        
        print(f"You have ${money} at your disposal.")
        bet = getBet(money)

        deck = getDeck()
        dealerHand = [deck.pop(),deck.pop()]
        playerHand = [deck.pop(),deck.pop()]

        print(f"Bet: ${bet}")
        while True:
            displayHands(playerHand,dealerHand,False)
            print()

            if getHandValue(playerHand) > 21:
                break
            move = getMove(playerHand, money - bet)

            if move == 'D':
                additionalBet = getBet(min(bet,(money-bet)))
                bet += additionalBet
                print(f"Bet increased to {bet}")
                print(f"Bet: {bet}")
            
            if move in ('H','D'):
                newCard = deck.pop()
                rank, suit = newCard
                print(f"You drew a {rank} of {suit}")
                playerHand.append(newCard)
            
            if move in ('S','D'):
                break
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print("Dealer hits...")
                dealerHand.append(deck.pop())
                displayHands(playerHand,dealerHand,False)

                if getHandValue(dealerHand) > 21:
                    break
                input("Press enter to continue")
                print("\n\n")
            displayHands(playerHand,dealerHand,True)

            playerValue = getHandValue(playerHand)
            dealerValue = getHandValue(dealerHand)

            if dealerValue>21:
                print(f"Dealer busts! You win ${bet}!")
                money += bet
            elif (playerValue>21) or (playerValue<dealerValue):
                print("You lost!")
                money -= bet
            elif playerValue > dealerValue:
                print(f"You won ${bet}!")
                money += bet
            elif playerValue == dealerValue:
                print("A tie game! Your money is safe in your hand... for now.")
            
            input("Enter to continue")
            print("\n\n")

def getBet(maxBet):
    while True:
        print(f"How much do you bet? (1-{maxBet} or QUIT)")
        bet = input("> ").upper().strip()
        if bet == 'QUIT':
            print("Bye bye!")
            sys.exit()

        if not bet.isdecimal():
            continue
        
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2,11):
            deck.append((str(rank),suit))
        for rank in ('J','Q','K','A'):
            deck.append((rank,suit))
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    if showDealerHand:
        print(f"DEALER: {getHandValue(dealerHand)}")
        displayCards(dealerHand)
    else:
        print("DEALER: ???")
        displayCards([BACKSIDE] + dealerHand[1:])
    print(f"PLAYER: {getHandValue(playerHand)}")
    displayCards(playerHand)

def getHandValue(cards):

    value = 0
    numberofAces = 0
    for card in cards:
        rank = card[0]
        if rank == "A":
            numberofAces += 1
        elif rank in ('K','Q','J'):
            value += 10
        else:
            value += int(rank)
    
    value += numberofAces
    for i in range(numberofAces):
        if value + 10 <=21:
            value += 10
    return value
    
def displayCards(cards):
    rows = ['','','','','']
    for i, card in enumerate(cards):
        rows[0] += ' ___  '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += '|{} |'.format(rank.ljust(2))
            rows[2] += '| {} |'.format(suit)
            rows[3] += '|_{}|'.format(rank.rjust(2,'_'))
    for row in rows:
        print(row)
    
def getMove(playerHand,money):
    while True:
        moves = ['(H)it','(S)tand']

        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
        
        movePrompt =', '.join(moves) +'> '
        move = input(movePrompt).upper()
        if move in ('H','S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move


if "__main__"==__name__:
    main()

"""
1. Insead of a fix amount, use input to enter the player desired amount.
2. Using condition in the getBet(): The player can only input the amount that
they entered before and the condition in the code restricts any amount above the maxBet.
3. Card = (rank,suit)
4. Cards = [(rank_1,suit_1),(rank_2,suit_2)]
5. Each string of rows list display parts of the cards.
With each string, there will be a line break and each row will
have parts of the cards.
6. The deck would be predictable starting with the first value 
we coded.
7. The player will get money even if they lost the game.
8. showDealerHand is used to display dealer hand on condition.
True when we get the result and stay False when we play.
If we set to either True or False value, the 1st card of the dealer would
stay either reveal or hidden during the entire game.
"""