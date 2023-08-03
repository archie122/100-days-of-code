from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(12, 20))]
    number_list = [choice(numbers) for _ in range(randint(6, 8))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 9))]

    password_list = letter_list + number_list + symbol_list
    shuffle(password_list)

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        state = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

        if state:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.insert(0, "archie.c122133@gmail.com")
        else:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

# Website Label

website_label = Label(text="Website:", fg="white")
website_label.grid(row=1, column=0)

# Website Entry

website_entry = Entry(width=38, fg="white", highlightthickness=0)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# Email Label

email_label = Label(text="Email/Username:", fg="white")
email_label.grid(row=2, column=0)

# Email Entry

email_entry = Entry(width=38, fg="white", highlightthickness=0)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "archie.c122133@gmail.com")

# Password Label

password_label = Label(text="Password:", fg="white")
password_label.grid(row=3, column=0)

# Password Entry

password_entry = Entry(width=21, fg="white", highlightthickness=0)
password_entry.grid(row=3, column=1)

# Generate Password Button

password_button = Button(text="Generate Password", highlightthickness=0, fg="black", command=generate_password)
password_button.grid(row=3, column=2)

# Add Button

add_button = Button(text="Add", width=36, highlightthickness=0, fg="black", command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
