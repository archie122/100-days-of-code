from tkinter import *

def button_click():
    print("You clicked me!")
    new_label = entry.get()
    label.config(text=new_label)


root = Tk()
root.geometry("500x300")
root.title("Layout")
root.config(padx=20, pady=20)

# Label
label = Label(text="Hello", font=("Arial", 20, 'bold'))
# label.pack()
# label.place(x=120, y=0) (Pretty okay to use but not recommended)
label.grid(row=0, column=0)

# Button
button = Button(text="Click Me", command=button_click)
# button.pack()
button.grid(row=1, column=1)

# Challenge

new_button = Button(text="Click Me")
new_button.grid(row=0, column=2)

# Entry
entry = Entry()
print(entry.get())
# entry.pack()
entry.grid(row=2, column=3)





root.mainloop()