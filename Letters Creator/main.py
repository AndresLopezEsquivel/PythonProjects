INVITED_NAMES_PATH = "./Input/Names/invited_names.txt"
STARTING_LETTER_PATH = "./Input/Letters/starting_letter.txt"
FINISHED_LETTER_PATH = "./Output/ReadyToSend/"

with open(INVITED_NAMES_PATH) as invited_names_file:
    list_of_names = invited_names_file.readlines()

with open(STARTING_LETTER_PATH) as starting_letter_file:
    starting_letter_file = starting_letter_file.read()

for name in list_of_names:
    current_letter = starting_letter_file.replace("[name]", name.strip())
    new_file_name = f"dear_{name.strip()}.txt"
    new_file_path = f"{FINISHED_LETTER_PATH}{new_file_name}"
    with open(new_file_path, "w") as letter_ready_to_send:
        letter_ready_to_send.write(current_letter)


