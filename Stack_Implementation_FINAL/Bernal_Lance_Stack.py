# Contains methods for the push, pop, peek, display, and clear

class Stack():

    Stk = []        # class variable containing the elements entered

    def __init__(self):     # instantiate class varible Stk
        Stack.Stk = []
    
    def isEmpty(self):      # method for checking if the list is empty
        if self.Stk == []:
            return True
        else:
            return False
    
    def push(self, element):    # method for adding element entered to the list
        self.Stk.append(element)
        print("" + element +" was inserted...")
        input()
    
    def pop(self):      # method for deleting the uppermost element 
        if self.isEmpty():
            print("The stack is empty.")
            input()
        else:
            print("Deleted element is: ", self.Stk.pop())
            input()
    
    def peek(self):     # method for cheking the uppermost element
        if self.isEmpty():
            print("The stack is empty.")
            input()
        else:
            print("The element last entered is: ", self.Stk[-1])
            input()
    
    def display(self):  # method for displaying all elements of stack list
        if self.isEmpty():
            print("The stack is empty.")
            input()
        else:
            a = self.Stk[::-1]
            print("The stack elements are: ")
            print(a)
            input()

    def clear(self):    # method for deleting all elements of the stack list
        if self.isEmpty():
            print("The stack is empty.")
            input()
        else:
            Stack.Stk = []
            print("Stack was cleared.")
            input()





