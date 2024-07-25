import sys


def collatzSequence(number):
    numberList: list = [number]
    nextNumber: int = 0
    while number != 1:
        if number % 2 == 0:
            nextNumber = number // 2
            numberList.append(nextNumber)
            # print(numberList)
        elif number % 2 == 1:
            nextNumber = number * 3 + 1
            numberList.append(nextNumber)
            # print(numberList)
        number = nextNumber
    return numberList


def main():
    print("""Collatz sequence is about 3n+1. It follows 3 rules: 
          1. If n is even, next number is n/2.
          2. If n is odd, next number is n*3 + 1.
          3. If n = 1, stop. Else repeat.""")
    startingNumber: int = 0
    while True:
        print("Enter a number greater than 0 or QUIT")
        inputNumber: str = input("> ")
        if inputNumber.upper() == "QUIT":
            sys.exit()
        elif inputNumber.isdecimal() and int(inputNumber) > 0:
            startingNumber: int = int(inputNumber)
            break
        else:
            print("Invalid input")
            continue
    # print(startingNumber)
    collatzList: list = collatzSequence(startingNumber)
    print(collatzList)
    print(f"There are {len(collatzList)} numbers in this sequence.")
# print() has flush = true would help slow down the output of the console with sleep()
# The codes in the book are much shorter and efficient than mine
# Especially the loop and not using list variable.

if __name__ == "__main__":
    main()
"""
1. 6 numbers.
2. 27 numbers.
3. Yes, since n//2 would result in even numbers that are the power of 2.
4. No since response == 0 checks for 0 value input.
"""