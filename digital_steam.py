import random, shutil, sys, time
# shutil does high-lv operations on files

MIN_STREAM_LENGTH = 2
MAX_STREAM_LENGTH = 20
PAUSE = 0.1
STREAM_CHARS = ['0', '1', '#', '$']

DENSITY = 0.03
WIDTH = shutil.get_terminal_size()[0] # get size of the terminal screen (columns and lines)
WIDTH -= 1
time.sleep(2)

def main():
    print("Ctrl C to exit")

    try:
        columns = [0] * WIDTH
        while True:
            for i in range(WIDTH):
                if columns[i] == 0:
                    if random.random() <= DENSITY:
                        columns[i] = random.randint(MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)
                if columns[i] > 0:
                    print(random.choice(STREAM_CHARS), end='')
                    columns[i] -= 1
                else:
                    print(' ', end='')
            print() # stuff shows in diagonal 
            sys.stdout.flush() # still no difference if comment out
                                # flush out stuff in buffer while normally it would wait
            time.sleep(PAUSE)

    except KeyboardInterrupt:
        print("Goodbye~")
        sys.exit()

if __name__ == "__main__":
    main()
"""
1. All blank spaces are replaced with dots. 
2. Exception has occurred: ValueError sleep length must be non-negative (time.sleep must be greater than negative)
3. Everything is dots.
4. Screen is filled with characters with no spaces
5. Columns slowly turns into a big screen of characters like in question 4.
"""

