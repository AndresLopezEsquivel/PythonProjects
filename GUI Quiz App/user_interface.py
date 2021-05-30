from quiz_brain import QuizBrain
from tkinter import *
# WINDOW
WINDOW_TITLE = "Quiz App"
WINDOW_X_PADDING = 20
WINDOW_Y_PADDING = 20
WINDOW_BACKGROUND_COLOR = "#375362"
# SCOREBOARD
SCOREBOARD_BACKGROUND_COLOR = WINDOW_BACKGROUND_COLOR
SCOREBOARD_TEXT_COLOR = "white"
SCOREBOARD_TEXT_FONT = ("Arial", 20, "italic")
SCOREBOARD_Y_PADDING = 10
# QUESTION BOARD
QUESTION_BOARD_WIDTH = 300
QUESTION_BOARD_HEIGHT = 300
QUESTION_BOARD_BACKGROUND_COLOR = "white"
QUESTION_BOARD_TEXT_FONT = ("Arial", 20, "italic")
QUESTION_BOARD_TEXT_X_POSITION = QUESTION_BOARD_WIDTH / 2
QUESTION_BOARD_TEXT_Y_POSITION = QUESTION_BOARD_HEIGHT / 2
QUESTION_BOARD_TEXT_WIDTH = 280
# TRUE BUTTON
TRUE_BUTTON_IMAGE_PATH = "./images/true.png"
TRUE_BUTTON_X_PADDING = 20
TRUE_BUTTON_Y_PADDING = 20
# FALSE BUTTON
FALSE_BUTTON_IMAGE_PATH = "./images/false.png"


class UserInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        # Setting up window
        self.window = Tk()
        self.window.title(WINDOW_TITLE)
        self.window.config(padx=WINDOW_X_PADDING,
                           pady=WINDOW_Y_PADDING,
                           bg=WINDOW_BACKGROUND_COLOR)
        # Setting up scoreboard
        self.scoreboard = Label(text="Score: -/-",
                                bg=SCOREBOARD_BACKGROUND_COLOR,
                                fg=SCOREBOARD_TEXT_COLOR,
                                font = SCOREBOARD_TEXT_FONT,
                                highlightthickness=0)
        self.scoreboard.grid(row=0,
                             column=1,
                             pady=SCOREBOARD_Y_PADDING)
        # Setting up Question Canvas
        self.question_board = Canvas(width=QUESTION_BOARD_WIDTH,
                                     height=QUESTION_BOARD_HEIGHT,
                                     bg=QUESTION_BOARD_BACKGROUND_COLOR,
                                     highlightthickness=0)
        self.question_board_text = self.question_board.create_text(QUESTION_BOARD_TEXT_X_POSITION,
                                                                   QUESTION_BOARD_TEXT_Y_POSITION,
                                                                   width=QUESTION_BOARD_TEXT_WIDTH,
                                                                   text="Are you ready?",
                                                                   font=QUESTION_BOARD_TEXT_FONT)
        self.question_board.grid(row=1,
                                 column=0,
                                 columnspan=2)
        # Setting up True button
        true_button_image = PhotoImage(file=TRUE_BUTTON_IMAGE_PATH)
        self.true_button = Button(image=true_button_image,
                                  highlightthickness=0,
                                  command=self.true_button_pressed)
        self.true_button.grid(row=2,
                              column=0,
                              padx=TRUE_BUTTON_X_PADDING,
                              pady=TRUE_BUTTON_Y_PADDING)
        # Setting up False button
        false_button_image = PhotoImage(file=FALSE_BUTTON_IMAGE_PATH)
        self.false_button = Button(image=false_button_image,
                                   highlightthickness=0,
                                   command=self.false_button_pressed)
        self.false_button.grid(row=2,
                               column=1)
        # Showing first question
        self.set_new_question()
        # Mainloop
        self.window.mainloop()

    def set_new_question(self):
        self.question_board.config(bg="white")
        new_question = self.quiz_brain.next_question()
        self.update_question_text(new_text=new_question)

    def true_button_pressed(self):
        answer = "True"
        self.quiz_brain.check_answer(user_answer=answer)
        self.update_scoreboard()
        if self.quiz_brain.still_has_questions():
            self.set_new_question()
        else:
            self.quiz_brain.current_question_text = ""
            self.quiz_brain.current_question_answer = ""
            total_score = f"Total score: {self.quiz_brain.user_score_text}"
            self.update_question_text(new_text=total_score)

    def false_button_pressed(self):
        answer = "True"
        self.quiz_brain.check_answer(user_answer=answer)
        self.update_scoreboard()
        if self.quiz_brain.still_has_questions():
            self.set_new_question()
        else:
            self.quiz_brain.current_question_text = ""
            self.quiz_brain.current_question_answer = ""
            total_score = f"Total score: {self.quiz_brain.user_score_text}"
            self.update_question_text(new_text=total_score)

    def update_scoreboard(self):
        self.scoreboard.config(text=self.quiz_brain.user_score_text)

    def update_question_text(self, new_text: str):
        self.question_board.itemconfig(self.question_board_text,
                                       text=new_text)