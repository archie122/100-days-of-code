from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# Dataframe
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")

FrenchToEnglish = data.to_dict(orient="records")
current_card = {}


# Functions

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(FrenchToEnglish)
    canvas.itemconfig(label1, text='French', fill="black")
    canvas.itemconfig(label2, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=card_front)

    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(label1, text='English', fill="white")
    canvas.itemconfig(label2, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_img, image=card_back)


def know_card():
    FrenchToEnglish.remove(current_card)
    new_data = pandas.DataFrame(FrenchToEnglish)
    new_data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# Window
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
label1 = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
label2 = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")

# Button 1
button_image_1 = PhotoImage(file="images/right.png")
button_1 = Button(image=button_image_1, highlightthickness=0, justify="center", command=know_card)
button_1.grid(row=1, column=1)

# Button 2
button_image_2 = PhotoImage(file="images/wrong.png")
button_2 = Button(image=button_image_2, highlightthickness=0, justify="center", command=next_card)
button_2.grid(row=1, column=0)

next_card()

window.mainloop()
