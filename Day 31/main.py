from tkinter import Tk, Canvas, PhotoImage, Button
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

# read data from csv
french_words = pandas.read_csv("data/french_words.csv")
french_words = french_words.to_dict(orient="records")
current_word = {}


def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(french_words)
    french_word = current_word["French"]
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_text, text=french_word, fill="black")
    canvas.itemconfig(canvas_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    english_word = current_word["English"]
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_text, text=english_word, fill="white")
    canvas.itemconfig(canvas_background, image=card_back_image)


# creating the window
window = Tk()
window.title("Flashy Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_background = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_title = canvas.create_text(400, 150, text="Title", font=('Ariel', 40, 'italic'))
canvas_text = canvas.create_text(400, 263, text="Word", font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()

