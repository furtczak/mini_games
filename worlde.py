import random
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
        delf.guess_dict ={
            0:[""]*5,
            1:[""]*5,
            2:[""]*5,
            3:[""]*5,
            4:[""]*5,
        }