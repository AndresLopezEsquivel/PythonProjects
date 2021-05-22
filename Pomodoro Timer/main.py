from tkinter import *
from timer import Timer

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TOMATO_IMAGE_PATH = "./tomato.png"
FONT_CENTRAL_TEXT = (FONT_NAME, 35, "bold")
FONT_TIMER_TEXT = (FONT_NAME, 50, "bold")
FONT_CHECKMARK = (FONT_NAME, 20, "bold")

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