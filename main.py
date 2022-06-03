import random

game_item = ['r','p','s']

def playRps():
    while True:
        playerChoice = input(f"\ntype \"R\" for ROCK | \"p\" for PAPER | \"s\" for SCISORS\n")
        compChoice = random.choice(game_item)
        print(compChoice, playerChoice)
        if playerChoice in game_item:
            if playerChoice == compChoice:
                print(f"Player{playerChoice}: Comp{compChoice} - Its a tie 🤝!")
                playRps()
            elif playerChoice == game_item[0]:
                if compChoice == game_item[1]:
                    print(f"\nPlayer: {playerChoice} | Comp: {compChoice} - Paper beats Rock - Comp Wins 😞\n")
                else:
                    print(f"\nPlayer: {playerChoice} | Comp: {compChoice} - Rock beats Scissors - You Win 🏆\n")
            elif playerChoice == game_item[1]:
                if compChoice == game_item[0]:
                    print(f"\nPlayer: {playerChoice} | Comp: {compChoice} - Paper beats Rock - You Win 🏆\n")
                else:
                    print(f"\nPlayer: {playerChoice} | Comp: {compChoice} - Scissors beats paper - Comp Wins😞\n")
            else:
                if compChoice == game_item[0]:
                    print(f"\nPlayer: {playerChoice} | Comp: {compChoice} - Rock beats scissors - Comp Wins😞\n")
                else:
                    print(f"\nPlayer: {playerChoice} | Comp: {compChoice} - Scissors beats paper - You Win 🏆\n")
        else:
            print(f"\nInvalid input.\n")
            playRps()
        
playRps()