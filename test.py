list = ["r","p","s"]

rule1 ="rock" > "scissors"

rule2 = "paper" > "rock"

rule3 = "scissors" > "paper"

print(rule1)

import random

game_item = ['r','p','s']


gameTry = True

tries = 0
compChoice = random.choice(game_item)

print(compChoice)

def playRps():
    while gameTry:
        playerChoice = input(f"\n\ntype \"R\" for ROCK | \"p\" for PAPER | \"s\" for SCISORS\n")

        print(compChoice, playerChoice)
        if playerChoice in game_item:
            if playerChoice == compChoice:
                print(f"Player{playerChoice}: Comp{compChoice} - Its a tie ! Play another game")
                playRps()
            elif playerChoice == game_item[0]:
                if compChoice == "p":
                    print(f"\nPlayer: {playerChoice} | Comp: {compChoice} - Paper beats Rock - Comp Wins\n")
                if compChoice == "s":
                    print(f"\nPlayer: {playerChoice} | Comp: {compChoice} - Paper beats Rock - Comp Wins\n")
                else:
                    print(f"\nPlayer: {playerChoice} | Comp: {compChoice} - Its a draw\n")
            elif playerChoice == game_item[1]:
                if compChoice == game_item[0]:
                    print(f"\nPlayer: {playerChoice} | Comp: {compChoice} - Paper beats Rock - You Win\n")
                else:
                    print(f"\nPlayer: {playerChoice} | Comp: {compChoice} - Scissors beats paper - Comp Wins\n")
            else:
                if compChoice == game_item[0]:
                    print(f"\nPlayer: {playerChoice} | Comp: {compChoice} - Rock beats scissors - Comp Wins\n")
                else:
                    print(f"\nPlayer: {playerChoice} | Comp: {compChoice} - Scissors beats paper - You Win\n")
        else:
            print("\nInvalid input. Please type \"R\" for ROCK || \"p\" for PAPER || \"s\" for SCISORS \n")
        
        

        print(tries)

    # if gameTry == tries:
    #     print("you've had your five(5) tries,  ")

playRps()

print("hello here")