import csv
import random
import time
from tkinter import *
import itertools

from tkinter.ttk import *

name = input("What is your name? ")

master = Tk()

c_width = 600
c_height = 500
c = Canvas(master, width=c_width, height=c_height)
c.pack()

# There are 12 combinations of distance and width done at a random order
distances = [64, 128, 256, 512]
widths = [8, 16, 32]

combinations = list(itertools.product(distances, widths))
len_combinations = len(combinations)
random_combinations = random.sample(combinations, len_combinations)

n_repetitions = 8

current_combination = 0
current_repetition = 0
start_time = None
left_rect = None
right_rect = None

# for each combination of the above, the user should execute an even number of task repetitions
# 4 repetitions means 4 clicks

# log the time taken between showing the next green targed and it being successfully clicked on
# [Name] [distance] [width] [selection number] [time]
# selection number ranges from 1 to the number of repetitions at each combination of distance and width

# Green swaps colours
def swap_left(event, left_rect, right_rect):
    global start_time, current_repetition, current_combination
    left_colour = c.itemcget(left_rect, "fill")

    if left_colour == "green":
        c.itemconfigure(left_rect, fill="blue")
        c.itemconfigure(right_rect, fill="green")

        end_time = time.time()
        elapsed = end_time - start_time
        with open(f'experiment_{name}.txt', "a", newline="") as txtfile:
            writer = csv.writer(txtfile, delimiter=" ", quoting=csv.QUOTE_MINIMAL)
            # [Name] [distance] [width] [selection number] [time]
            writer.writerow(
                [name] + [random_combinations[current_combination][0]] + [random_combinations[current_combination][1]] + [current_repetition + 1] + [f"{elapsed:.2f}"]
            )

        current_repetition += 1
        print(current_repetition)
        master.after(300, next_rep)


def swap_right(event, left_rect, right_rect):
    global start_time, current_repetition, current_combination
    right_colour = c.itemcget(right_rect, "fill")

    if right_colour == "green":
        c.itemconfigure(left_rect, fill="green")
        c.itemconfigure(right_rect, fill="blue")

        end_time = time.time()
        elapsed_ms = int((end_time - start_time) * 1000)
        with open(f'experiment_{name}.txt', "a", newline="") as txtfile:
            writer = csv.writer(txtfile, delimiter=" ", quoting=csv.QUOTE_MINIMAL)
            # [Name] [distance] [width] [selection number] [time]
            writer.writerow(
      )

        current_repetition += 1
        print(current_repetition)
        print(elapsed_ms)
        master.after(300, next_rep)


def next_rep():
    global current_combination, current_repetition

    if current_repetition >= n_repetitions:
        current_combination += 1
        current_repetition = 0

    if current_combination < len(random_combinations):
        render_columns(random_combinations[current_combination])
    else:
        print("Complete")
        c.delete("all")
        c.create_text(c_width // 2, c_height // 2, text="Complete", font=("Arial", 24))


def set_start_time():
    global start_time
    start_time = time.time()


def render_columns(combination):
    global left_rect, right_rect, start_time

    leftrec_colour = 'blue'
    rightrec_colour = 'green'

    if left_rect:
        leftrec_colour = c.itemcget(left_rect, "fill")
    if right_rect:
        rightrec_colour = c.itemcget(right_rect, "fill")

    c.delete("all")

    distance, width = combination
    rec_distance = distance
    rec_width = width
    total_span = rec_distance + rec_width
    margin = (c_width - total_span) / 2

    left_rect = c.create_rectangle(margin, 0, (margin + rec_width), c_height, fill=leftrec_colour)
    right_rect = c.create_rectangle((margin + rec_distance), 0, (margin + rec_width + rec_distance), c_height, fill=rightrec_colour)

    c.tag_bind(
        left_rect,
        "<ButtonPress-1>",
        lambda event: swap_left(event, left_rect, right_rect),
    )
    c.tag_bind(
        right_rect,
        "<ButtonPress-1>",
        lambda event: swap_right(event, left_rect, right_rect),
    )

    master.after(50, lambda: set_start_time())


next_rep()

# c.itemconfigure('cool', fill='blue')
# c.itemconfigure(rect, fill='red')

# c.coords(rect, 10, 10, 50, 100)


"""
Function calls can be bound to specific items (or groups) using similar methods to item configuration.

For example, the following statements bind function calls to a Canvas item named "c". 
In both cases, the functions receive one parameter describing the event:
"""
# c.tag_bind(rect, "<ButtonPress-1>", foo)
# c.tag_bind("cool", "<ButtonPress-1>", bar)

master.mainloop()
