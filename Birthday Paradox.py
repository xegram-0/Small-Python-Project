"""
Birthday Problem is about people having the same birthday.
In a group of 70 people, there is 99.9% of two people having the same birthday.
And even with 23 people, there is a chance of 50% of that happens.
Write a program to experiment this problem.
"""

import datetime, random

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr','May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print("How many birthdays do you want to generate (max 100)")
    response = input('> ')
    if response.isdecimal() and (0<int(response)<=100):
        numBDays = int(response)
        break

print(f"Here are {numBDays} birthdays")
birthdays = getBirthdays(numBDays)

for i, birthdays in enumerate(birthdays):
    if i!=0:
        print(', ',end='')
    monthName = MONTHS[birthday.month -1]
    dateText ='{} {}'.format(monthName,birthday.day)
    print(dateText,end='')

match = getMatch(birthdays)

print("In this simulation ",end='')
if match != None:
    monthName = MONTHS[match.month -1 ]
    dateText = '{} {}'.format(monthName, match.day)
    print(f"multiple people have a birthday on {dateText}")
else:
    print("there are no matching birthdays.")

print(f"Generating {numBDays} random birthdays 100,000 times")
input("Press enter to begin...")

print("Let\'s run another 100,000 simulations.")
simMatch = 0
for i in range(100000):
    if i%10000==0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays != None):
        simMatch = simMatch +1
print("100,000 simulations runs.")

probability = round(simMatch/100000 * 100,2)
print("Out of 100,000 simulations of {numBDays}")