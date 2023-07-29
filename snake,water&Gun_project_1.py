# SNAKE , WATER & GUN ......> GAME PROJECT
import random

def game(comp ,you):
    if comp == you:
        return None
    elif comp == 'S':
        if  you=='W':
            return False
        elif you == 'G':
            return True
    elif comp == 'W':
        if you=='G':
            return False
        elif you =='S':
            return True
    elif comp =='G':
        if you=='S':
            return False
        elif you=='W':
            return True
print("comp : snake (S) , water (W) , gun(G) ?")
randNo =random.randint(1,3)    #...>random tag is use for random working for computer to play the game
if randNo ==1:
    comp = 'S'
elif randNo == 2:
    comp ='W'
elif randNo == 3:
    comp='G' 

you = input("you: snake (S) , water (W) , gun(G) ?")
a = game(comp ,you)

# print(f"computer chose {comp}")
# print(f"you chose {you}")

if a== None:
    print("game is tie")
elif a:
    print("you win")   
else:
    print("you lose")     


