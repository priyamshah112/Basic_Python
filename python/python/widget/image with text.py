import tkinter

root = tkinter.Tk()

text1 = tkinter.Text(root, height=20, width=30)
photo=tkinter.PhotoImage(file='name.png')
text1.insert('end','\n')
text1.image_create('end', image=photo)

text1.pack(side='left')

text2 = tkinter.Text(root, height=20, width=50)
scroll = tkinter.Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color', foreground='#476042', 
						font=('Tempus Sans ITC', 12, 'bold'))
text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
text2.insert('end','\nWilliam Shakespeare\n', 'big')
quote = """
To be, or not to be that is the question:
Whether 'tis Nobler in the mind to suffer
The Slings and Arrows of outrageous Fortune,
Or to take Arms against a Sea of troubles,
"""
text2.insert('end', quote, 'color')
text2.insert('end', 'follow-up\n', 'follow')
text2.pack(side='left')
scroll.pack(side='right')

root.mainloop()
