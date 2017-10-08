from tkinter import *

window = Tk()

v = IntVar()

Radiobutton(window, text="CHESSE", variable=v, value=1).pack(anchor=W)
Radiobutton(window, text="JAM", variable=v, value=2).pack(anchor=W)
Radiobutton(window, text="BUTTER", variable=v, value=3).pack(anchor=W)
Radiobutton(window, text="BREAD", variable=v, value=4).pack(anchor=W)

window.mainloop()
