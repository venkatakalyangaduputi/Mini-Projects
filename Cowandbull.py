import random
import tkinter as tk
from tkinter import messagebox

def generate_secret_number():
    return str(random.randint(1000, 9999))

def get_cows_and_bulls(secret, guess):
    cows = sum(1 for s, g in zip(secret, guess) if s == g)
    bulls = sum(1 for g in guess if g in secret) - cows
    return cows, bulls

def check_guess():
    guess = entry.get()
    if not guess.isdigit() or len(guess) != 4:
        messagebox.showerror("Invalid Input", "Please enter a valid 4-digit number.")
        return
    
    global attempts
    attempts += 1
    cows, bulls = get_cows_and_bulls(secret_number, guess)
    result_label.config(text=f"Cows: {cows}, Bulls: {bulls}")
    attempts_label.config(text=f"Attempts: {attempts}")
    
    if cows == 4:
        messagebox.showinfo("Congratulations!", f"You guessed the number {secret_number} in {attempts} attempts.")
        reset_game()

def reset_game():
    global secret_number, attempts
    secret_number = generate_secret_number()
    attempts = 0
    result_label.config(text="")
    attempts_label.config(text="Attempts: 0")
    entry.delete(0, tk.END)

def play_game():
    global root, entry, result_label, attempts_label, secret_number, attempts
    
    root = tk.Tk()
    root.title("Cows and Bulls Game")
    root.geometry("400x300")
    root.configure(bg="#000000")
    
    tk.Label(root, text="Cows and Bulls Game", font=("Comic Sans MS", 16, "bold"), bg="#000000", fg="cyan").pack(pady=5)
    tk.Label(root, text="Enter a 4-digit number:", font=("Comic Sans MS", 12), bg="#000000", fg="white").pack(pady=5)
    
    entry = tk.Entry(root, font=("Comic Sans MS", 14), justify="center", bg="#333333", fg="white")
    entry.pack(pady=5)
    
    tk.Button(root, text="Check", font=("Comic Sans MS", 12, "bold"), command=check_guess, bg="#000000", fg="black").pack(pady=5)
    
    result_label = tk.Label(root, text="", font=("Comic Sans MS", 12, "bold"), bg="#000000", fg="yellow")
    result_label.pack(pady=5)
    
    attempts_label = tk.Label(root, text="Attempts: 0", font=("Comic Sans MS", 12, "bold"), bg="#000000", fg="orange")
    attempts_label.pack(pady=5)
    
    tk.Button(root, text="Restart", font=("Comic Sans MS", 12, "bold"), command=reset_game, bg="#000000", fg="black").pack(pady=5)
    
    secret_number = generate_secret_number()
    attempts = 0
    
    root.mainloop()

if __name__ == "__main__":
    play_game()
