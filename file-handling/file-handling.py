# Andrés López Esquivel
# 24/06/2021
# File handling

NUMBERS_FILE_PATH =  "./files/numbers.txt"
NAMES_FILE_PATH = "./files/names.txt"


def read():
    with open(NUMBERS_FILE_PATH, "r", encoding="utf-8") as numbers_file:
        numbers = [int(number) for number in numbers_file]
    print(numbers)


def write():
    names = ["Andrés", "Alejandro", "Paco", "Tanaka", "Yoshida"]
    with open(NAMES_FILE_PATH, "w", encoding="utf-8") as names_file:
        for name in names:
            names_file.write(f"{name}\n")


def run():
    # read()
    write()


if __name__ == "__main__":
    run()