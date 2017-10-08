from tkinter import *

master = Tk()

w = Scale(master, from_=0, to=100)
w.pack()
w =Label(text="VOLUME")
w.pack()
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()
w =Label(text="BASE")
w.pack()






master.mainloop()
