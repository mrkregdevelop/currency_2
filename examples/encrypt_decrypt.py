'''
A
Taras
['T', 'a', 'r', 'a', 's']
[84, 97, 114, 97, 115] + 1
[85, 98, 115, 98, 116]
['U', 'b', 's', 'b', 't']
Ubsbt
B

Ubsbt
['U', 'b', 's', 'b', 't']
[85, 98, 115, 98, 116] - 1
[84, 97, 114, 97, 115]
['T', 'a', 'r', 'a', 's']
Taras

A -||||-> B
'''

KEY = 2


def encrypt(message: str):
    message = list(message)
    encrypted_message = ''

    for char in message:
        encrypted_message += chr(ord(char) + KEY)

    return encrypted_message


def decrypt(encrypted_message: str):
    message = list(encrypted_message)
    encrypted_message = ''

    for char in message:
        encrypted_message += chr(ord(char) - KEY)

    return encrypted_message
