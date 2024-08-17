import sys

original_stdout = sys.stdout

def main():
    # https://www.geeksforgeeks.org/ways-to-save-python-terminal-output-to-a-text-file/
    with open("diamondText.txt", 'w') as file:
        sys.stdout = file
        for diamondSize in range(0, 10):
            displayOutlineDiamond(diamondSize)
            print()
            displayFilledDiamond(diamondSize)
            print()

def displayOutlineDiamond(size):
    for i in range(size):
        print(' ' * (size - i - 1), end='')
        print('/',end='')
        print('@' * (i * 2), end='')
        print('\\')

    for i in range(size):
        print(' ' * i, end='')
        print('\\', end='')
        print(' ' * ((size - i - 1) * 2), end='')
        print('/')

def displayFilledDiamond(size):
    for i in range(size):
        print(' ' * (size - i - 1), end='')
        print('/' * (i + 1), end='')
        print('\\' * (i + 1))

    for i in range(size):
        print(' ' * i, end='')
        print('\\' * (size - i), end='')
        print('/' * (size - i))

if __name__ == "__main__":
    main()

"""
1. The top right when creating the outline will be @ instead of \
2. The inner diamond would be filled with @ instead of blank space but only half of the diamond.
3. The size of the diamond is increased.
4. The outline would be overlapped with triangles.
"""