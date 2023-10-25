import tkinter as tk
from tkinter import messagebox
import random


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.board = [" " for _ in range(9)]
        self.current_turn = "X"
        self.buttons = []
        self.create_board()
        self.window.mainloop()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.window, text="", font=("Helvetica", 20), width=3, height=1,
                               command=lambda j=i: self.button_clicked(j))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def button_clicked(self, index):
        if self.board[index] == " ":
            self.buttons[index].config(text=self.current_turn)
            self.board[index] = self.current_turn
            if self.check_win(self.current_turn):
                self.show_win_message(self.current_turn)
            elif " " not in self.board:
                self.show_draw_message()
            else:
                self.current_turn = "O"
                self.computer_move()

    def computer_move(self):
        index = self.find_best_move()
        self.buttons[index].config(text=self.current_turn)
        self.board[index] = self.current_turn
        if self.check_win(self.current_turn):
            self.show_win_message(self.current_turn)
        elif " " not in self.board:
            self.show_draw_message()
        else:
            self.current_turn = "X"

    def find_best_move(self):
        # Check if there exists a single move for the computer that will win the game
        for i in range(9):
            if self.board[i] == " " and self.check_win("O", i):
                return i

        # Check if there exists a single move for the player that will cause the computer to lose the game
        for i in range(9):
            if self.board[i] == " " and self.check_win("X", i):
                return i

        # Check if any of the corner spaces (spaces 0, 2, 6, or 8) are free
        corners = [0, 2, 6, 8]
        random.shuffle(corners)
        for corner in corners:
            if self.board[corner] == " ":
                return corner

        # Check if the center is free
        if self.board[4] == " ":
            return 4

        # Move on any of the side pieces (spaces 1, 3, 5, or 7)
        sides = [1, 3, 5, 7]
        random.shuffle(sides)
        for side in sides:
            if self.board[side] == " ":
                return side

    def check_win(self, player, index=None):
        if index is None:
            board = self.board
        else:
            board = self.board.copy()
            board[index] = player

        for i in range(0, 9, 3):
            if board[i] == board[i+1] == board[i+2] == player:
                return True

        for i in range(3):
            if board[i] == board[i+3] == board[i+6] == player:
                return True

        if board[0] == board[4] == board[8] == player:
            return True

        if board[2] == board[4] == board[6] == player:
            return True

        return False


if __name__ == '__main__':
    game = TicTacToe()
   
