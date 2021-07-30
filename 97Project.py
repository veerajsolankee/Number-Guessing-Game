import random
number = random.randint(1, 9)
chances=0
print("Guess the number between 1 to 9 if you win you get a price if you lose you lose a chance you will get 5 chances ")
while chances < 5:
    guess=int(input("enter your guess"))
    if guess==number:
        print("congratulation")
        break
    elif guess<number:
        print("try a greater number ")
    elif guess>number:
        print("guess a lesser number ")    
    chances=chances-1
if chances>5:
        print("Game Over.The correct answer is number",number )        

