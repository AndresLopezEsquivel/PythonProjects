PATH_FILE = "./ProgramFile.txt"


class TextFileManager:

    def write_text_file(self, text):
        with open(PATH_FILE, 'w', encoding="utf-8") as file:
            file.write(text)
