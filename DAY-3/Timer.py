import tkinter as tk
from tkinter import messagebox
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")

        self.is_running = False
        self.is_paused = False
        self.start_time = 0.0
        self.elapsed_time = 0.0
        self.duration = 0

        self.label = tk.Label(root, text="0:00:00.0", font=("Helvetica", 36))
        self.label.pack(padx=20, pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_timer, state=tk.DISABLED)
        self.resume_button = tk.Button(root, text="Resume", command=self.resume_timer, state=tk.DISABLED)
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer, state=tk.DISABLED)

        self.start_button.pack()
        self.pause_button.pack()
        self.resume_button.pack()
        self.reset_button.pack()

        self.time_unit_label = tk.Label(root, text="Enter time unit (hours, mins, or secs):")
        self.time_unit_label.pack(pady=5)

        self.time_unit_entry = tk.Entry(root, width=10)
        self.time_unit_entry.insert(0, "secs")  # Default time unit is seconds
        self.time_unit_entry.pack(pady=5)

        self.duration_entry = tk.Entry(root, width=10)
        self.duration_entry.insert(0, "5")  # Default duration is 5 seconds
        self.duration_entry.pack(pady=10)

        self.update()

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.is_paused = False
            self.duration = self.parse_duration(self.duration_entry.get(), self.time_unit_entry.get())
            self.start_time = time.time()
            self.update_buttons_state()

    def pause_timer(self):
        if self.is_running and not self.is_paused:
            self.is_paused = True
            self.elapsed_time = self.duration - (time.time() - self.start_time)
            self.update_buttons_state()

    def resume_timer(self):
        if self.is_running and self.is_paused:
            self.is_paused = False
            self.start_time = time.time() - (self.duration - self.elapsed_time)
            self.update_buttons_state()

    def reset_timer(self):
        self.is_running = False
        self.is_paused = False
        self.elapsed_time = 0.0
        self.start_time = 0.0
        self.update_buttons_state()
        self.display_time()

    def update_buttons_state(self):
        if self.is_running:
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.resume_button.config(state=tk.NORMAL if self.is_paused else tk.DISABLED)
            self.reset_button.config(state=tk.NORMAL)
            self.duration_entry.config(state=tk.DISABLED)
            self.time_unit_entry.config(state=tk.DISABLED)
        else:
            self.start_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
            self.resume_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.DISABLED)
            self.duration_entry.config(state=tk.NORMAL)
            self.time_unit_entry.config(state=tk.NORMAL)

    def update(self):
        if self.is_running and not self.is_paused:
            self.elapsed_time = self.duration - (time.time() - self.start_time)
            self.display_time()
            if self.elapsed_time <= 0:
                self.show_time_message()
                self.reset_timer()
        self.root.after(100, self.update)

    def display_time(self):
        if self.elapsed_time < 0:
            self.elapsed_time = 0
        hours = int(self.elapsed_time // 3600)
        remaining_time = self.elapsed_time % 3600
        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)
        tenths = int((self.elapsed_time * 10) % 10)
        self.label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}.{tenths}")

    def parse_duration(self, input_str, time_unit):
        input_str = input_str.strip().lower()
        if time_unit == "hours":
            return int(input_str) * 3600  # Convert hours to seconds
        elif time_unit == "mins":
            return int(input_str) * 60  # Convert minutes to seconds
        elif time_unit == "secs":
            return int(input_str)  # Duration is in seconds
        else:
            return int(input_str)  # Default to seconds if no valid time unit specified

    def show_time_message(self):
        self.label.config(text="0:00:00.0")
        messagebox.showinfo("Timer Finished", "Time's UP!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
