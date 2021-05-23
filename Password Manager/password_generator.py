import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class PasswordGenerator:

    def __init__(self, number_of_letters, number_of_symbols, number_of_numbers):
        self.number_of_letters = number_of_letters
        self.number_of_numbers = number_of_numbers
        self.number_of_symbols = number_of_symbols
        self.password_list = []

    def generate_password(self):
        self.password_list = []
        password_list_part_1 = [random.choice(LETTERS) for _ in range(self.number_of_letters)]
        password_list_part_2 = [random.choice(NUMBERS) for _ in range(self.number_of_numbers)]
        password_list_part_3 = [random.choice(SYMBOLS) for _ in range(self.number_of_symbols)]
        self.password_list.extend(password_list_part_1)
        self.password_list.extend(password_list_part_2)
        self.password_list.extend(password_list_part_3)
        random.shuffle(self.password_list)
        final_password = "".join(self.password_list)
        return final_password
