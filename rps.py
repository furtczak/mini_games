

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