import random 
def main():
    play_game()
    ans = str(input("Do you want to play again? (Y/N) ")).lower()
    print("")
    while ans == 'y' or ans == 'yes':
        play_game()
        ans = str(input("Do you want to play again? (Y/N) ")).lower()
        print("")
    else:
        print("Thanks for playing! :)")

def play_game():
#user input is taken
    user_choice = str(input("Pick between 'rock', 'paper' or 'scissors': ")).lower()
    choice, random_num = pick_choice()
    num_user = 0
    while ((user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors")):
        if (user_choice == "rock"):
            num_user = 1
        elif (user_choice == "paper"):
            num_user = 2
        elif (user_choice == "scissors"):
            num_user = 3
        print("You picked: " + user_choice)
        print("Computer picked: " + choice)
        compare(num_user, random_num)
        break
    else:
        print("invalid input")
    print("")
    return()
  
def pick_choice():
#picks a choice from rock, paper or scissors
    random_num = random.randint(1,3)
    choice = ""
    if (random_num == 1):
        choice = "rock"
    elif (random_num == 2):
        choice = "paper"
    else:
        choice = "scissors"
    return(choice, random_num)
def compare(num_user, random_num):
    if (num_user == 1 and random_num == 2):
        print("Paper beats rock. You lose :(")
    elif (num_user == 2 and random_num == 3):
        print("Scissors beat paper. You lose :(")
    elif (num_user == 3 and random_num == 1):
        print("Rock beats scissors. You lose :(")
    elif (num_user == 2 and random_num == 1):
        print("Paper beats rock. You win :)")
    elif (num_user == 3 and random_num == 2):
        print("Scissors beat paper. You win :)")
    elif (num_user == 1 and random_num == 3):
        print("Rock beats scissors. You win :)")
    else:
        print("Its a tie")
    print("")
if __name__ == '__main__':
    main()
