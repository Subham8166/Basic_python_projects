# THE PERFECT GUESS
import random
randno = random.randint(1,100)
user = None
guesses = 0
while(user != randno):
    user = int(input("Enter your Guess: "))
    guesses += 1
    if (user == randno):
        print("right guess")
    else:
        if(user > randno):
            print("your guess is wrong , Enter the  smaller no.")
        else:
            print("your guess is wrong , Enter the  larger no.")       

print(f"you guessed the no. in {guesses} guesses")
