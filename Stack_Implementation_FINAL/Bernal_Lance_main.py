# Title: StackList Implementation
# Author: Lance Bernal
# Date: 11-10-2022
# Description: Implement stack list with the following functions: PUSH, POP, PEEK, DISPLAY STACKS, SORT STACK (ASCENDING), SORT STACK (DESCENDING), and CLEAR.

import os
from Bernal_Lance_Stack import Stack        # import Stack class from Bernal_Lance_Stack
from Bernal_Lance_sorting import Sort       # import Sort class from Bernal_Lance_sorting

sort = Sort()       # create instance of class Sort
s = Stack()         # create instance of class Stack


def clear():    # function clear console
    os.system('cls')

def header():   # fuction for the header of program
    print("------------------------STACK LIST------------------------")

valid = ('1', '2', '3', '4', '5', '6', '7', '0')    # a tuple of valid inputs (for checking if input is valid)

# menu list
choices = """                            MENU       
    1. PUSH
    2. POP
    3. PEEK
    4. DISPLAY
    5. SORT STACK (ASCENDING)
    6. SORT STACK (DESCENDING)
    7. CLEAR STACK
    0. QUIT

"""

def menu():     # function for displaying menu and getting choice of user
    while True:
        clear()
        header()
        print(choices)
        choice = input("Please enter your choice [ex. 1]: ")
        if choice not in valid:     # checks if input is valid if not display an error
            print("ERROR: Invalid input! Press [ENTER] to re-enter")
            input()
            menu()
        else:
            selection(choice)


def selection(choice):      # take the choice as parameter then proceed accordingly
    if choice == '1':
        clear()
        header()
        element = input("Enter element to push: ")
        s.push(element) # pass the entered element to push method in class Stack
    elif choice == '2':
        clear()
        header()
        s.pop()
    elif choice == '3':
        clear()
        header()
        s.peek()
    elif choice == '4':
        clear()
        header()
        s.display()
    elif choice == '5':
        clear()
        header()
        sort.sortA()
    elif choice == '6':
        clear()
        header()
        sort.sortD()
    elif choice == '7':
        clear()
        header()
        s.clear() 
    elif choice == '0':
        clear()
        header()
        print("Goodbye! ")
        exit(0)

menu()
