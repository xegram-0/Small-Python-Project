import random
import sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

print("Let's start playing CHO HAN game.")
print("""Rules:
    Dealer will put 2 dices in a bamboo cup and roll.
    You as the player must guess 
    whether the total of 2 dices will be
    either even (CHO) or odd (HAN).""")

while True:
    print("How many coins do you have?")
    yourPurse = input("> ")
    if not yourPurse.isdecimal():
        print("Enter a valid amount i.e. 3000 coins.")
        continue
    else:
        yourPurse = int(yourPurse)
        break

while True:
    print(f"You have in your hands {yourPurse} coins, bet your coins or quit?")
    while True:
        pot = input("> ")
        if pot.lower() == 'quit':
            print("Gambling is not good for your soul.")
            sys.exit()
        elif not pot.isdecimal():
            print("Pure coins cannot be tainted with rubbish")
            print("Enter a number i.e. 3000")
        elif int(pot) > yourPurse:
            print("Greedy without solid coins are bad luck.")
            print("Enter a valid amount with in your purse.")
        elif int(pot) < 1:
            print("Goddess of fortuna do not love those who are coward.")
            print("0 coin is not allowed.")
        else:
            pot = int(pot)
            break

    dice1: int = random.randint(1, 6)
    dice2: int = random.randint(1, 6)

    print("The dealer has stirred up the dices and looked at you confidently that you would lose your bet.")
    print("CHO OR HAN")
    print("Make your choice....")

    while True:
        bet: str = input("> ").upper()
        if bet != 'CHO' and bet != 'HAN':
            print("CHO OR HAN? (Choose either of 2 options)")
            continue
        else:
            break

    print("The dealer revealed the cup and your fate has been decided....")
    print(f"{JAPANESE_NUMBERS[dice1]} - {JAPANESE_NUMBERS[dice2]}")
    print(f" {dice1} - {dice2}")

    isRollEven: bool = (dice1 + dice2) % 2 == 0
    if isRollEven:
        result: str = "CHO"
    else:
        result = "HAN"
    playerWon: bool = bet == result

    if playerWon:
        print("You have challenged your fate and fate granted you victory.")
        yourPurse = yourPurse + pot
        print(f"The blessings of the dealer takes {pot // 10} of your coins. Be grateful.")
        yourPurse = yourPurse - (pot // 10)
    else:
        yourPurse = yourPurse - pot
        print("You embraced your chances but your fate could not withstand the hash truth of the dices....")
        print("But rewards are for those who are determined.")

    if yourPurse == 0:
        print()
        print("No coins no games.")
        print("Fate has not been kind to you.")
        print("Leave and maybe next time you can win.")
        sys.exit()
