from tkinter import *
master = Tk()


def hello():
    print ("hello!")

# create a toplevel menu
menubar = Menu(master)
menubar.add_command(label="Hello!", command=hello)
menubar.add_command(label="Quit!", command=master.quit)

# display the menu
master.config(menu=menubar)


master.mainloop()
