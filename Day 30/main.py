from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, messagebox, END
from random import randint, shuffle, choice
import pyperclip
import json

FILE_NAME = "data.json"

# ---------------------------- SEARCH INFO ------------------------------- #


def search_info():
    website_value = website_input.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!!")
    else:
        if website_value in data:
            email_value = data[website_value]["email"]
            password_value = data[website_value]["password"]
            messagebox.showinfo(title=website_value, message=f"Email: {email_value}\nPassword: {password_value}")
        else:
            messagebox.showinfo(title="Oops", message=f"No data found for {website_value}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*',
               '(', ')', '-', '+', '=', '[', ']', '{', '}', '|', ';', ':', ',', '.', '/', '?', '<', '>', '`', '~', '_',
               '"', "'", '\\']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password_string = "".join(password_list)
    password_input.insert(0, password_string)
    pyperclip.copy(password_string)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_info():
    website_value = website_input.get()
    email_value = email_input.get()
    password_value = password_input.get()

    if len(website_value) <= 0 or len(email_value) <= 0 or len(password_value) <= 0:
        messagebox.showinfo(title="Oops", message="Please make sure that you have not left any fields empty!!")
    else:
        new_data = {
            website_value : {
                "email": email_value,
                "password": password_value
            }
        }

        is_ok = messagebox.askokcancel(title=website_value, message=f"These are the value entered: \nEmail: {email_value} "
                                       f"\nPassword: {password_value} \n Is it ok to save?")

        if is_ok:
            try:
                with open(FILE_NAME, "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open(FILE_NAME, "w") as file:
                    json.dump(new_data, file, indent=4, sort_keys=True)
            else:
                data.update(new_data)

                with open(FILE_NAME, "w") as file:
                    json.dump(data, file, indent=4, sort_keys=True)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# create the canvas to place the image
canvas = Canvas(width=200, height=200)
password_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_logo)
canvas.grid(column=1, row=0)

# place the labels on the screen
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# place the input field on the screen
website_input = Entry(width=21)
website_input.focus()
website_input.grid(column=1, row=1, sticky="EW")

email_input = Entry(width=35)
email_input.insert(0, "devadigaajay1729@gmail.com")
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="EW")

# place the button on the screen
generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, command=save_info)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

search_btn = Button(text="Search", command=search_info)
search_btn.grid(column=2, row=1, sticky="EW")

window.mainloop()
