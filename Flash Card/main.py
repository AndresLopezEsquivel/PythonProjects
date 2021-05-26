from data_maganer import DataManager
from tkinter import *

APP_TITLE = "Flash Card Japanese - English"
# LANGUAGES FILE
JAPANESE_TO_ENGLISH_FILE_PATH = "./data/japanese_to_english.csv"
# WINDOW PROPERTIES
BACKGROUND_COLOR = "#B1DDC6"
SCREEN_X_PADDING = 50
SCREEN_Y_PADDING = 50
# CANVAS CARD PROPERTIES
FRONT_CARD_IMAGE_PATH = "./images/card_front.png"
BACK_CARD_IMAGE_PATH = "./images/card_back.png"
CANVAS_CARD_WIDTH = 800
CANVAS_CARD_HEIGHT = 526
CARD_IMAGE_X_POSITION = CANVAS_CARD_WIDTH / 2
CARD_IMAGE_Y_POSITION = CANVAS_CARD_HEIGHT / 2
# LANGUAGE NAME TITLE PROPERTIES
LANGUAGE_NAME_X_POSITION = 400
LANGUAGE_NAME_Y_POSITION = 100
LANGUAGE_NAME_FONT = ("Arial", 40, "italic")
# WORD OF CURRENT LANGUAGE PROPERTIES
WORD_X_POSITION = 400
WORD_Y_POSITION = 263
WORD_FONT = ("Arial", 60, "bold")
# WORD PRONUNCIATION PROPERTIES
WORD_PRONUNCIATION_X_POSITION = 400
WORD_PRONUNCIATION_Y_POSITION = 205
WORD_PRONUNCIATION_FONT = ("Arial", 30, "italic")
# CORRECT ANSWER BUTTON PROPERTIES
CORRECT_ANSWER_BUTTON_IMAGE_PATH = "./images/right.png"
# INCORRECT ANSWER BUTTON PROPERTIES
INCORRECT_ANSWER_BUTTON_IMAGE_PATH = "./images/wrong.png"
# AFTER
timer = None
# DataManager INSTANCE
data_manager = DataManager(languages_data_file_path=JAPANESE_TO_ENGLISH_FILE_PATH)


def next_card():
    global timer
    global data_manager
    if data_manager.word_list_is_not_empty():
        if timer is not None:
            card.after_cancel(timer)
        word_data = data_manager.select_random_word()
        language_one = data_manager.language_one
        language_two = data_manager.language_two
        word_language_one = word_data[0]
        word_pronunciation_language_one = word_data[1]
        word_language_two = word_data[2]
        card.itemconfig(background_image_card, image=front_image)
        card.itemconfig(language_name, text=language_one, fill="black")
        card.itemconfig(word, text=word_language_one, fill="black")
        card.itemconfig(word_pronunciation, text=word_pronunciation_language_one)
        timer = card.after(3000, flip_card, language_two, word_language_two)
    else:
        list_of_words_is_empty()


def flip_card(language_two, word_language_two):
    card.itemconfig(background_image_card, image=back_image)
    card.itemconfig(language_name, text=language_two, fill="white")
    card.itemconfig(word, text=word_language_two, fill="white")
    card.itemconfig(word_pronunciation, text="")
    card.after_cancel(timer)


def is_known():
    if data_manager.word_list_is_not_empty():
        data_manager.remove_current_word_data()
        next_card()
    else:
        list_of_words_is_empty()


def list_of_words_is_empty():
    card.itemconfig(background_image_card, image=front_image)
    card.itemconfig(language_name, text="", fill="black")
    card.itemconfig(word, text="No more words to show", fill="black")
    card.itemconfig(word_pronunciation, text="")

# Setting up window properties
window = Tk()
window.title(APP_TITLE)
window.config(bg=BACKGROUND_COLOR, padx=SCREEN_Y_PADDING, pady=SCREEN_Y_PADDING)

# Setting up canvas card properties
card = Canvas(width=CANVAS_CARD_WIDTH, height=CANVAS_CARD_HEIGHT, bg= BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file=FRONT_CARD_IMAGE_PATH)
back_image = PhotoImage(file=BACK_CARD_IMAGE_PATH)
background_image_card = card.create_image(CARD_IMAGE_X_POSITION, CARD_IMAGE_Y_POSITION, image=front_image)
language_name = card.create_text(LANGUAGE_NAME_X_POSITION, LANGUAGE_NAME_Y_POSITION,
                                 text="日本語", font=LANGUAGE_NAME_FONT)
word = card.create_text(WORD_X_POSITION, WORD_Y_POSITION, text="大学", font=WORD_FONT)
word_pronunciation = card.create_text(WORD_PRONUNCIATION_X_POSITION, WORD_PRONUNCIATION_Y_POSITION,
                                      text="だいがく", font=WORD_PRONUNCIATION_FONT)
card.grid(row=0, column=0, columnspan=2)

# Setting up correct_answer button
correct_answer_button_image = PhotoImage(file=CORRECT_ANSWER_BUTTON_IMAGE_PATH)
correct_answer_button = Button(image=correct_answer_button_image, highlightthickness=0, command=is_known)
correct_answer_button.grid(row=1, column=0)

# Setting up incorrect_answer button
incorrect_answer_button_image = PhotoImage(file=INCORRECT_ANSWER_BUTTON_IMAGE_PATH)
incorrect_answer_button = Button(image=incorrect_answer_button_image, highlightthickness=0, command=next_card)
incorrect_answer_button.grid(row=1, column=1)

next_card()

window.mainloop()