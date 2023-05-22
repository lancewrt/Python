# Title : Caecar Cipher
# Author : Lance R. Bernal
# Date: 10-07-2022
# Description: A simple program to encrypt and decrypt text using caecar cipher. This program can cipher ascii values from 32 upto 122

import os

def clrscr(): # function for clearing the termninal
    if os.name == 'posix': 
        _= os.system('clear')
    else:
        _= os.system('cls')

def encrypt(): # function for encrypting the texts
    clrscr()
    divider()
    print("               Encryption       ")
    text = input("Enter word/text to be encrypted: ") # stores the string entered by user
    pin = int(input("Enter PIN to encrypt [ex. 1234]: ")) # stores the pin entered by user

    pin = pin % ord('z') # modulo the pin entered to the maximum ascii value which is ord('z') or 122
    textEncrypt = "" # stores the converted string
    #check = [] # stores ascii values of each character for checking

    for index in text: # loop for assigning ascii with shifted value for each character of string  
        asciiVal = ord(index) 
        asciiVal = asciiVal + pin 
        if asciiVal <= ord('z'):
            asciiVal = asciiVal
        else: # if the ascii value of a character exceeds ord('z'), it will be modulo-ed, 31 is added to start the shift at the minimum value of ord(' ') or 32
            asciiVal =  (asciiVal % ord('z')) + 31

        #check.append(asciiVal) # write each encrypted ascii value for checking
        textEncrypt += chr(asciiVal)

    clrscr()
    divider()

    #print(check) # display encrypted ascii values for checking
    print(" The encrypted text/word is:", textEncrypt) # display the encrypted string
    again()

def decrypt(): # function for decrypting the encrypted string
    clrscr()
    divider()
    print("               Decryption       ")
    text = input("Enter word/text to be decrypted: ") # stores the encrypted string
    pin = int(input("Enter PIN to decrypt [ex. 1234]: ")) # stores the pin entered by the user

    pin = pin % ord('z') # modulo the pin entered to the maximum ascii value which is ord('z') or 122
    textDecrypt = "" # stores the converted string
    #check = [] # stores ascii values of each character for checking

    for index in text: # loop for decrypting the string using the pin
        asciiVal = ord(index)
        asciiVal = asciiVal - pin
        if asciiVal >= ord(' '):
            asciiVal = asciiVal
        else: # if the ascii value of a character is less than ord(' ') or 32, 31 will be deducted and the ascii value will be modulo-ed to start the shift at ord(' ') or 32
            asciiVal = (asciiVal - 31) % ord('z')

        # check.append(asciiVal) # write each decrypted ascii value for checking
        textDecrypt += chr(asciiVal)

    clrscr()
    divider()
    # print(check) # display encrypted ascii values for checking
    print("The decrypted text/word is:", textDecrypt) # display the decrypted string
    again()

def divider(): # function to divide contents in terminal
    print(" ")
    print("*******************************************")
    print(" ")

def again(): # function for going back to main menu/page
    divider()
    choice = input(" Do you want to go to menu? [y/n]: ")
    if choice == 'y': # if user choose 'y', the program will go to menu, if not it will exit
        menu()
    else:
        exit()

def menu(): # main menu/page of program 
    clrscr()
    divider()
    print("                  Menu       ")
    print("         1. Encrypt Text")
    print("         2. Decrypt Text")
    print("         3. Exit")
    print(" ")
    choice = int(input("Enter you choice [1-3]: "))
    if choice == 1: # the user's choice corresponds a condtion, and the program will proceed accordingly
        encrypt()
    elif choice == 2:
        decrypt()
    else:
        exit()

menu() # calling of function main