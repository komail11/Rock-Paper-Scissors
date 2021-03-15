import random
import time 
#Creating title
text = "Rock Paper Scissors"
title = text.center(225,"#")
print(title)

#Implementing game
def rps ():
    rnd = int(input("How many rounds of games do you want to play ?\n"))
    three_choices = ["Rock","Paper","Scissors"]
    count_w = 0
    count_l = 0

    while True:
        if count_w == rnd or count_l == rnd:
            break
        user = input("Input: ")
        ai = random.choice(three_choices)
        print("AI: ",ai)
    
        if user == "Rock":
            if ai == user:
                pass
            elif ai == "Paper":
                count_l += 1
            elif ai == "Scissors":
                count_w += 1

        if user == "Paper":
            if ai == user:
                pass
            elif ai == "Rock":
                count_w += 1
            elif ai == "Scissors":
                count_l += 1
            
        if user == "Scissors":
            if ai == user:
                pass
            elif ai == "Rock":
                count_l += 1      
            elif ai == "Paper":
                count_w += 1
               

    if count_w > count_l:
        print("User has won")
    else:
        print("AI has won")



#Rematch
While True:
    rematch = input("Would you like to play again ? \n")
    if rematch == "Yes":
        rps()
    elif rematch == "No":
        quit()

