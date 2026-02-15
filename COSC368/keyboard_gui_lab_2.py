import random
from tkinter import *
import time
import csv


CONDITIONS = ["static", "dynamic"]
name = input("What is your name? ")
while True:
    condition = str(input("What condition would you like (static or dynamic)? "))
    if condition in CONDITIONS:
        break

board = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
# Produces a random assortment of 6 letters of the alphabet that get their order randomised at each block
alphabet = ''.join([board[0], board[1], board[2]])
target_letters=''.join(random.sample(alphabet, k=6))
target_letters_list = random.sample(list(target_letters), len(target_letters))

counter = 0
n_repetitions = 6

window = Tk()

# keyboard frame
frame = Frame(window, relief=RAISED, bd=2)
frame.grid(row=1, column=0, columnspan=2)


letter_input = StringVar(window, " ")
value = StringVar(window, f"{target_letters_list[counter]}")
start_time = time.time()


def render_keyboard():
    for widget in frame.winfo_children():
        widget.destroy()

    for row, row_keys in enumerate(board):
        # keyboard row frame
        row_frame = Frame(frame)
        row_frame.grid(row=row + 1, column=0, columnspan=2)
        for column, letter in enumerate(row_keys):
            button_frame = Frame(row_frame, height=32, width=32)
            button_frame.pack_propagate(False)
            button_frame.grid(row=0, column=column)

            button = Button(
                button_frame,
                width=1,
                height=1,
                text=f"{letter}",
                command=lambda x=letter: append(letter_input, x),
            )
            button.pack(fill=BOTH, expand=True)


def start_block():
    global n_repetitions
    global counter
    global target_letters_list

    n_repetitions-=1
    if n_repetitions <= 0:
        value.set(f"All blocks are complete")
        window.after(1000, window.destroy)
        return
    target_letters_list = random.sample(list(target_letters), len(target_letters))
    counter = 0
    value.set(target_letters_list[counter])


def start_static(x, total_time):
    with open("experiment_static_log.txt", "a", newline="") as txtfile:
        writer = csv.writer(txtfile, delimiter=" ", quoting=csv.QUOTE_MINIMAL)
        # writer.writerow(
        #     [name] + [condition] + [x] + [n_repetitions] + [f"{total_time:.2f}"]
        # )
        writer.writerow(
            [x] + [n_repetitions] + [f"{total_time/1000:.2f}"]
        )


def start_dynamic(x, total_time):
    global board
    if condition == 'dynamic':
        row_1 = list(board[0])
        random.shuffle(row_1)
        row_1 = "".join(row_1)

        row_2 = list(board[1])
        random.shuffle(row_2)
        row_2 = "".join(row_2)

        row_3 = list(board[2])
        random.shuffle(row_3)
        row_3 = "".join(row_3)

        board = [row_1, row_2, row_3]
        render_keyboard()
    with open('experiment_dynamic_log.txt', 'a', newline='') as txtfile:
        writer = csv.writer(
            txtfile, delimiter=" ", quoting=csv.QUOTE_MINIMAL
        )
        # writer.writerow(
        #     [name] + [condition] + [x] + [n_repetitions] + [f"{total_time:.2f}"]
        # )  
        writer.writerow(
            [x] + [n_repetitions] + [f"{total_time/1000:.2f}"]
        )  


def append(the_value, x):
    global n_repetitions
    global counter
    global target_letters_list
    global start_time
    global board
    """
    Static: this presents a randomised keyboard layout to users, but the keyboard remains static across selections.
    Dynamic: this randomises the location of every character key after every selection.
    """

    the_value.set(the_value.get() + x)

    next_target = target_letters_list[counter]
    if x == next_target:
        total_time = (time.time() - start_time) * 1000
        if condition == 'static':
            start_static(x, total_time)
        else:
            start_dynamic(x, total_time)
        start_time = time.time()
        counter+=1
        if counter == len(target_letters_list):
            start_block()
        else:
            value.set(target_letters_list[counter])
    else:
        return

def clear_data(data):
    data.set("")


label = Label(window, textvariable=value)
label.grid(row=0, column=0, columnspan=2, pady=10, sticky="n")

if condition == 'static':
    row_1 = list(board[0])
    random.shuffle(row_1)
    row_1 = "".join(row_1)

    row_2 = list(board[1])
    random.shuffle(row_2)
    row_2 = "".join(row_2)

    row_3 = list(board[2])
    random.shuffle(row_3)
    row_3 = "".join(row_3)

    board = [row_1, row_2, row_3]


render_keyboard()


window.mainloop()
