from logging import root
import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(u, c):
    if u == c:
        return "tie"
    elif (u == "rock" and c == "scissors") or \
         (u == "scissors" and c == "paper") or \
         (u == "paper" and c == "rock"):
        return "user"
    else:
        return "computer"

def play_round(user_choice):
    global user_wins, computer_wins, rounds, series_limit
    
    rounds += 1
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    if result == "user":
        user_wins += 1
        status = "You win this round! 😎😀"
    elif result == "computer":
        computer_wins += 1
        status = "Computer wins this round! 😏😏"
    else:
        status = "😌 It's a tie! 😌"
    
    score_label.config(text=f"Score - You: {user_wins} | Computer: {computer_wins}")
    result_label.config(text=f"Computer chose: {computer_choice}\n{status}")
    
    if user_wins == series_limit:
        messagebox.showinfo("Game Over", "🎉 Congratulations! You won the series! 🎉")
        root.quit()
    elif computer_wins == series_limit:
        messagebox.showinfo("Game Over", "😩 You lost the series! Better luck next time. 😩")
        root.quit()

def start_game():
    global user_wins, computer_wins, rounds, series_limit
    try:
        series = int(series_entry.get())
        if series < 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the series!🫠🫠")
        return
    
    series_limit = (series // 2) + 1
    user_wins, computer_wins, rounds = 0, 0, 0
    score_label.config(text="Score - You: 0 | Computer: 0")
    result_label.config(text="")

tk_root = tk.Tk()
tk_root.title("Rock-Paper-Scissors Game")
tk_root.geometry("650x550")


series_entr=tk.Label(tk_root, text="Welcome to 🪨 📄 ✂️ Game", font=("Comic Sans MS", 40)).pack(pady=15)
# series_entr.pack(pady=15)

tk.Label(tk_root, text="Enter match series : ", font=("Comic Sans MS", 30)).pack()
series_entry = tk.Entry(tk_root, font=("Comic Sans MS", 30))
series_entry.pack(pady=15)



tk.Button(tk_root, text="Start Game 👍", font=("Comic Sans MS", 30), command=start_game).pack()

result_label = tk.Label(tk_root, text="", font=("Comic Sans MS", 30))
result_label.pack()

score_label = tk.Label(tk_root, text="Score - You: 0 | Computer: 0", font=("Comic Sans MS", 40))
score_label.pack()

button_frame = tk.Frame(tk_root)
button_frame.pack()

tk.Button(button_frame, text="🪨", font=("Times New Roman", 50), command=lambda: play_round("rock")).grid(row=0, column=0, padx=15, pady=15)
tk.Button(button_frame, text="📄", font=("Times New Roman", 50), command=lambda: play_round("paper")).grid(row=0, column=1, padx=15, pady=15)
tk.Button(button_frame, text="✄", font=("Times New Roman", 50), command=lambda: play_round("scissors")).grid(row=0, column=2, padx=15, pady=15)

tk_root.mainloop()