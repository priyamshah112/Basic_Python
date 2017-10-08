from tkinter import *

pooja = Tk()

window = Spinbox(pooja, from_=0, to=10)
window.pack()

mainloop()


window = Spinbox(values=(1, 2, 4, 8))
window.pack()
