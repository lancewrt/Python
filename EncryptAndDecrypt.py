# Program for encryption and decryption of text



text = input("Enter the word/text to encrypt: ")
password = int(input("Enter PIN (ex. 1234): "))
code = ""
password = password % len(password)

for i in text:
    textASCII = ord(i)
    encrypText = textASCII + password
    if encrypText > ord('~'):
        encrypText = ord(' ') + password -\
            (ord('~') - textASCII + 1)
    code += chr(encrypText)
print(code)


text = input("Enter the word/text to decrypt: ")
password = int(input("Enter the PIN to decrypt: "))
code = ""
password = password % len(password)

for i in text:
    textASCII = ord(i)
    decrypText = textASCII - password
    if decrypText < ord(' '):
        decrypText = ord('~') - \
            (password - (32 - textASCII + 1))
    code += chr(decrypText)
print(code)