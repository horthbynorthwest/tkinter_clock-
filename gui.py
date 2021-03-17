from tkinter import *

window = Tk()

def km_to_miles():
    miles = float(e1_value.get()) * 1.6
    t1.insert(END, miles)

b1 = Button(window, text="Convert", command=km_to_miles)
b1.grid(row=0,column=0)

km_label = Label(text="KM")
km_label.grid(row=0, column=1)
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=1, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)
t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=2)

window.mainloop()