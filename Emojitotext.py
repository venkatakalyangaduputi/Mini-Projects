import tkinter as tk
import emoji
from tkinter import ttk

def convert_emoji():
    user_input = emoji_input.get()
    result = emoji.demojize(user_input)
    output_label.config(text=f"{result}")

root = tk.Tk()
root.title("Emoji to Text Converter")
root.geometry("500x350")
root.configure(bg="#121212")

style = ttk.Style()
style.configure("TButton", font=("Comic Sans MS", 12), padding=10, background="#4CAF50", foreground="white")
style.configure("TLabel", font=("Comic Sans MS", 14), background="#121212", foreground="white")
style.configure("TEntry", font=("Comic Sans MS", 14), padding=8)

heading = ttk.Label(root, text="🚀 Emoji to Text Converter", font=("Comic Sans MS", 20, "bold"))
heading.pack(pady=10)

def on_entry_click(event):
    if emoji_input.get() == "Enter emojis here...":
        emoji_input.delete(0, "end")
        emoji_input.config(foreground="black")

def on_focus_out(event):
    if not emoji_input.get():
        emoji_input.insert(0, "Enter emojis here...")
        emoji_input.config(foreground="gray")

emoji_input = ttk.Entry(root, font=("Comic Sans MS", 14), width=30, foreground="gray")
emoji_input.insert(0, "Enter emojis here...")
emoji_input.bind("<FocusIn>", on_entry_click)
emoji_input.bind("<FocusOut>", on_focus_out)
emoji_input.pack(pady=10, ipady=5)

def on_hover(event):
    convert_button.config(style="Hover.TButton")

def off_hover(event):
    convert_button.config(style="TButton")

style.configure("Hover.TButton", font=("Comic Sans MS", 12), padding=10, background="#FFD700")
convert_button = ttk.Button(root, text="Convert", command=convert_emoji, style="TButton")
convert_button.pack(pady=15)
convert_button.bind("<Enter>", on_hover)
convert_button.bind("<Leave>", off_hover)

output_frame = tk.Frame(root, bg="#1E1E1E", bd=2, relief="solid")
output_frame.pack(pady=10, fill="x", padx=20)
output_label = ttk.Label(output_frame, text="", font=("Comic Sans MS", 14), wraplength=450, anchor="center")
output_label.pack(pady=10)

footer = ttk.Label(root, text="Made By Venkata Kalyan", font=("Comic Sans MS", 10), foreground="#BBBBBB")
footer.pack(side="bottom", pady=5)

# Run the application
root.mainloop()
