import tkinter
from tkinter import *
from tkinter.ttk import *

def clicked():
    pgbar.start(10)

def stopped():
    pgbar.stop()

root = tkinter.Tk()
root.geometry("500x500")

pgbar = Progressbar(
    root,
    length = 200,
    orient = HORIZONTAL,
    maximum = 100,
    value = 50,
    mod = 'indeterminate'
)
pgbar.pack()

btn = Button(
    root,
    text = "Click Me",
    command = clicked,
)
btn.pack()

btn2 = Button(
    root,
    text = "Stop",
    command = stopped,
)
btn2.pack()

root.mainloop()