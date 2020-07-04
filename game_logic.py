import random
def game_logic(i):
    options = ["Rock", "Paper", "Scissors"]
    result = random.choice(options)

    if (i == result):
        print("Computer Chose: " + result)
        print("Draw")
    elif (i == "Rock") and (result == "Scissors"):
        print("Computer Chose: " + result)
        print("You Win!")
    elif ( i == "Scissors") and (result == "Paper"):
        print("Computer Chose: " + result)
        print("You Win!")
    elif ( i == "Paper") and (result == "rock"):
        print("Computer Chose: " + result)
        print("You Win!")
    else:
        print("Computer Chose: " + result)
        print("You lose :(")
