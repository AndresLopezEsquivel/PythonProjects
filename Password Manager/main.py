from tkinter import *
from tkinter import messagebox
from password_data_manager import PasswordDataManager
from password_generator import PasswordGenerator
import pyperclip

WINDOW_TITLE = "Password Manager"
PADLOCK_IMAGE_PATH = "logo.png"
PASSWORDS_DATA_FILE_PATH = "passwords_data.json"


def search_password():
    website_name = website_entry.get()
    website_name_is_empty = len(website_name) == 0

    if website_name_is_empty:
        title = "Website name field empty"
        message = "Please enter the name of the website whose password you are looking for."
        messagebox.showerror(title=title, message=message)
    else:
        password_manager = PasswordDataManager(passwords_data_file_path=PASSWORDS_DATA_FILE_PATH)

        if password_manager.website_password_exists(website_searched=website_name):
            website_password_data = password_manager.get_website_password(website_searched=website_name)
            username = website_password_data["username"]
            password = website_password_data["password"]
            title = website_name
            message = f"Username: {username} \n Password: {password}"
            messagebox.showinfo(title=title, message=message)
        else:
            title = "Website Password data not fount"
            message = f"There are no details for {website_name}."
            messagebox.showerror(title=title, message=message)


def generate_password():
    password_entry.delete(0, END)
    password = password_generator.generate_password()
    password_entry.insert(0, password)
    pyperclip.copy(password)


def add_password():
    website_name = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    website_name_is_empty = len(website_name) == 0
    username_is_empty = len(username) == 0
    password_is_empty = len(password) == 0

    if website_name_is_empty or username_is_empty or password_is_empty:
        title = "Empty Fields founded"
        message = "There are empty fields. Please, write all the required data."
        messagebox.showerror(title=title, message=message)
    else:
        title = "Confirm data"
        message = f"Please confirm data. \n Website: {website_name} \n Username: {username} \n Password: {password}"
        is_data_confirmed = messagebox.askokcancel(title=title, message=message)

        if is_data_confirmed:
            new_password_data = {website_name: {"username": username, "password": password}}
            password_manager = PasswordDataManager(passwords_data_file_path=PASSWORDS_DATA_FILE_PATH)
            password_manager.add_new_password(new_password_data=new_password_data)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


window = Tk()
window.title(WINDOW_TITLE)
window.config(padx=50, pady=50)

password_generator = PasswordGenerator(number_of_letters=4, number_of_numbers=4, number_of_symbols=2)

canvas = Canvas(width=200, height=200)
padlock_photo_image = PhotoImage(file=PADLOCK_IMAGE_PATH)
canvas.create_image(100, 100, image=padlock_photo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username: ")
username_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

username_entry = Entry(width=35)
username_entry.insert(0, "proof@proof.com")
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

search_password_button = Button(text="Search password", command=search_password)
search_password_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_password_button = Button(text="Add password", width=35, command=add_password)
add_password_button.grid(row=4, column=1, columnspan=2)

window.mainloop()