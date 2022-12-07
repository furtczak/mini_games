import random

# Generate a random number between 1 and 10
secret_num = random.randint(1, 10)

# Prompt the user to enter a number
guess = int(input("Enter a number between 1 and 10: "))

# Keep prompting the user to enter a number until they guess the secret number
while guess != secret_num:
    print("Wrong, try again!")
    guess = int(input("Enter a number between 1 and 10: "))

# If the user guesses the secret number, congratulate them
print("Congratulations, you guessed the secret number!")