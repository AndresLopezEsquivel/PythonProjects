import pandas
import random

FIRST_COLUMN_NAME = "japanese"
SECOND_COLUMN_NAME = "japanese_pronunciation"
THIRD_COLUMN_NAME = "english"


def dataframe_to_dict(data_file_path):
    dataFrame = pandas.read_csv(data_file_path)
    dataFrame_to_dict = {row[FIRST_COLUMN_NAME]: [row[SECOND_COLUMN_NAME], row[THIRD_COLUMN_NAME]]
                         for (index, row) in dataFrame.iterrows()}
    return dataFrame_to_dict


class DataManager:

    def __init__(self, languages_data_file_path):
        self.languages_data_file_path = languages_data_file_path
        self.words_dictionary = dataframe_to_dict(self.languages_data_file_path)
        self.words_dictionary_keys = [key for key in self.words_dictionary]
        self.word_language_one = ""
        self.pronunciation_word_language_one = ""
        self.word_language_two = ""

    def random_pair_of_words(self):
        self.word_language_one = random.choice(self.words_dictionary_keys)
        self.pronunciation_word_language_one = self.words_dictionary[self.word_language_one][0]
        self.word_language_two = self.words_dictionary[self.word_language_one][1]
        return self.word_language_one, self.pronunciation_word_language_one,self.word_language_two
