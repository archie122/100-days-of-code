from tkinter import *

root = Tk()
root.title("Miles to Km Converter")
root.minsize(width=100, height=100)
root.config(padx=50, pady=50)


# Button Clicked Function

def button_clicked():
    result.config(text=round(int(input.get()) * 1.609, 2))


# Textbox

input = Entry(width=10, justify="center")
input.grid(row=0, column=0)

# Label 1

miles = Label(text="Miles")
miles.grid(row=0, column=1)

# Label 2

km = Label(text="Km")
km.grid(row=1, column=1)

# Label 3

result = Label(text="0")
result.grid(row=1, column=0)

# Button

button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=0)

root.mainloop()
