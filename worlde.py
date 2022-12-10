import random
from rich import print
word =("awake",
"blush",
"focal",
"evade",
"serve",
"model",
"karma",
"grade",
"quiet")




class Wordle:
    def __init__(self):
        self.word = random.choice(word)
        self.num_guesses=0
        self.guess_dict ={
            0:[""]*5,
            1:[""]*5,
            2:[""]*5,
            3:[""]*5,
            4:[""]*5,
        }
    
    
    def draw_board(self):
        for guess in self.guess_dict.values():
            print(" | ".join(guess))
            print("=======")
    
    
    
    
    def get_user_input(self):
        user_guess = input("enter a 5 letter word: ")
        while len(user_guess) != 5:
            user_guess = input("now valid, enter a 5 letter word")
    
        user_guess = user_guess.lower()
        for idx, char in enumerate(user_guess):
            if char in self.word:
                if char == self.word[idx]:
                    char = f"[gree]{char}[/]" # gree
                else:
                    char = f"[yellow]{char}[/]" # yellow
            self.guess_dict[self.num_guesses][idx]= char

        self.num_guesses += 1
        return user_guess
    
    
    
    def play(self):
        while True:
            self.draw_board()
            user_guess = self.get_user_input()

            if user_guess == self.word:
                self.draw_board()
                print(f"You win, the word was {self.word}")
                break
            if self.num_guesses > 5:
                self.draw_board()
                print(f"You lost, the word was {self.word}")
                break
        