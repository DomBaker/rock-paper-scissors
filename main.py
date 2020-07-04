from game_logic import game_logic

def main():
    
    user_input = input("Enter Rock, Paper or Scissors: ")
    if (user_input != "Rock") or (user_input != "Paper") or (user_input != "Scissors"):
        print("Please enter either 'Rock','Paper','Scissors'")
    else:
        game_logic(user_input)

if __name__ == "__main__":
    main()