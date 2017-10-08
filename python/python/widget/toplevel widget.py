from tkinter import *


top = Toplevel()
top.title("HI")

msg = Message(top, text="HOW ARE YOU?")
msg.pack()

button = Button(top, text="Dismiss", command=top.destroy)
button.pack()

