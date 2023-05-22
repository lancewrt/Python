# contain class for insertion sorting the stack in ascending or descending order
from Bernal_Lance_Stack import Stack # import Stack class

sortI = Stack()      # create instance of Stack class 

class Sort():

    def sort(self):
        self.list = sortI.Stk.copy()        # create copy of the stack list so that the original wont be sorted
        for i in range(1, len(self.list)):  # start sorting at 1 and continue until the lenght of whole stack is reached
            key=self.list[i]                # make the index the basis for sorting
            j=i-1                           # 
            while j>=0 and key<self.list[j]:# compare value of key and the current index, 
                self.list[j+1]=self.list[j] # if key is lower, the value of index will be put in the next index
                j=j-1
            self.list[j+1]=key              # the greater value of will be the new key or basis for sorting
        return self.list                    # return the sorted stack

    def sortA(self):
        if sortI.Stk == []:                 # check if stack is empty
            print("The stack is empty.")
            input()
        else:
            print(Sort.sort(self))          # if stack is not empty print the sorted stack
            input()
 
    def sortD(self):
        if sortI.Stk == []:                 # check if stack is empty
            print("The stack is empty.")
            input()
        else:
            a = Sort.sort(self)[::-1]       
            print(a)                        # if stack is not empty print the sorted stack in reverse
            input()



    
                 

