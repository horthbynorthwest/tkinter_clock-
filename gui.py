from tkinter import *

window = Tk()

def km_to_miles():
    t1.insert(END,"Success!")

b1 = Button(window,text="Run",command=km_to_miles)
b1.grid(row=0,column=0)

e1=Entry(window)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)

window.mainloop()