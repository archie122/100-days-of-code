import tkinter as tk

# Create a window and size it
window = tk.Tk()
window.title("Hello World")
window.minsize(width=500, height=300)

# Label
#     mylabel = tk.Label(text="This is a label", font=("Arial", 24, "bold"))
#     mylabel.pack(expand=True)  # This is the line that actually puts the label on the screen


# mylabel["text"] = "This is a new label"
# mylabel.config(text="This is a new label")

# Button
#     def button_clicked():
#         # mylabel.config(text="You clicked me!")
#         mylabel.config(text=input.get())
#
#
#     button = tk.Button(text="Click Me", command=button_clicked)
#     button.pack(expand=True)

# Entry
#     input = tk.Entry(width=10)
#     input.pack(expand=True)
#     input.insert(0, string="Type here")

# Textbox
#     def button_clicked():
#         print(text.get("1.0", "end-1c"))
#
#     text = tk.Text(height=5, width=30)
#     text.focus()
#     text.insert(0.0, "Type something here")
#     text.pack(expand=True)
#
#     button = tk.Button(text="Click Me", command=button_clicked)
#     button.pack(expand=True)

# Spinbox
#     def spinbox_used():
#         print(spinbox.get())
#
#
#     spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
#     spinbox.pack(expand=True)

# Scale
#     def scale_used(value):
#         print(value)
#
#     scale = tk.Scale(from_=0, to=100, command=scale_used)
#     scale.pack(expand=True)

# Checkbutton
#         def checkbutton_used():
#             print(checked.get())
#
#         checked = tk.IntVar()
#         check_button = tk.Checkbutton(text="Is it true?", variable=checked, command=checkbutton_used)
#         check_button.pack(expand=True)

# Radiobutton
#     def radio_used():
#         print(radio_state.get())
#
#     radio_state = tk.StringVar()
#     radioButton1 = tk.Radiobutton(text="Option 1", variable=radio_state, value="A", command=radio_used)
#     radioButton1.pack(expand=True)
#     radioButton2 = tk.Radiobutton(text="Option 2", variable=radio_state, value="B", command=radio_used)
#     radioButton2.pack(expand=True)
#     radioButton3 = tk.Radiobutton(text="Option 3", variable=radio_state, value="C", command=radio_used)
#     radioButton3.pack(expand=True)

# Listbox
#     def listbox_used(event):
#         print(listbox.get(listbox.curselection()))
#
#     listbox = tk.Listbox(height=4)
#     fruits = [
#         "Apple",
#         "Pear",
#         "Orange",
#         "Banana",
#     ]
#
#     for fruit in fruits:
#         listbox.insert(fruits.index(fruit), fruit)
#
#     listbox.pack(expand=True)
#     listbox.bind("<<ListboxSelect>>", listbox_used)




























window.mainloop()