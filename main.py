from rps import rock_paper_scissors
from guessthenumber import guess_the_number
from worlde import Wordle
from connect_4 import Connectfour
from tiktaktoe import TicTacTogame
while True:
    txt = """Mini Games!!!
    - Guess The Number (1)
    - Rock, Paper, Scissors (2)
    - Wordle (3)
    - ConnectFour (4)
    - Tic Tac Toe (5)
Select a game (press a number or 'q' to quit): """
    value = input(txt)
    if value == "1":
        guess_the_number(100)
    if value =="2":
        rock_paper_scissors()
    if value =="3":
        game = Wordle()
        game.play()
    if value =="4":
        game = Connectfour()
        game.play()    
    if value =="5":
        game = TicTacTogame()
        game.play()  
    else:
        break