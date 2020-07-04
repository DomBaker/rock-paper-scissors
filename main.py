from game_logic import game_logic

def main():
    
    user_input = input("Enter Rock, Paper or Scissors (case does not matter): ")

    if (user_input.lower() == "rock") or (user_input.lower() == "paper") or (user_input.lower() == "scissors"):
        game_logic(user_input.lower())   
    else:
        print("Please enter either 'Rock','Paper','Scissors' capitalisation does not matter.")
        

if __name__ == "__main__":
    main()
