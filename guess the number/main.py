
from guessthenumber import guess_the_number

while True:
    txt = """Mini Games!!!
    - Guess The Number (1)
    - Rock, Paper, Scissors (2)
    - Wordle (3)
    - ConnectFour (4)
    - Tic Tac Toe (5)
Select a game (press a number or 'q' to quit): """
    value = input(txt)
    if value == "a":
        guess_the_number(100)