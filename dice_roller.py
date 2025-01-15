import random, sys

def main():
    # for keep looping this simulation
    while True:
        try:
            diceStr:str = input("> ")
            # whatever the result is would quit the program
            if diceStr.upper() == 'QUIT':
                print("Bye ~~~")
                sys.exit()
            
            diceStr = diceStr.lower().replace(' ', '')

            # find() would return -1 if nothing is found with no exception unlike index()
            # find() would find the first case of the object
            
            dIndex = diceStr.find('d')
            if dIndex == -1:
                raise Exception("Missing the 'd' character")
            # would do the same but find() would give an intruction unlike index() and index() cannot give value without being attention grabber
            # exception would stop the program but in try block, it should be fine with both cases
            # dIndex = diceStr.index('d')
            

            numberDice = diceStr[:dIndex]
            if not numberDice.isdecimal():
                raise Exception("Number of dice is not valid.")
            numberDice = int(numberDice)

            modIndex = diceStr.find("+")
            if modIndex == -1:
                modIndex = diceStr.find('-')
            # it only accept whole number
            if modIndex == -1:
                modIndex = diceStr.find('*')
            if modIndex == -1:
                numberSides = diceStr[dIndex + 1:]
            else:
                numberSides = diceStr[dIndex + 1: modIndex]
            if not numberSides.isdecimal():
                raise Exception("number of sides is not valid.")
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
            
            #mod only matters to sum of all the rolls
            if diceStr[modIndex] == "*":
                print(f"Total: {sum(rolls) * modAmount} (each die: ", end ='')
            else:
                print(f"Total: {sum(rolls) + modAmount} (each die: ", end ='')
            # should always have 2 variables for enumerate
            for i, roll in enumerate(rolls):
                rolls[i] = str(roll)
            print(', '.join(rolls), end='')

            if modAmount != 0:
                # is this necessary, if we just put mod with the value
                # by the logic, we omit the sign and grab the value so yeah, this step is needed
                modSign = diceStr[modIndex]
                print(f" with mod {modSign}{abs(modAmount)}", end='')
            print(')')

        except Exception as exc:
            print("Invalid input. Should be something like 3d2+3 or 10d6.")
            print("Input is invalid because " + str(exc))
            continue
if __name__ == "__main__":
    main()
"""
1. No roll is registered in the roll list only the mod lives
2. Just make values turn negative
3. Everything except the value of each roll is present
4. Exception is raised and continues to ask for valid input
"""