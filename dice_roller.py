import random, sys

def main():
    while True:
        try:
            diceStr:str = input("> ")
            if diceStr.upper() == 'QUIT':
                print("Bye")
                sys.exit()
            
            diceStr = diceStr.lower().replace(' ', '')

            dIndex = diceStr.find('d')
            if dIndex == -1:
                raise Exception("Missing the 'd' character")
            
            numberDice = diceStr[:dIndex]
            if not numberDice.isdecimal():
                raise Exception("Number of dice is not available.")
            numberDice = int(numberDice)

            modIndex = diceStr.find("+")
            if modIndex == -1:
                modIndex = diceStr.find('-')
            
            if modIndex == -1:
                numberSides = diceStr[dIndex + 1:]
            else:
                numberSides = diceStr[dIndex + 1: modIndex]
            if not numberSides.isdecimal():
                raise Exception("Cannot find valid number of sides.")
            numberSides = int(numberSides)

            if modIndex == -1:
                modAmount = 0
            else:
                modAmount = int(diceStr[modIndex + 1:])
                if diceStr[modIndex] == '-':
                    modAmount = -modAmount
            
            rolls = []
            for i in range(numberDice):
                rollResult = random.randint(1, numberSides)
                rolls.append(rollResult)
            
            print(f"Total: {sum(rolls) + modAmount} (each die: ", end ='')
            for i, roll in enumerate(rolls):
                rolls[i] = str(roll)
            print(', '.join(rolls), end='')

            if modAmount != 0:
                modSign = diceStr[modIndex]
                print(f" with mod {modSign}{abs(modAmount)}", end='')
            print(')')
        except Exception as exc:
            print("Invalid input. Should be something like 3d2+3 or 10d6.")
            print("Input is invalid because " + str(exc))
            continue
if __name__ == "__main__":
    main()