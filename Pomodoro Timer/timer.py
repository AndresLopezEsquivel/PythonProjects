from tkinter import Canvas, PhotoImage
import math

YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
PINK = "#e2979c"
RED = "#e7305b"
TOMATO_IMAGE_PATH = "./tomato.png"
CHECKMARK = "✔"
FONT_NAME = "Courier"
FONT_TIMER_TITLE = (FONT_NAME, 30, "bold")
FONT_TIMER_COUNTER = (FONT_NAME, 50, "bold")
FONT_CHECKMARK = (FONT_NAME, 30, "bold")
TIMER_TITLES = ["Timer", "Working", "Short Break", "Long Break"]
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


class Timer(Canvas):

    def __init__(self):
        super().__init__()
        self.tomato_image = PhotoImage(file=TOMATO_IMAGE_PATH)
        self.timer = None
        self.repetitions = 0
        self.total_checkmarks = ""
        self.config(width=200, height=300, bg=YELLOW, highlightthickness=0)
        self.create_image(100, 150, image=self.tomato_image)
        self.timer_title = self.create_text(100, 20, text=TIMER_TITLES[0], fill=GREEN, font=FONT_TIMER_TITLE)
        self.timer_counter_text = self.create_text(100, 170, text="00:00", fill="white", font=FONT_TIMER_COUNTER)
        self.checkmark = self.create_text(100, 280, text="", fill=GREEN, font=FONT_CHECKMARK)
        self.grid(column=1, row=1)

    def count_down(self, seconds_remaining):
        if seconds_remaining >= 0:
            minutes_amount = math.floor(seconds_remaining / 60)
            seconds_amount = seconds_remaining % 60

            if seconds_amount < 10:
                time_remaining = f"{minutes_amount}:0{seconds_amount}"
            else:
                time_remaining = f"{minutes_amount}:{seconds_amount}"

            self.itemconfig(self.timer_counter_text, text=time_remaining)
            self.timer = self.after(1000, self.count_down, seconds_remaining - 1)
        else:
            self.repetitions += 1
            if self.repetitions % 2 == 0:
                self.total_checkmarks = ""
                for _ in range(int(self.repetitions / 2)):
                    self.total_checkmarks += CHECKMARK
            self.itemconfig(self.checkmark, text=self.total_checkmarks)
            self.start()

    def count_work_time(self):
        self.count_down(WORK_MIN * 60)

    def count_short_break_time(self):
        self.count_down(SHORT_BREAK_MIN * 60)

    def count_long_break_time(self):
        self.count_down(LONG_BREAK_MIN * 60)

    def start(self):
        # self.timer = None
        if self.repetitions < 8:
            if self.repetitions % 2 == 0:
                self.itemconfig(self.timer_title, text=TIMER_TITLES[1], fill=GREEN)
                self.count_work_time()
            elif self.repetitions == 7:
                self.itemconfig(self.timer_title, text=TIMER_TITLES[3], fill=RED)
                self.count_long_break_time()
            else:
                self.itemconfig(self.timer_title, text=TIMER_TITLES[2], fill=PINK)
                self.count_short_break_time()
        else:
            self.reset()

    def reset(self):
        self.after_cancel(self.timer)
        # Why this line of code is the solution?
        self.timer = None
        self.total_checkmarks = ""
        self.repetitions = 0
        self.itemconfig(self.timer_title, text=TIMER_TITLES[0], fill=GREEN)
        self.itemconfig(self.timer_counter_text, text="00:00")
        self.itemconfig(self.checkmark, text="")
