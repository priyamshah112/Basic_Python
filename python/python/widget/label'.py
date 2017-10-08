import tkinter

master = tkinter.Tk()

listbox =tkinter.Listbox(master)
listbox.pack()

Listbox.insert('end', "a list entry")

for item in ["one", "two", "three", "four"]:
    Listbox.insert('end', item)

master.mainloop()
