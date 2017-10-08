"""GUI FOR RECORDING FORM   FRONTEND   PAGE 1   LOGIN PAGE"""
from tkinter import *
def screen():
    
    
    window = Tk()
    
    frame=Frame(bg='green')
    lbl1=Label(window,text='\t\t ~~WELCOME TO K J SOMAIYA COLLEGE OF ENGINEERING~~ ')
    lbl1.pack()
    lbl1=Label(window,text='\t ~STUDENT RECORD FORM~' )
    lbl1.pack()

    lbl1=Label(window,text='ROLL NUMBER - ')
    lbl1.pack()
    k=StringVar()
    e=Entry(window,textvariable=k)
    e.pack()
    
    lbl2=Label(window,text='NAME - ')
    lbl2.pack()
    k=StringVar()
    e=Entry(window,textvariable=k)
    e.pack()
    
    lbl3=Label(window,text='PROCTOR NAME - ')
    lbl3.pack()
    k=StringVar()
    e=Entry(window,textvariable=k)
    e.pack()
    
    lbl4=Label(window,text='EXPOSURE COURSE - ')
    lbl4.pack()
    k=StringVar()
    e=Entry(window,textvariable=k)
    e.pack()
    
    lbl5=Label(window,text='OTHER ACTIVITIES - ')
    lbl5.pack()
    k=StringVar()
    e=Entry(window,textvariable=k)
    e.pack()
    b=Button(window,text="SUBMIT")
    b.pack()

    window=mainloop()
screen()
