from tkinter import *
from timer import Timer

YELLOW = "#f7f5dd"

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady= 50, bg=YELLOW)

# Pomodoro canvas timer
timer = Timer()

# Start button
start_button = Button(text="Start", highlightthickness=0, command=timer.start)
start_button.grid(column=0, row=2)

# Reset button
reset_button = Button(text="Reset", highlightthickness=0, command=timer.reset)
reset_button.grid(column=2, row=2)

window.mainloop()