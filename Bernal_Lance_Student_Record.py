# Title: Activity 2: Student Record 
# Author: Lance Bernal
# Date: 11-02-2022
# Description: A simpile program for encoding records of student. This program is capable of adding, viewing, updating, deleting, saving, reading, and sorting of entered recodrs.

import os   
import csv
import operator

def clear():    # function clear console
    os.system('cls')
def header():   # fuction for the header of program
    print("------------------------CLASS RECORD------------------------")
    print("\n")
def again():    # function for going back to menu
    choice = input("Do you want to go to menu [yes/no]? ")
    if choice == 'yes' or choice == 'y':
        menu()
    else:
        exit(0)

record = [] # list to store records
valid = ('1', '2', '3', '4', '5', '6', '7', '8', '9')   # valid input in menu

choices = """                            MENU          
    1. Add Student Grade
    2. View/Display All Student Record
    3. Search Student Record
    4. Update Student Record
    5. Delete Student Record
    6. Save Student Record to csv file
    7. Read Student Record from a csv file
    8. Sort Student by Average (Ascending/Descending Order)
    9. Quit
""" # to display in menu
aORd = """                            SORT GRADE
    1. Sort in Ascending
    2. Sort in Descending
""" # to display in sortGrade

def menu():
    while True:
        clear()
        header()
        print(choices)
        choice = input("Please enter your choice: ")    # asks user to enter their choice from the menu
        
        if choice not in valid:     # display an error if the choice is not on the accepted value
            print("ERROR: The input is not in the menu, try again. \n") 
        else:
            selection(choice)       # if choice is valid, it will proceed to selection

def selection(choice):      # take the choice as parameter then proceed accordingly
    if choice == '1':
        addGrade()
    elif choice == '2':
        viewGrade()
    elif choice == '3':
        searchRec()
    elif choice == '4':
        updateRec()
    elif choice == '5':
        deleteRec()
    elif choice == '6':
        saveFile()
    elif choice == '7':
        readFile() 
    elif choice == '8':
        sortGrade()
    elif choice == '9':
        clear()
        print("Goodbye! ")
        exit(0)

def addGrade():     # fuction for adding new record
    clear()
    header()
    num = int(input("Enter number of students: "))
    for i in range(num):    # loop for taking input from user
        clear()
        header()
        _name = (input("Enter the name: ")).upper()
        _math = (float(input("Enter grade in Mathematics: ")))
        _science = (float(input("Enter grade in Science: ")))
        _english = (float(input("Enter grade in English: ")))
        _average = round(((_math + _science + _english)/3),2)
        record.append([_name, _math, _science, _english, _average]) # append entered inputs in the list record
    again()

def viewGrade():    # function for displaying the records
    clear()
    header()
    i = 0
    if len(record) == 0:    # if there are no record, it will display an error
        print("ERROR: You have no records! ")
        again()
    else:                   # else, display all the records from the list
        while i < len(record): 
            print("NAME: " + record[i][0] + "\t\t MATH: ", record[i][1], " SCIENCE: ", record[i][2], " ENGLISH: ", record[i][3], " AVERAGE: ", record[i][4])
            i = i + 1
        again()

def searchRec():        # function for searching a record based on name
    clear()
    header()
    search = input("Enter name of student: ").upper()   
    for sublist in record:      # look through the lists until entered name is found
        if search in sublist:   # if name is found, display its record
            print("NAME: " + sublist[0] + "\t\t MATH: ", sublist[1], "SCIENCE: ", sublist[2], "ENGLISH: ", sublist[3], "AVERAGE: ", sublist[4])
            again()

    if search not in sublist:   # if the name entedred is not on the lists, display an error
        print("ERROR: " + search + " is not found in the student record!")
        _again = input("Do you want to enter again? [yes/no]: ") # ask if user wants to re-enter name
        if _again == 'yes' or _again == 'y':
            searchRec()
        else:
            again()
            
def updateRec():    # function for updating record
    clear()
    header()
    search = input("Enter name of student to update: ").upper()     # ask user for name of the record to be updated
    for sublist in record:  # look through the lists until name is found
        if search in sublist:   # if name is found, display prmpt, then ask the user to enter new info
            print("You will update the records of " + search)
            sublist[0] = input("Enter new name: ").upper()
            sublist[1] = float(input("Enter new grade in Math: "))
            sublist[2] = float(input("Enter new grade in Science: "))
            sublist[3] = float(input("Enter new grade in English: "))
            sublist[4] = round(((sublist[1] + sublist[2] + sublist[3])/3),2)
            again()
    if search not in sublist:   # if the name entered is not on the lists, display an error
        print("ERROR: " + search + " is not found in the student record!")
        _again = input("Do you want to enter again? [yes/no]: ")
        if _again == 'yes' or _again == 'y':
            updateRec()
        else:
            again()

def deleteRec():    # function for deleting a record
    clear()
    header()
    search = input("Enter name of student to delete record: ").upper()  # ask user the name whose record to be deleted
    for sublist in record:  # look through the lists until name is found
        if search in sublist:   # if name is found, remove the record, then display prompt
            record.remove(sublist)
            print("You deleted the record of " + search)
            again()

    if search not in sublist:   # if the name entered is not on the lists, display an error
        print("ERROR: " + search + " is not found in the student record!")
        _again = input("Do you want to enter again? [yes/no]: ")
        if _again == 'yes' or _again == 'y':
            deleteRec()
        else:
            again()

def saveFile(): # function for saving the record to a file
    clear()
    header()
    _fileName = input("Please enter file name: ")   # ask the user for the file name
    if ".csv" not in _fileName: # if the file extension is not .csv, make it .csv
        _fileName = str(_fileName + ".csv")
    with open(_fileName , 'w', encoding="ISO-8859-1", newline='') as file:  # open file as wtite 
        write = csv.writer(file)    # use csv to write the record to the file
        write.writerow(("NAME", "MATH", "SCIENCE", "ENGLISH", "AVERAGE"))   # Write the header of the .csv file
        write.writerows(record) # write the records in the rows of file
    print("The record has been saved!") # display prompt
    again()

def readFile(): # funtion for reading the saved file
    clear()
    header()
    _fileName = input("Please enter file name: ")   # ask the user for the name of the file
    if ".csv" not in _fileName:     # add .csv if the ectension is not .csv
        _fileName = str(_fileName + ".csv")
    try:    # if file is founf, open it in read mode
        file = open(_fileName, 'r')
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)
        file.close()
    except FileNotFoundError:       # display an error if file is not found
        print("ERROR: Wrong file or file path")
    again()

def sortGrade():    # function for sorting grade (ascending or descending)
    clear()
    header()
    print(aORd)
    _choice = input("Enter choice: ")
    if _choice == "1":
        record.sort(key= operator.itemgetter(4))    # sort using the 5th element(average) as the key
        print("The record has been sorted! ")
        again()
    elif _choice == "2":
        record.sort(reverse = True, key= operator.itemgetter(4)) # sort using the 5th element(average) as the key in descending
        print("The record has been sorted! ")
        again()

menu()