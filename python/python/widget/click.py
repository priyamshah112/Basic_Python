import tkinter
#The controller.
def click1():
    counter.set(counter.get()+1)
    
if __name__=='__main__':
    window=tkinter.Tk()
    #The model.
    counter=tkinter.IntVar()
    counter.set(0)
    #The views.
    frame=tkinter.Frame(window)
    frame.pack()

    button=tkinter.Button(frame,text='Click Me',command=click1)
    button.pack()

    label=tkinter.Label(frame,textvariable=counter)
    label.pack()

    #start the machinery!
    window=tkinter.Tk()
