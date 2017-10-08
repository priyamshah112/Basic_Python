"""GUI FOR RECORDING FORM   FRONTEND   PAGE 1   LOGIN PAGE"""
from tkinter import *
def screen():
    
    
    window = Tk()
    
    frame=Frame(bg='green')
    lbl1=Label(window,text='\t\t ~~WELCOME TO K J SOMAIYA COLLEGE OF ENGINEERING~~ ')
    lbl1.pack()
    lbl1=Label(window,text='\t ~STUDENT RECORD FORM~' )
    lbl1.pack()
    r=IntVar()
    Radiobutton(window, text="\t STUDENT",variable=r,value=1).pack(anchor=W,side='top')
    Radiobutton(window, text="\t PROFESSOR", variable=r,value=2).pack(anchor=W,side='top')
    
    lbl1=Label(window,text='LOGIN')
    lbl1.pack()
    k=StringVar()
    e=Entry(window,textvariable=k)
    e.pack()
    
    lbl1=Label(window,text='PASSWORD')
    lbl1.pack()
    k=StringVar()
    e=Entry(window,textvariable=k)
    e.pack()

    b=Button(window,text="SUBMIT")
    b.pack()
    
    frame.pack()
    window.mainloop()
screen()
