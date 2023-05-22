import os
def clear():        # fuction for clearing the console
    os.system('cls')

def main():
    while True:     
        stack = []      # list for storing the delimiters
        clear()         # clear console
        print("**************MATCHING DELIMITERS**************")
        print(" ")
        exp = input("Enter expression: ")       # ask the user for input
        check(exp, stack)  # pass parameters to method check
        if stack == []:     # if stack is empty execute the statement
            print("The expression " +exp+ " is balanced")
        elif '[' in stack or '{' in stack or '(' in stack:               # if stack contains '[' '{' or '(' execute the statement
            print("Missing closing delimiter")
            print("The expression " +exp+ " is not balanced")
        else:                                                            # else execute this statement
            print("Missing opening delimiter")
            print("The expression " +exp+ " is not balanced")
            
        choice = input("Do you want to try again? [yes/no]: ") 
        if choice == 'y' or choice == 'yes':
            continue
        else:
            print("Goodbye!")
            break

def pairs(open, close): # function for determining correct opening and closing delimiter
    if open == '[' and close == ']':
        return True
    if open == '{' and close == '}':
        return True
    if open == '(' and close == ')':
        return True
    return False

def check(exp, stack): # function to append or pop stack 
    for index in range(len(exp)):       # loop through each element of the entered expression
        if exp[index] == '[' or exp[index] == '{' or exp[index] == '(': # if opening demiter is found, append it to stack
            stack.append(exp[index])
        elif exp[index] == ']' or exp[index] == '}' or exp[index] == ')': 
            if stack == []:                                                # if closing delimiter is found and the stack is empty, append. 
                stack.append(exp[index])
            elif pairs(stack[-1], exp[index] or len(stack) != 0):          # if closing delimiter is found and the stack is not empty, pop.
                stack.pop()
            else:
                return False

main()