# Guess a secret three-digit number based on clues
# Responses to your guess will be the following:
# Pico for correct digit at wrong place
# Fermi when guessing the right place and right digit
# Bagels means no right digits
# You have 10 tries


import random

MAX_DIGITS = 3
MAX_ATTEMPTS = 10

def get_clue(yourGuess,the_number):
    # Check the digit in the number is equal to the secret number
    # elif ... in would shows if there is a right digit at wrong place
    for i in range(MAX_DIGITS):
        if yourGuess[i] == the_number[i]:
            print("Fermi")
        elif yourGuess[i] in the_number:
            print("Pico")
        else:
            print("Bagels")

def main():

    print("***************************")
    print("Welcome to bagels game!")
    print("Guess a 3-digit number with the following clues:")
    print("You get Pico if the digit is correct and at wrong place")
    print("You get Fermi when the the digit is at the right place and a correct digit")
    print("You get bagels when the digit is incorrect")
    print("Let's start the game!")
    print("***************************")

    # Using slicing requires both varibles to be string
    the_number = str(random.randint(100,999))
    yourAttempts = 1

    while yourAttempts <= MAX_ATTEMPTS:
        yourGuess = input("> ")
        if yourGuess == the_number:
            print("Bingo!!!")
            break
        else:
            get_clue(yourGuess,the_number)
    # Need to be before if otherwise exceed the attempt limit
        yourAttempts += 1
        if yourAttempts > MAX_ATTEMPTS:
            print("You have exceeded your attempt")
            print("You lose!")

    print("Thank you for playing!")
    
if "__main__" == __name__:
    main()