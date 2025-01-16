import sys, time
import sevseg

def main():
    try:
        while True:
            print('\n' * 30)

            currentTime = time.localtime()
            # this would only display 24 hour system
            hours = str(currentTime.tm_hour)
            #hours = str(currentTime.tm_hour % 12)
            
            if hours == '0':
                hours == '12'
            minutes = str(currentTime.tm_min)
            seconds = str(currentTime.tm_sec)

            hDigits = sevseg.getSevSegStr(hours, 2) # this is in a list
            #print(hDigits)
            hTop, hMid, hBot = hDigits.splitlines() # which is why can be seperated in 3 parts by \n 

            mDigits = sevseg.getSevSegStr(minutes, 2)
            mTop, mMid, mBot = mDigits.splitlines()

            sDigits = sevseg.getSevSegStr(seconds, 2)
            sTop, sMid, sBot = sDigits.splitlines()

            print(f"{hTop}   {mTop}   {sTop}")
            print(f"{hMid} * {mMid} * {sMid}")
            print(f"{hBot} * {mBot} * {sBot}")
            print()
            print("Ctr C to exit")
            
            # act as a delay
            while True:
                time.sleep(0.01)
                if time.localtime().tm_sec != currentTime.tm_sec:
                    break
            

    except KeyboardInterrupt:
        print("Good bye!")
        sys.exit()

if __name__ == "__main__":
    main()
"""
1. Time would only refresh after 2 seconds.
2. Since time usually displays in 2 digits, change it to 1 would make the 0 before 1 digit disappear.
3. Multiple lines of clock would be next to each other like a column, which loses the sense of a counter.
4. NameError name 'sevseg' is not defined

"""