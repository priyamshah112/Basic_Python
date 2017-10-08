"""WIDGET 1: TEXT"""
import tkinter
window = tkinter.Tk()
f=tkinter.Text(window,height=20,width=300)
f.pack()
quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
f.insert('end',quote)
window.mainloop()
