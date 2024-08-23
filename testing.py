import tkinter as tk
from tkinter import messagebox
import time
import winsound

class ReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Break Reminder")
        self.root.iconify()  # hide the window
        self.root.configure(background="#f0f0f0")  # set background color

        # Create a frame to hold the label and button
        self.frame = tk.Frame(self.root, bg="#f0f0f0")
        self.frame.pack(padx=20, pady=20)

        # Create a label with a nice font and color
        self.label = tk.Label(self.frame, text="Break Reminder", font=("Segoe UI", 24, "bold"), fg="#333")
        self.label.pack(pady=10)

        # Create a button to restart the countdown
        self.button = tk.Button(self.frame, text="Restart", font=("Segoe UI", 12), fg="#fff", bg="#4CAF50", command=self.restart)
        self.button.pack(pady=10)

        self.countdown(20 * 60)  # start the countdown for 20 minutes

    def countdown(self, count):
        if count > 0:
            self.root.after(1000, self.countdown, count - 1)  # call this function every 1 second
        else:
            self.remind()

    def remind(self):
        winsound.Beep(2500, 1000)  # play a beep sound
        messagebox.showinfo("Break Time!", "Take a 20-second break!")
        self.countdown(20 * 60)  # restart the countdown

    def restart(self):
        self.countdown(20 * 60)  # restart the countdown

if __name__ == "__main__":
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()