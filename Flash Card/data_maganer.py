import pandas
import random

WORDS_TO_STUDY_FILE_NAME = "./data/word_to_study.csv"
FIRST_COLUMN_NAME = "japanese"
SECOND_COLUMN_NAME = "japanese_pronunciation"
THIRD_COLUMN_NAME = "english"

# def dataframe_to_dict(data_file_path):
#     dataFrame = pandas.read_csv(data_file_path)
#     dataFrame_to_dict = {row[FIRST_COLUMN_NAME]: [row[SECOND_COLUMN_NAME], row[THIRD_COLUMN_NAME]]
#                          for (index, row) in dataFrame.iterrows()}
#     return dataFrame_to_dict


def dataframe_to_list(data_file_path):
    try:
        dataFrame = pandas.read_csv(WORDS_TO_STUDY_FILE_NAME)
        print("words_to_study.csv file successfully read.")
    except FileNotFoundError:
        dataFrame = pandas.read_csv(data_file_path)
        print(f"words_to_study.csv does not exist. Instead, {data_file_path} is being used.")
    finally:
        dataFrame_to_list = dataFrame.to_dict(orient="records")
    return dataFrame_to_list


class DataManager:

    # def __init__(self, languages_data_file_path):
    #     self.languages_data_file_path = languages_data_file_path
    #     self.words_dictionary = dataframe_to_dict(self.languages_data_file_path)
    #     self.words_dictionary_keys = [key for key in self.words_dictionary]
    #     self.word_language_one = ""
    #     self.pronunciation_word_language_one = ""
    #     self.word_language_two = ""

    def __init__(self, languages_data_file_path):
        self.languages_data_file_path = languages_data_file_path
        self.words_list = dataframe_to_list(self.languages_data_file_path)
        self.current_word_data = {}
        self.language_one = FIRST_COLUMN_NAME.title()
        self.language_two = THIRD_COLUMN_NAME.title()
        self.word_language_one = ""
        self.word_pronunciation_language_one = ""
        self.word_language_two = ""

    # def random_pair_of_words(self):
    #     self.word_language_one = random.choice(self.words_dictionary_keys)
    #     self.pronunciation_word_language_one = self.words_dictionary[self.word_language_one][0]
    #     self.word_language_two = self.words_dictionary[self.word_language_one][1]
    #     return self.word_language_one, self.pronunciation_word_language_one,self.word_language_two

    def select_random_word(self):
        word_data = random.choice(self.words_list)
        self.current_word_data = word_data
        self.word_language_one = word_data[FIRST_COLUMN_NAME]
        self.word_pronunciation_language_one = word_data[SECOND_COLUMN_NAME]
        self.word_language_two = word_data[THIRD_COLUMN_NAME]
        return self.word_language_one, self.word_pronunciation_language_one, self.word_language_two

    def word_list_is_not_empty(self):
        return len(self.words_list) > 0

    def remove_current_word_data(self):
        if self.word_list_is_not_empty():
            print(f"Before removing: {self.words_list}")
            self.words_list.remove(self.current_word_data)
        print(f"After removing: {self.words_list}")

    def save_data(self):
        language_one_words = [data[FIRST_COLUMN_NAME] for data in self.current_word_data]
        words_pronunciation_language_one = [data[SECOND_COLUMN_NAME] for data in self.current_word_data]
        language_two_words = [data[THIRD_COLUMN_NAME] for data in self.current_word_data]
        words_data_dictionary = {
            FIRST_COLUMN_NAME: language_one_words,
            SECOND_COLUMN_NAME: words_pronunciation_language_one,
            THIRD_COLUMN_NAME: language_two_words
        }
