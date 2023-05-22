
from fileinput import filename
import os
import csv
from itertools import zip_longest
import operator


def clear():
    os.system('cls')
def header():
    print("------------------------CLASS RECORD------------------------")
    print("\n")
def again():
    choice = input("Do you want to go to menu [yes/no]? ")
    if choice == 'yes' or choice == 'y':
        menu()
    else:
        exit(0)


name = []
math = []
science = []
english = []
average = []
record = [name, math, science, english, average]

    


valid = ('1', '2', '3', '4', '5', '6', '7', '8', '9')

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
"""
aORd = """                            SORT GRADE
    1. Sort in Ascending
    2. Sort in Descending
"""


def menu():
    while True:
        clear()
        header()
        print(choices)
        choice = input("Please enter your choice: ")
        
        if choice not in valid:
            print("ERROR: The input is not in the menu, try again. \n") 
        else:
            selection(choice)

def selection(choice):
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

def addGrade():
    clear()
    header()

    num = int(input("Enter number of students: "))
    for i in range(num):
        name.append(input("Enter the name: "))
        math.append(float(input("Enter grade in Mathematics: ")))
        science.append(float(input("Enter grade in Science: ")))
        english.append(float(input("Enter grade in English: ")))
        average.append(round(((math[i] + science[i] + english[i])/3), 2))
    
    again()

def viewGrade():
    clear()
    header()
    i = 0
    while i < len(name):
        print("NAME: " + name[i] + "\t\tMATH: ", math[i],"   SCIENCE: ", science[i], "ENGLISH: ", english[i], "AVERAGE: ", average[i])
        i = i+1
    again()

def searchRec():
    clear()
    header()
    search = input("Enter name of student: ")
    if search not in name:
        print("" + search + " is not found in the student record!")
        _again = input("Do you want to enter again? [yes/no]: ")
        if _again == 'yes' or _again == 'y':
            searchRec()
        else:
            again()
    else:
        i = name.index(search)
        print("NAME: " + name[i] + "\t\tMATH: ", math[i],"   SCIENCE: ", science[i], "ENGLISH: ", english[i], "AVERAGE: ", average[i])
    again()

def updateRec():
    clear()
    header()
    search = input("Enter name of student to update record: ")
    if search not in name:
        print("" + search + " is not found in the student record!")
        _again = input("Do you want to enter again? [yes/no]: ")
        if _again == 'yes' or _again == 'y':
            updateRec()
        else:
            exit(0)
    else:
        i = name.index(search)
        print("You will update the record of " + search)
        name[i] = input("Enter new Name: ")
        math[i] = float(input("Enter new grade in Mathematics: "))
        science[i] = float(input("Enter new grade in Science: "))
        english[i] = float(input("Enter new grade in English: "))
    again()

def deleteRec():
    clear()
    header()
    search = input("Enter name of student to delete record: ")
    if search not in name:
        print("" + search + " is not found in the student record!")
        _again = input("Do you want to enter again? [yes/no]: ")
        if _again == 'yes' or _again == 'y':
            deleteRec()
        else:
            exit(0)
    else:
        i = name.index(search)
        _choice = input("You will delete all records of" + search + ", continue? [yes/no] ")
        if _choice == 'yes' or choice == 'y':
            name.pop(i)
            math.pop(i)
            science.pop(i)
            english.pop(i)
            print("" + search + "'s record has been deleted")
            again()
        else:
            menu()

def saveFile():
    clear()
    header()
    _fileName = input("Please enter file name: ")
    if ".csv" not in _fileName:
        _fileName = str(_fileName + ".csv")
    with open(_fileName , 'w', encoding="ISO-8859-1", newline='') as file:
        write = csv.writer(file)
        write.writerow(("NAME", "MATH", "SCIENCE", "ENGLISH", "AVERAGE"))
        export_record = zip_longest(*record, fillvalue = '')
        write.writerows(export_record)
    print("The record has been saved!")
    again()

def readFile():
    clear()
    header()
    _fileName = input("Please enter file name: ")
    if ".csv" not in _fileName:
        _fileName = str(_fileName + ".csv")
    try:
        file = open(_fileName, 'r')
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)
        file.close()
    except FileNotFoundError:
        print("Wrong file or file path")
    again()

def sortGrade():
    clear()
    header()
    print(aORd)
    _choice = input("Enter choice: ")
    if _choice == "1":
        for i in average:
            average.sort
        record.sort(key = operator.itemgetter())
        print(record)
        again()
        #for index in average:
         #   print()


menu()