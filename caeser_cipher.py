try:
    import pyperclip
except ImportError:
    pass

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
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
            # translated = translated + symbol
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
"""
1. Then the encrypted/decrypted message would only be presented in "ABC".
2. There would be 0 shifts and it means it stays the same.
3. UnboundLocalError
4. NameError: key is not defined
5. The translated message would stay the same since there is no shift in its message.
"""