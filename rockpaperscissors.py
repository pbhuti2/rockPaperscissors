'''

Created on Feb 1, 2020

@author: pbhuti2
'''

import random

keepPlaying = True

while(keepPlaying == True):
    print("Welcome")
    print("First to 2 wins. Press q to quit. type in baby letters")
    #rock is 1, paper is 2, scissors is 3
   
    scoreComp = 0
    scorePlayer = 0
   
    while(scorePlayer < 2) and (scoreComp < 2):
        choiceComp = random.randint(1,3)
        choicePlayer = input("pick either rock, paper, or scissors!")
       
        if(choicePlayer == "q"):
            keepPlaying = False
            break
        elif((choicePlayer == "rock" ) and (choiceComp == 1)) or ((choicePlayer == "paper" ) and (choiceComp == 2)) or ((choicePlayer == "scissors" ) and (choiceComp == 3)):
            print("DRAAAW! (McCree Voice)")
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
           
        elif((choicePlayer == "rock" ) and (choiceComp == 2)) or ((choicePlayer == "paper" ) and (choiceComp == 3)) or ((choicePlayer == "scissors" ) and (choiceComp == 1)):
            print("You took an L 9_9")
            scoreComp = scoreComp + 1
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
        elif((choicePlayer == "rock" ) and (choiceComp == 3)) or ((choicePlayer == "paper" ) and (choiceComp == 1)) or ((choicePlayer == "scissors" ) and (choiceComp == 2)):
            print("GG YOU WON THIS ROUND")
            scorePlayer = scorePlayer + 1
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
        else :
            print("smh, ROCK PAPER OR SCISSORS! LOWERCASE")
           
    if (scorePlayer == 2):
            print("you actually won...")
         
           
    if (scoreComp == 2):
            print("you cant beat me im the CPU, you lost")
           
    print("Computer's Score: ", + scoreComp , "Your Score: ", + scorePlayer)
