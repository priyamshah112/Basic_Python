from tkinter import *

master = Tk()

var = StringVar(master)
var.set("SELECT") # initial value

option = OptionMenu(master, var, "I", "ME", "MYSELF", "PRIYAM")
option.pack()

#
# test stuff

def ok():
    print( "OPTION is", var.get())
    master.quit()

button = Button(master, text="OK", command=ok)
button.pack()

master.mainloop()
