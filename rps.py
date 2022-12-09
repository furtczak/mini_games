import random

def rock_paper_scissors():
    print("Let's plat Rock Paper Scissors")

    r="rock"
    p="paper"
    s="scissors"
    all_choices = [r,p,s]

    user = input(f"Enter a choice({r},{p},{s}): ") 

    if user not in all_choices:
        print("invalid choice")
        return
    computer= random.choice(all_choices)

    print(f"Users chose {user}, computer chose {computer}" )

    if user == computer:
        print("Tie")
    elif (user == r and computer == s) or (user ==p and computer== r) or (user == s and computer == r):
        print("You won")
    else:
        print("You lost")