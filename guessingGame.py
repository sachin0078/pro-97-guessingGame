import random

number =(random.randint(1,5))

print("Number guessing game")
print("Guess a number (between 1 and 5")
guess=int(input("Enter your guess:- "))
if(guess == number):
    print("Congratulation YOU WON!!!")
else:
    print("YOU LOSE!!! The number is",number)