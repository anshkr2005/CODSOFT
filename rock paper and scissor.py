import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.config(bg='lightblue')

        self.user_score = 0
        self.computer_score = 0

        self.choices = ['r', 'p', 's']
        self.choices_dict = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors", font=('Helvetica', 14), bg='lightblue')
        self.label.pack(pady=20)

        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play('r'), height=2, width=10, bg='lightgray')
        self.rock_button.pack(side=tk.LEFT, padx=20)

        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play('p'), height=2, width=10, bg='lightgray')
        self.paper_button.pack(side=tk.LEFT, padx=20)

        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play('s'), height=2, width=10, bg='lightgray')
        self.scissors_button.pack(side=tk.LEFT, padx=20)

        self.score_label = tk.Label(self.root, text="Score: You - 0, Computer - 0", font=('Helvetica', 12), bg='lightblue')
        self.score_label.pack(pady=20)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        result_text = f"User choice: {self.choices_dict[user_choice]}\nComputer choice: {self.choices_dict[computer_choice]}\n"

        if user_choice == computer_choice:
            result_text += "It's a tie!"
        elif (user_choice == 'r' and computer_choice == 's') or \
             (user_choice == 'p' and computer_choice == 'r') or \
             (user_choice == 's' and computer_choice == 'p'):
            result_text += "You win this round!"
            self.user_score += 1
        else:
            result_text += "Computer wins this round!"
            self.computer_score += 1

        self.score_label.config(text=f"Score: You - {self.user_score}, Computer - {self.computer_score}")

        # Adding a simple animation effect for the result
        self.animate_result(result_text)

    def animate_result(self, result_text):
        # Create a toplevel window to show the animation
        animation_window = tk.Toplevel(self.root)
        animation_window.geometry("300x150")
        animation_window.title("Round Result")
        animation_window.config(bg='lightblue')

        result_label = tk.Label(animation_window, text=result_text, font=('Helvetica', 12), bg='lightblue')
        result_label.pack(pady=20)

        # Animation effect: gradually change the background color
        def change_bg_color(step=0):
            colors = ['#FFCCCC', '#FF9999', '#FF6666', '#FF3333', '#FF0000']
            if step < len(colors):
                result_label.config(bg=colors[step])
                animation_window.after(100, change_bg_color, step + 1)
            else:
                animation_window.after(1500, animation_window.destroy)

        change_bg_color()

def main():
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
