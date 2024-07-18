import datetime

DAYS = ('SUNDAY', 'MONDAY', 'TUESDAY','WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')
MONTHS = ('JAN', 'FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCTO','NOVEM','DEC')
def getMonthYear():
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
    return month, year
def getCalendar(year:int, month:int):
    calText = ' '
    calText += (''* 34) + MONTHS[month -1] + ' ' + str(year) + '\n'
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'
    weekSeparator = ('+----------' * 7) + '+\n'
    blankRow = ('|          ' * 7) + '|\n'
    currentDate = datetime.date(year, month, 1)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)
    while True:
        calText += weekSeparator
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)
        dayNumberRow += '|\n'

        calText += dayNumberRow
        for i in range(3):
            calText += blankRow

        if currentDate.month != month:
            break
    calText += weekSeparator
    return calText
def saveFile(month:int, year:int, calText:str):
    calendarFile = f"calendar_{year}_{MONTHS[month - 1]}"
    with open(calendarFile, 'w') as fileObj:
        fileObj.write(calText)
    print(f"{calendarFile} is saved")

def main():
    inputMonth, inputYear = getMonthYear()
    calText = getCalendar(inputYear, inputMonth)
    print(calText)
    print("Do you want to save calendar to a file? (Y/N)")
    while True:
        response = input("> ").upper()
        if response.startswith("Y"):
            saveFile(inputMonth, inputYear, calText)
            break
        elif response.startswith("N"):
            print("Goodbye")
            break
        else:
            print("Please put a valid answer (i.e. Y or N)")
            continue
if __name__ == "__main__":
    main()