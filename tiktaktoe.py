import random

player, computer = "X", "O"

winners = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),
           (1,4,7),(2,5,8),(0,4,8),(2,4,6))

class TicTacTogame:

    def __init__(self):
        self.board = [" "]*9

    def print_board(self):
        for i, val in enumerate(self.board):
            end = " | "
            if i == 2 or i == 5:
                end = "\n-----------\n"
            elif i == 8:
                end = "\n"
            print(val, end=end)

    def can_move(self, move):
        if move in range(1, 10) and self.board[move-1] == " ":
            return True
        return False

    def can_win(self, player):
        win = True
        for tup in winners:
            win = True
            for idx in tup:
                if self.board[idx] != player:
                    win = False
                    break
            if win == True:
                break
        return win

    def make_move(self, player, move):
        # moved, win
        if self.can_move(move):
            self.board[move-1] = player
            win = self.can_win(player)
            return (True, win)
        return (False, False)

    def computer_move(self):
        for move in (5, 1, 3, 7, 9, 2, 4, 6, 8):
            if self.can_move(move):
                return self.make_move(computer, move)
        return self.make_move(computer, -1)

    def play(self):
        print("Order is:\n1 2 3\n4 5 6\n7 8 9")
        print(f"player is {player}, computer is {computer}")

        result = "Tie"
        while True:
            if self.board.count(player) + self.board.count(computer) == 9:
                break

            self.print_board()

            move = int(input("make your move [1-9]: "))
            moved, won = self.make_move(player, move)
            if not moved:
                print("invalid move! try again!")
                continue

            if won:
                result = "You win!"
                break

            _, won = self.computer_move()
            if won:
                result = "You lose!"
                break

        self.print_board()
        print(result)
            