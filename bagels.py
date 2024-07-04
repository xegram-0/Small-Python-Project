# Guess a secret three-digit number based on clues
# Responses to your guess will be the following:
# Pico for correct digit at wrong place
# Fermi when guessing the right place and right digit
# Bagels means no right digits
# You have 10 tries


import random
import secrets

MAX_DIGITS = 3
MAX_ATTEMPTS = 10

def main():
    guess:bool = True
    print("***************************")
    print("Welcome to bagels game!")
    print("Guess a 3-digit number with the following clues:")
    print("You get Pico if the digit is correct and at wrong place")
    print("You get Fermi when the the digit is at the right place and a correct digit")
    print("You get bagels when the digit is incorrect")
    print("Let's start the game!")
    print("***************************")
    while True:
        secret_gen = secrets.SystemRandom()
        the_number = secret_gen.randint(100,999)
        yourAttempts = 0
        while yourAttempts < MAX_ATTEMPTS:
            yourGuess = get_number()
            evaluate_yourGuess(yourGuess)
            

       
        
        

if "__main__" == __name__:
    main()