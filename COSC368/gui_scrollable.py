from tkinter import *
import random
import string

window = Tk()
window.title("2D Scrolling Text")

text = Text(window, wrap=NONE, width=20, height=8)
text.grid(row=0, column=0, sticky="nsew")

# Vertical scrollbar
scrollbar_ver = Scrollbar(window, orient=VERTICAL, command=text.yview)
scrollbar_ver.grid(row=0, column=1, sticky="ns")

# Horizontal scrollbar
scrollbar_hor = Scrollbar(window, orient=HORIZONTAL, command=text.xview)
scrollbar_hor.grid(row=1, column=0, sticky="ew")

# Configure scroll commands
text.configure(yscrollcommand=scrollbar_ver.set, xscrollcommand=scrollbar_hor.set)

# test text
characters = string.ascii_letters + string.digits
random_string = ''.join(random.choice(characters) for _ in range(50))
sample_text = "".join(f"{random_string}\n" for _ in range(50))
text.insert(END, sample_text)

window.mainloop()
