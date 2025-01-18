import random, sys, time

PAUSE = 0.15

ROWS = [
    '    # #',
    '   #{}-{}#',
    '  #{}---{}#',
    ' #{}-----{}#',
    '#{}-------{}#',
    ' #{}-----{}#',
    '  #{}---{}#',
    '   #{}-{}#',
    '    # #',
    '   #{}-{}#',
    '  #{}---{}#',
    ' #{}-----{}#',
    '#{}-------{}#',
    ' #{}-----{}#',
    '  #{}---{}#',
    '   #{}-{}#',]

def main():

    try:
        print("Ctrl C to exit")
        time.sleep(2)
        rowIndex = 0

        while True:
            rowIndex += 1
            if rowIndex == len(ROWS):
                rowIndex = 0
            
            
        
            randomSelection = random.randint(1, 4)
            if randomSelection == 1:
                leftNuc, rightNuc = 'A', 'T'
            elif randomSelection == 2:
                leftNuc, rightNuc = 'T', 'A'
            elif randomSelection == 3:
                leftNuc, rightNuc = 'C', 'G'
            elif randomSelection == 4:
                leftNuc, rightNuc = 'G', 'C'
            # this fix the display of blank {} {}
            if rowIndex == 0 or rowIndex == 9:
                print(ROWS[rowIndex].format(leftNuc, rightNuc))
                continue

            print(ROWS[rowIndex].format(leftNuc, rightNuc))
            
            time.sleep(PAUSE)

    except KeyboardInterrupt:
        print("Bye")
        sys.exit()

if __name__ == "__main__":
    main()

"""
1. The program skips by 1 DNA pair until hit the list index out of range.
2. Only A,T pair appears.
3. Sleep length must be non-negative
"""