
print("Enter the message you want to decypt")
message = input("> ")

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = num - key
            if num <0:
                num = num + len(SYMBOLS)
            translated = translated + SYMBOLS[num]
        else:
            translated = translated + symbol
    print(f"Key #{key}: {translated}")
"""
1. NameError: translated is not defined.
2. The symbol would not be translated.
3. It would produce a number of encrypted messages based on the number of characters in SYMBOLS.
It would be a miracle if this creates another meaningful word.
"""
