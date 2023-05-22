import random

tries = 1
num = int(random.randint(0,100))
guess = int(input("Please Enter a number from 1-100: "))
print(num)

while(tries < 5):
    if guess < num:
        print("Your guess is lower than the generated number")
        guess = int(input("Please enter a higher number: "))
        tries = tries + 1
    elif guess > num:
        print("Your guess is higher than the generated number")
        guess = int(input("Please enter a lower number: "))
        tries = tries + 1
    else:
        break

if guess == num:
    print("Congratulations your guess is correct the number is", num)
else:
    print("Sorry your guesses are wrong")
