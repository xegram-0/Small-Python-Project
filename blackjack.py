import random, sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = "backside"

def main():

    money = int(input("How much money you want to play?"))
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



if "__main__"==__name__:
    main()