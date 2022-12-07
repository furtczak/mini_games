import random

def guess_the_numer(x):
    print("Let's play guess the number")

    random_number = random.randint(0,x)

    num_guesses = 0
    while True:
        guess=int(input(f"guess the number in range 0-{x}"))
        num_guesses +=1

        if guess == random_number:
            print(f"Congrats, The looking number is {x}")
            break
        elif guess < random_number:
            print("Too low")
        else:
            print("Too high ")