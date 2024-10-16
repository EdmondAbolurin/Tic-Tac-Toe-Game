import tkinter as tk
from tkinter import messagebox

# Main Tic-Tac-Toe class
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.player = 'X'  # Player X starts
        self.buttons = [[None, None, None],  # 3x3 grid of buttons
                        [None, None, None],
                        [None, None, None]]
        self.create_board()
        
    def create_board(self):
        """Create a 3x3 grid of buttons"""
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(self.root, text="", font=('Arial', 24), width=5, height=2,
                                                   command=lambda r=row, c=col: self.click_button(r, c))
                self.buttons[row][col].grid(row=row, column=col)
        
        # Add a reset and exit button at the bottom
        reset_button = tk.Button(self.root, text="Reset Game", font=('Arial', 14), command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")
        
        exit_button = tk.Button(self.root, text="Exit Game", font=('Arial', 14), command=self.root.quit)
        exit_button.grid(row=4, column=0, columnspan=3, sticky="nsew")
        
    def click_button(self, row, col):
        """Handle a button click by marking it and switching players"""
        if self.buttons[row][col]['text'] == "" and not self.check_winner():
            self.buttons[row][col]['text'] = self.player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.player} wins!")
                self.disable_buttons()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.disable_buttons()
            else:
                # Switch player
                self.player = 'O' if self.player == 'X' else 'X'
    
    def check_winner(self):
        """Check if there is a winning combination"""
        for row in range(3):
            if self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2]['text'] != "":
                return True  # Row win
        for col in range(3):
            if self.buttons[0][col]['text'] == self.buttons[1][col]['text'] == self.buttons[2][col]['text'] != "":
                return True  # Column win
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True  # Diagonal win
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True  # Diagonal win
        return False
    
    def is_draw(self):
        """Check if the game is a draw"""
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]['text'] == "":
                    return False
        return True
    
    def disable_buttons(self):
        """Disable all buttons after the game ends"""
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state="disabled")
    
    def reset_game(self):
        """Reset the game to the initial state"""
        self.player = 'X'
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", state="normal")


# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
