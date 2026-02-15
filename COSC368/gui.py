from tkinter import *
from tkinter.ttk import *

# Geometry managers are used to control where widgets are placed within their parent widget
# Widgets will not appear unless placed using a geometry manager

# intitialise Tk's capabilities
window = Tk()

# Packer ------------------
# side_labels = ["bottom1", "bottom2", "top1", "top2", "left1", "right1"]
# for theside in side_labels:
#     button = Button(window, text=theside)
#     button.pack(side=theside[0:-1])
# --------------------------

# Frames for Layout ----------
# frame_left = Frame(window, borderwidth=4, relief=RIDGE)
# frame_left.pack(side="left", fill="y", padx=5, pady=5)
# frame_right = Frame(window)
# frame_right.pack(side="right")

# button1 = Button(frame_left, text="Button 1")
# button1.pack(side="top")
# button2 = Button(frame_left, text="Button 2")
# button2.pack(side="bottom")

# for label_num in range(4):
#     button = Button(frame_right, text="Button" + str(label_num + 3))
#     button.grid(row=label_num // 2, column=label_num % 2)
# ---------------

# Gridder ----------
# for label_num in range(6):
#     button = Button(window, text="Button" + str(label_num))
#     button.grid(row=label_num // 2, column=label_num % 3)
#     if label_num == 1:
#         button.grid(columnspan=2, sticky="ew")  # compass directions (N, E, S, W)
#     elif label_num == 3:
#         button.grid(rowspan=2, sticky="ns")  # compass directions (N, E, S, W)

# window.columnconfigure(1, weight=1)
# window.rowconfigure(1, weight=1)
# window.rowconfigure(2, weight=1)

# ------------

# s = Style()
# s.configure('TButton', font='helvetica 24', foreground='green')

# # support mutable strings and set it
data = StringVar()
data.set("")

label = Label(window, textvariable=data)
label.grid(row=0, column=0)

entry = Entry(window, textvariable=data)
entry.grid(row=1, column=0)

def clear_data(data):
    data.set("")

clear = Button(window, text="Clear", command=lambda:clear_data(data))
clear.grid(row=2, column=0)

quit = Button(window, text="Quit", command=window.destroy)
quit.grid(row=3, column=0)

# initialises the infinite loop that continually awairs user input on the GUI
window.mainloop()
