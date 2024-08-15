import sys, time
import sevseg

secondsLeft = 30

try:
    while True:
        print('\n' * 50)
        hours = str(secondsLeft // 3600)
        minutes = str((secondsLeft // 3600) // 60)
        seconds = str(secondsLeft % 60)

        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        print(hTopRow + " " + mTopRow + " " + sTopRow)
        print(hMiddleRow + " " + mMiddleRow + " " + sMiddleRow)
        print(hBottomRow + " " + mBottomRow + " " + sBottomRow)

        if secondsLeft == 0:
            print()
            print("    ****BOOM****")
            break
        print()
        print("Ctrl C to exit")

        time.sleep(1)
        secondsLeft -= 1
except KeyboardInterrupt:
    print("Countdown cannot work")
    print("Thanks for playing!")
    sys.exit()