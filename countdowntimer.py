import time
import tkinter as tk
from tkinter import ttk
from threading import Thread
from playsound import playsound
class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("400x300")
        self.root.configure(bg="#1e1e2e")

        self.running = False
        self.time_left = 0

        # Style Configuration
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12), padding=5)
        style.configure("TLabel", font=("Arial", 12), background="#1e1e2e", foreground="white")
        style.configure("TFrame", background="#1e1e2e")

        # Timer selection frame
        frame = ttk.Frame(root)
        frame.pack(pady=10)

        # Hours, Minutes, Seconds Dropdown
        ttk.Label(frame, text="Hours:").grid(row=0, column=0)
        self.hours = tk.StringVar(value="0")
        self.hours_menu = ttk.Combobox(frame, textvariable=self.hours, values=list(range(24)), width=5)
        self.hours_menu.grid(row=0, column=1)

        ttk.Label(frame, text="Minutes:").grid(row=0, column=2)
        self.minutes = tk.StringVar(value="0")
        self.minutes_menu = ttk.Combobox(frame, textvariable=self.minutes, values=list(range(60)), width=5)
        self.minutes_menu.grid(row=0, column=3)

        ttk.Label(frame, text="Seconds:").grid(row=0, column=4)
        self.seconds = tk.StringVar(value="0")
        self.seconds_menu = ttk.Combobox(frame, textvariable=self.seconds, values=list(range(60)), width=5)
        self.seconds_menu.grid(row=0, column=5)

        # Timer Display
        self.timer_label = ttk.Label(root, text="00:00:00", font=("Helvetica", 40), foreground="#ffcc00")
        self.timer_label.pack(pady=10)

        # Progress Bar
        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)

        # Buttons
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)

        self.start_btn = ttk.Button(button_frame, text="Start", command=self.start_timer)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.stop_btn = ttk.Button(button_frame, text="Stop", command=self.stop_timer)
        self.stop_btn.grid(row=0, column=1, padx=5)

        self.reset_btn = ttk.Button(button_frame, text="Reset", command=self.reset_timer)
        self.reset_btn.grid(row=0, column=2, padx=5)

    def countdown(self):
        self.running = True
        self.time_left = int(self.hours.get()) * 3600 + int(self.minutes.get()) * 60 + int(self.seconds.get())
        total_time = self.time_left
        start_time = time.time()  # Use time.time() for real-time tracking

        while self.time_left > 0 and self.running:
            current_time = time.time()
            elapsed_time = int(current_time - start_time)  # Calculate elapsed time accurately
            remaining_time = max(0, total_time - elapsed_time)

            hrs, rem = divmod(remaining_time, 3600)
            mins, secs = divmod(rem, 60)

            self.timer_label.config(text=f"{hrs:02}:{mins:02}:{secs:02}")
            self.progress["value"] = ((total_time - remaining_time) / total_time) * 100

            self.beep_sound()

            time.sleep(1 - ((time.time() - current_time) % 1))  # Adjust sleep time to maintain accuracy

        if self.running:
            self.timer_label.config(text="Time's Up!")
            self.progress["value"] = 100

    def beep_sound(self):
        playsound("/System/Library/Sounds/Ping.aiff")  # Default macOS sound
 # Beep sound

    def start_timer(self):
        if not self.running:
            Thread(target=self.countdown, daemon=True).start()

    def stop_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.timer_label.config(text="00:00:00")
        self.progress["value"] = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()
