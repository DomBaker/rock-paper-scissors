import random
def game_logic(i):
    options = ["rock", "paper", "scissors"]
    result = random.choice(options)

    if (i == result):
        print("Computer Chose: " + result.capitalize())
        print("Draw")
    elif (i == "rock") and (result == "scissors"):
        print("Computer Chose: " + result.capitalize())
        print("You Win!")
    elif ( i == "scissors") and (result == "paper"):
        print("Computer Chose: " + result.capitalize())
        print("You Win!")
    elif ( i == "paper") and (result == "rock"):
        print("Computer Chose: " + result.capitalize())
        print("You Win!")
    else:
        print("Computer Chose: " + result.capitalize())
        print("You lose :(")
