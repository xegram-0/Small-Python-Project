import random
import sys
# Just the way to express the cultural game
JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

print("Let's start playing CHO HAN game.")
print("""Rules:
    Dealer will put 2 dices in a bamboo cup and roll.
    You as the player must guess 
    whether the total of 2 dices will be
    either even (CHO) or odd (HAN).""")
# Input a valid amount of coins
while True:
    # For some reason, specific about the type of variable
    # and change it make the ide question a lot
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
'''
1. By changing the value of the 'purse' variable.
2. If their bet is larger than what in their purse, they make an invalid bet.
3. Take the total of 2 dices and module it with 2, that would lead to whether the sum is odd or even.
4. The dices would produce 1 each since the randint is restricted to 1.
5. The question is quite unclear: if 'pot // 10' to '0' then no; if 'pot // 0' then divided by 0.
6. Player would bet even they run out of money.
'''