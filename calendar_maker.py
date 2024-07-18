import datetime

DAYS = ('SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')
MONTHS = ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCTO', 'NOVEM', 'DEC')


def getMonthYear():
    year, month = 0, 0
    # Validate year
    while True:
        response = input("Enter year: ")
        # Only check year from 1 AD and above
        if response.isdecimal() and int(response) > 0:
            year = int(response)
            break
        print("Invalid response")
        print("Enter a year (i.e. 2023)")
        continue
    # Validate month
    while True:
        response = input("Enter month: ")
        # if only is ok but if not would produce detailed prompts to the users
        if not response.isdecimal():
            print("Invalid response.")
            print("Enter a month (i.e. 3 for March)")
            continue
        month = int(response)
        # if response is not a valid one, repeat the loop
        if 1 <= month <= 12:
            break
        print("Your response should be in range of 1 to 12")
    return month, year


def getCalendar(year: int,
                month: int):
    calText = ' '
    # The year tittle i.e. Mar 2023 the newline
    calText += ('' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
    # For the names of the week
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'
    # Separate the day names and the date number below
    weekSeparator = ('+----------' * 7) + '+\n'
    # Empty space for the cell having date number
    blankRow = ('|          ' * 7) + '|\n'
    # Get datetime object, start from day 1 of the month
    currentDate = datetime.date(year, month, 1)
    # print(currentDate, currentDate.weekday()) # For testing, not understand what this does
    # Make the calendar starts at Sunday instead of any other day since we designed
    # the first day to be Sunday at line 41
    # weekday() returns 6 if it is Sunday
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)
    # Where the calendar text happens
    while True:
        # Separators are drawn
        calText += weekSeparator
        dayNumberRow = ''
        # Where 7 days are drawn for the month
        for i in range(7):
            # Adjust the date number
            dayNumberLabel = str(currentDate.day).rjust(2)
            # Format the row containing date number
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            # Increment the date number i.e. 1 to 2 to 3 up to the max number of the month
            currentDate += datetime.timedelta(days=1)
        # Closing the row containing the date number
        dayNumberRow += '|\n'
        # Add as a part of calendar text each time
        calText += dayNumberRow
        # Format the cell with 3 blank space (line 45)
        for i in range(3):
            calText += blankRow
        # Break the loop when the month is exceeded
        # This does not include when the row exceeds the month
        # i.e. when the row reaches the final date of the input month
        # the program would take some dates of the next/previous month
        # then calls it off with this if statement
        if currentDate.month != month:
            break
    # Separate the weeks
    calText += weekSeparator
    return calText


def saveFile(month: int,
             year: int,
             calendarText: str) -> None:
    # File string can be used with f string format.
    calendarFile = f"calendar_{year}_{MONTHS[month - 1]}"
    with open(calendarFile, 'w') as fileObj:
        fileObj.write(calendarText)
    print(f"{calendarFile} is saved")


def main():
    # Only get the main stuff
    inputMonth, inputYear = getMonthYear()
    calText = getCalendar(inputYear, inputMonth)
    print(calText)
    # Want to give the user the choice of saving or not
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
"""
1. By changing the contents of the MONTHS tuples.
2. ValueError, the program thinks the year = 0.
3. By removing the calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'
4. By removing the codes that save file or like what I did, choices.
5. No calendar is printed in the terminal but it is saved in the file.
"""