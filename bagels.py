# Guess a secret three-digit number based on clues
# Responses to your guess will be the following:
# Pico for correct digit at wrong place
# Fermi when guessing the right place and right digit
# Bagels means no right digits
# You have 10 tries


import random

MAX_DIGITS = 3
MAX_ATTEMPTS = 3

def get_clue(yourGuess,the_number):
    # If all correct
    if yourGuess == the_number:
        return "Bingo"
    # Check the digit in the number is equal to the secret number
    # elif ... in would shows if there is a right digit at wrong place
    # This is the ease mode of the game
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

   
    # This is where the game is running
    while True:
         # Using slicing requires both varibles to be string
        print("New number has been generated!")
        the_number = str(random.randint(100,999))
        yourAttempts = 1
        # This is the part where the guessing happens
        while yourAttempts <= MAX_ATTEMPTS:
            print(f"You have {MAX_ATTEMPTS} attempts.")
            yourGuess=""
            # Right format of number
            # Else loop for eternity
            while len(yourGuess) != MAX_DIGITS or not yourGuess.isdecimal():
                print(f"Your guess #{yourAttempts}:")
                yourGuess = input("> ")

            get_clue(yourGuess,the_number)

        # Need to be before if otherwise exceed the attempt limit
            yourAttempts += 1
            if yourAttempts > MAX_ATTEMPTS:
                print("You have exceeded your attempts")
                print(f"The number is {the_number}")
                print("You lose!")
        
        print("Do you want to play again? (y/n)")

        
        # Work with the 'n' but not 'y'
        # Later on, this also worked???
        choice = input("> ")
        if choice.lower() != 'y':
            break

        # This time the code worked???

        # if not input('> ').lower().startswith('y'):
        #     break
    print("Thank you for playing!")
if "__main__" == __name__:
    main()

# This part is for the question of the program
# The answer codes file is in the book folder
'''
1. The number of digits will be changed according to the value
2. Same as question 1, you can have as many guesses as you want
3. When larger than 10, the code resulted in string out of range
since the list only have from 0 to 10 (10 numbers)
4. The answer will be hard-coded '123'
5. UnboundLocalError: The variable does not have any value to begin with
6. No shuffle means the list will stay the same, means the secret number
would be '012'
7. The code would still run fine, just not prompt the players that
they answer right.
8. The loop will run till you get the right answer a.k.a unlimited guesses
'''