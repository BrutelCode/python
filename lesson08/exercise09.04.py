from random import seed
from random import randrange
from datetime import datetime  # all 3 at the beginning

seed(datetime.now())  # once, before randint call

round = 0
score = [0, 0]  # Player, computer
history = []
while True:
    round += 1
    print("Round " + str(round))

    # Eisodos xristi
    player_input = int(input("Choose (0-rock, 1-scissors, 2-paper): "))
    while player_input not in [0, 1, 2]:
        print("Wrong input. Choices: 0-rock, 1-scissors, 2-paper")
        player_input = int(input("Choose (0-rock, 1-scissors, 2-paper): "))

    # Epilogi ipologisti
    computer_random = randrange(3)  # Random number from 0 to 2 (0-rock, 1-scissors, 2-paper)

    # Elegxos toy poios nikise
    diff = player_input - computer_random

    if diff == -1 or diff == 2:
        winner = "player"
    elif diff == 1 or diff == -2:
        winner = "computer"
    else:
        winner = "no winner"

    # Diorthosi tou skor
    if winner == "player":
        score[0] += 1
    elif winner == "computer":
        score[1] += 1


    # enimerwsi tou istorikou
    history.append("Round " + str(round) + ": Player: " + str(player_input) + ", Computer: " + str(computer_random) + ", Score: " + str(score[0]) + "-" + str(score[1]))


    # Ektypwsi toy nikiti kai tou skor
    print("Computer picks: " + str(computer_random))
    print("Player-Computer: " + str(score[0]) + "-" + str(score[1]))

    if score[0] == 3:
        print("Player wins! ")
        print("")
        for history_item in history:
            print(history_item)
        break
    elif score[1] == 3:
        print("Computer wins! ")
        print("")
        for history_item in history:
            print(history_item)
        break

    print("====================\n")
