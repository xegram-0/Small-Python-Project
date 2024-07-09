# Create bitmap "World map"

import sys

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

#bitmap = """
#"""
print("Enter the message to display with the bitmap.")
message = input("> ")
if message == '':
    sys.exit()

# splitlines() turns string to items of a list at each line breaks.
# Draw from 1st line to the last
for line in bitmap.splitlines():
    # bit = character of the bitmap
    # i = index

    # Expect 2, got 1 error
    #for i, bit in line:
    # What enumerate does:  (0, thing[0]), (1, thing[1]), (2, thing[2]),
    # So i takes the number while bit takes the thing
    for i,bit in enumerate(line):
        # ' ' needs to have space
        # otherwise it would condense to each other
        if bit ==' ':
            print(' ',end='')
        else:
            # Testing
            #print(bit)
            #print(message[i],end='')

            # This math is to keep the range within the len(message)
            # If not, it exceeds and crashes
            # Also to print the message in order
            print(message[i%len(message)],end='')
    print()
"""
1. There will be blank space after typing the message.
2. Yes. The nonspace characteres in the bitmap act as the placeholders
for our messages.
3. i variable creates character from the message.
4. There will be no newlines. Every new character is printed on the same line
until it jumps to the next one.
"""