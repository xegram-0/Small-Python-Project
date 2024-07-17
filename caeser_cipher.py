try:
    import pyperclip
except ImportError:
    pass

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def main():

    while True:
        print("(E)ncrypt or (D)ecrypt?")
        response = input("> ").lower()

        if response.startswith('e'):
            mode = 'encrypt'
            break
        elif response.startswith('d'):
            mode = 'decrypt'
            break
        print("Please select mode (press e or d)")

    while True:
        maxKey = len(SYMBOLS) - 1
        print(f"Enter the key from 0 to {maxKey} for the mode")
        response = input("> ").upper()
        if not response.isdecimal():
            continue
        if 0 <= int(response) < len(SYMBOLS):
            key = int(response)
            break

    print(f"Enter the message you want to {mode}")
    message = input("> ").upper()
    # message = meassage.upper()

    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = num - key

            if num >= len(SYMBOLS):
                num = num - len(SYMBOLS)
            elif num < 0:
                num = num + len(SYMBOLS)

            translated = translated + SYMBOLS[num]
        else:
            translated = translated + symbol
    print(translated)

    try:
        pyperclip.copy(translated)
        print("Your translated message is copied to the clipboard.")
    except:
        pass
if __name__ == "__main__":
    main()

