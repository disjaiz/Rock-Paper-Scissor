import random

def winner(user_choice, comp_choice, choice_list):
    winner = ""
    if user_choice == comp_choice:
        return "draw"

    elif (user_choice == choice_list[0] and comp_choice == choice_list[1]) or \
        (user_choice == choice_list[1] and comp_choice==choice_list[2]) or \
            (user_choice == choice_list[2] and comp_choice == choice_list[0]):
        return "computer"
    
    return "user"

def game_start():
    choice_list = ["rock" , "paper", "scissor"]
    print("Choose between 'rock', 'paper', 'scissor'")
    user_choice = input("\nYour choice => ")

    # check invalid input by user
    while user_choice not in choice_list:
        print("Invalid choice! Please try again.")
        user_choice = input("\nYour choice => ")

    
    computer_choice = random.choice(choice_list)

    print("Computer'choice =>" , computer_choice)
    
    result = winner(user_choice, computer_choice, choice_list)
    if result == "draw":
        print("\nIts a draw 🙆‍♀️ ")
    elif result == "user":
        print("\nCongratulations, you WIN 😎")
    else: 
        print("\nYou lose! Better luck next time.")
    
    play_again = input("Do you want to play again? (yes or no): ")
    if play_again == "yes":
        game_start()
    

game_start()