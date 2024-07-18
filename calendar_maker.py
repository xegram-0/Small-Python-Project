import datetime

DAYS = ('SUNDAY', 'MONDAY', 'TUESDAY','WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')
MONTHS = ('JAN', 'FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCTO','NOVEM','DEC')

print()

while True:
    response = input("Enter year: ")
    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
    print("Invalid response")
    print("Enter a year (i.e. 2023)")
    continue

while True:
    response = input("Enter month: ")
    if not response.isdecimal():
        print("Invalid response.")
        print("Enter a month (i.e. 3 for March)")
        continue
    month = int(response)
    if 1 <= month <= 12:
       break
    print("Your response should be in range of 1 to 12")

def getCalendar(year:int, month:int):
    calText = ' '
    calText += (''* 34) + MONTHS[month -1] + ' ' + str(year) + '\n'
    calText += "......Sun.........Mon..........Tues.........Wed..........Thurs.........Fri..........Sat....\n"
    weekSeparator = ("+------------"*7) + "\n"
    blankRow = ("|            "*7) + "\n"
    currentDate = datetime.date(year, month, 1)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)
    while True:
        calText += weekSeparator
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (" " * 8)
            currentDate += datetime.timedelta(days=1)
        dayNumberRow += '\n'

        calText += dayNumberRow
        for i in range(3):
            calText += blankRow

        if currentDate.month != month:
            break
    calText += weekSeparator
    return calText
calText = getCalendar(year, month)
print(calText)

calendarFile = f"calendar_{year}_{month}"
with open(calendarFile, 'w') as fileObj:
    fileObj.write(calText)
print(f"{calendarFile} is saved")
