



from random import choice

# why remove duplication?
# so in future we only need to update the code in one place
# so we won't forget to update code in all the place

valid_choices = ['rock', 'paper', 'scissors']

def winner(user_choice, computer_choice):
    return "OOPS - TODO"

if __name__ == "__main__":

    # ONLY RUN THE FOLLOWING CODE IF WE RUN THIS SCRIPT FROM THE COMMAND LINE
    # BUT NOT IF WE ARE IMPORTING SOME CODE FROM THIS FILE TO ANOTHER FILE
    # PREVENTS EXECUTION OF THE CODE BELOW

    #
    # USER SELECTION
    #

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in valid_choices:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice([valid_choices])
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    if u == "rock" and c == "rock":
        print("It's a tie!")
    elif u == "rock" and c == "paper":
        print("The computer wins")
    elif u == "rock" and c == "scissors":
        print("The user wins")

    elif u == "paper" and c == "rock":
        print("The computer wins")
    elif u == "paper" and c == "paper":
        print("It's a tie!")
    elif u == "paper" and c == "scissors":
        print("The user wins")

    elif u == "scissors" and c == "rock":
        print("The computer wins")
    elif u == "scissors" and c == "paper":
        print("The user wins")
    elif u == "scissors" and c == "scissors":
        print("It's a tie!")
