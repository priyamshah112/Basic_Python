"""GUI FOR RECORDING FORM   FRONTEND   PAGE 1   LOGIN PAGE"""
from tkinter import *
def screen():
    
    
    window = Tk()
    
    frame=Frame(bg='green')
    lbl1=Label(window,text='\t\t ~~WELCOME TO K J SOMAIYA COLLEGE OF ENGINEERING~~ ')
    lbl1.pack()
    lbl1=Label(window,text='\t ~STUDENT RECORD FORM~' )
    lbl1.pack()

    var=StringVar()
    
    
    lbl1=Label(window,text='\n 1]APPLIED PHYSICS ' )
    lbl1.pack()
    
    lbl1=Label(window,text='\n 2]APPLIED CHEMISTRY ' )
    lbl1.pack()
    lbl1=Label(window,text='\n 3]APPLIED MATHEMATICS ' )
    lbl1.pack()

    
    d=Checkbutton(window,text="BEEE",variable=var,onvalue=1).pack(anchor=W)
    e=Checkbutton(window,text="ENGINEERING DRAWING",variable=var,onvalue=1).pack(anchor=W)
    f=Checkbutton(window,text="FCP",variable=var,onvalue=2).pack(anchor=W)
    g=Checkbutton(window,text="MECHANICS",variable=var,onvalue=2).pack(anchor=W)
    h=Checkbutton(window,text="EVS",variable=var,onvalue=2).pack(anchor=W)
    i=Checkbutton(window,text="CS",variable=var,onvalue=1).pack(anchor=W)

    b=Button(window,text="SUBMIT")
    b.pack()
    window=mainloop()
screen()
