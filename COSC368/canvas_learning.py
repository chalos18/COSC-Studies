from tkinter import *

from tkinter.ttk import *

master = Tk()

c = Canvas(master, width=200, height=200)

c.pack()
c.create_line(0, 0, 200, 100, tag='cool')
c.create_line(0, 100, 200, 0, dash=(4, 4), tag="cool")
rect = c.create_rectangle(50, 25, 150, 75)

c.itemconfigure('cool', fill='blue')
c.itemconfigure(rect, fill='red')

# c.coords(rect, 10, 10, 50, 100)


"""
Function calls can be bound to specific items (or groups) using similar methods to item configuration.

For example, the following statements bind function calls to a Canvas item named "c". 
In both cases, the functions receive one parameter describing the event:
"""
# c.tag_bind(rect, "<ButtonPress-1>", foo)
# c.tag_bind("cool", "<ButtonPress-1>", bar)

master.mainloop()
