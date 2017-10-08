"""GUI FOR RECORDING FORM   FRONTEND   PAGE 1   LOGIN PAGE"""
from tkinter import *
def screen():
    
    
    window = Tk()
    
    frame=Frame(bg='green')
    lbl1=Label(window,text='\t\t ~~WELCOME TO K J SOMAIYA COLLEGE OF ENGINEERING~~ ')
    lbl1.pack()
    lbl1=Label(window,text='\t ~STUDENT RECORD FORM~' )
    lbl1.pack()

    lbl1=Label(window,text='\tSELECT ANY 1 OPTIONS ')
    lbl1.pack()
    v=IntVar()
    
    Radiobutton(window, text="\t1] CREATE STUDENT RECORD",variable=v,value=1).pack(anchor=W)
    Radiobutton(window, text="\t2] READ STUDENT RECORD", variable=v,value=2).pack(anchor=W)
    Radiobutton(window, text="\t3] REWRITE STUDENT RECORD",variable=v, value=3).pack(anchor=W)
    Radiobutton(window, text="\t4] DELETE STUDENT RECORD",variable=v ,  value=4).pack(anchor=W)
    Radiobutton(window, text="\t5] EXIT ",variable=v,value=5).pack(anchor=W)
    lbl1.pack()

    b=Button(window,text="SUBMIT")
    b.pack()
    
    window=mainloop()
screen()
 
