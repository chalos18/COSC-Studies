from tkinter import *

board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

window = Tk()

value = StringVar(window, " ")
label = Label(window, textvariable=value)
label.grid(row=0, column=0, sticky="w")

clear = Button(window, text="Clear", command=lambda: clear_data(value))
clear.grid(row=0, column=1, sticky="e", pady=5, padx=8)

# keyboard frame
frame = Frame(window, relief=RAISED, bd=2)
frame.grid(row=1, column=0, columnspan=2)


def append(the_value, x):
    the_value.set(the_value.get() + x)

def clear_data(data):
    data.set("")


for row, row_keys in enumerate(board):
    # keyboard row frame
    row_frame = Frame(frame)
    row_frame.grid(row=row+1, column=0, columnspan=2)
    for column, letter in enumerate(row_keys):
        button = Button(
            row_frame,
            width=1,
            height=1,
            text=f"{letter}",
            command=lambda x=letter: append(value, x),
        )
        button.grid(row=row, column=column)

window.mainloop()
