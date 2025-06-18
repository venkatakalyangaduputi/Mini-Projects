import tkinter as tk
from tkinter import filedialog, messagebox
import pyautogui
import cv2
import numpy as np
import threading
import time

class ScreenRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Recorder")
        self.root.geometry("400x300")
        self.root.configure(bg="#1e1e1e")

        self.recording = False
        self.fps = 1
        self.output_filename = ""

        # Title Label
        self.title_label = tk.Label(root, text="Screen Recorder", font=("Arial", 16, "bold"), fg="black", bg="#1e1e1e")
        self.title_label.pack(pady=10)

        # Start Button
        self.start_button = tk.Button(root, text="Start Recording", command=self.toggle_recording, width=20, bg="#4CAF50", fg="black", font=("Arial", 12, "bold"))
        self.start_button.pack(pady=10)

        # Select File Button
        self.file_button = tk.Button(root, text="Change Save Location", command=self.select_output_file, width=20, bg="#2196F3", fg="black", font=("Arial", 12, "bold"))
        self.file_button.pack(pady=10)

        # Status Label
        self.status_label = tk.Label(root, text="Status: Idle", font=("Arial", 12), fg="black", bg="#1e1e1e")
        self.status_label.pack(pady=10)

        # Quit Button
        self.quit_button = tk.Button(root, text="Quit", command=self.quit, width=20, bg="#f44336", fg="black", font=("Arial", 12, "bold"))
        self.quit_button.pack(pady=10)

    def toggle_recording(self):
        if not self.output_filename:
            messagebox.showwarning("Screen Recorder", "Please select a save location before recording.")
            return
        
        if not self.recording:
            self.recording = True
            self.start_button.config(text="Stop Recording", bg="#f44336")
            self.status_label.config(text="Status: Recording...", fg="red")
            threading.Thread(target=self.record_screen, daemon=True).start()
        else:
            self.recording = False
            self.start_button.config(text="Start Recording", bg="#4CAF50")
            self.status_label.config(text="Status: Idle", fg="white")

    def select_output_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".mp4",
                                                 filetypes=[("MP4 files", "*.mp4")],
                                                 title="Select Save Location")
        if file_path:
            self.output_filename = file_path
            messagebox.showinfo("Screen Recorder", f"File will be saved as:\n{self.output_filename}")

    def record_screen(self):
        screen_width, screen_height = pyautogui.size()
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # More compatible codec
        out = cv2.VideoWriter(self.output_filename, fourcc, self.fps, (screen_width, screen_height))
        start_time = time.time()

        while self.recording:
            screen = pyautogui.screenshot()
            frame = np.array(screen)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            frame = cv2.resize(frame, (screen_width, screen_height))
            out.write(frame)
            elapsed_time = time.time() - start_time
            expected_time = (out.get(cv2.CAP_PROP_FRAME_COUNT) + 1) / self.fps
            sleep_time = max(0, expected_time - elapsed_time)
            time.sleep(sleep_time)

        out.release()
        messagebox.showinfo("Screen Recorder", f"Recording saved as {self.output_filename}")

    def quit(self):
        self.recording = False
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenRecorder(root)
    root.mainloop()
