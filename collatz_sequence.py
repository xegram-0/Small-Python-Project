import sys


def collatzSequence(number):
    numberList: list = [number]
    while True:
        if number % 2 == 0:
            numberList.append(number/2)
        elif number % 2 == 1:
            numberList.append(number*3 + 1)
        elif number == 1:
            return numberList
        else:
            continue


def main():
    print("""Collatz sequence is about 3n+1. It follows 3 rules: 
          1. If n is even, next number is n/2.
          2. If n is odd, next number is n*3 + 1.
          3. If n = 1, stop. Else repeat.""")

    print("Enter a number greater than 0 or QUIT")
    inputNumber: str = input("> ")
    while True:
        if inputNumber.upper() == "QUIT":
            sys.exit()
        elif inputNumber.isdecimal() and int(inputNumber) > 0:
            startingNumber: int = int(inputNumber)
            break
        else:
            print("Invalid input")

    collatzList: list = collatzSequence(startingNumber)
    print(collatzList)


if __name__ == "__main__":
    main()