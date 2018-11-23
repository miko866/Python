rot = int(input('Enter the key: '))
action = input('Would do you [e]ncrypting or [d]ecrypting?: ')
data = input('Get text: ')

if action == 'e' or action == 'encrypting':
    text = ''
    for char in data:
        char_ord = ord(char)
        if 32 <= char_ord <= 126: # create alphabet
            char_ord -= 32
            char_ord += rot # rotate into the right == encrypting
            char_ord %= 94
            char_ord += 32
            text += chr(char_ord)
        else:
            text += char
    print("Code: '{}'".format(text))
elif action == 'd' or action == 'decrypting':
    text = ''
    for char in data:
        char_ord = ord(char)
        if 32 <= char_ord <= 126:
            char_ord -= 32
            char_ord -= rot # rotate into the left == decrypting
            char_ord %= 94
            char_ord += 32
            text += chr(char_ord)
        else:
            text += char
    print("Text: '{}'".format(text))
else:
    print('Error. Try again.')