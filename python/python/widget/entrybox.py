from tkinter import *
master=Tk()
v=StringVar()
g=StringVar()
b=Button(master,text="username").grid(row=1,column=0)
b1=Button(master,text="password").grid(row=0,column=0)

e=Entry(master, textvariable=v).grid(row=0,column=1)
e1=Entry(master, textvariable=g).grid(row=1,column=1)
label=Label(master,text="sign in").grid(row=2,column=0)
s=v.get()
s=g.get()
mainloop()
