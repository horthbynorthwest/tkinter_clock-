from tkinter import *

window = Tk()

def kg_to_multiple():
    gram = float(e1_value.get()) * 1000
    pound = float(e1_value.get()) * 2.20462
    ounce = float(e1_value.get()) * 35.274

    gram_text.delete("1.0", END)
    gram_text.insert(END, gram)

    pound_text.delete("1.0", END)
    pound_text.insert(END, pound)

    ounces_text.delete("1.0", END)
    ounces_text.insert(END, ounce)

b1 = Button(window, text="Convert", command=kg_to_multiple)
b1.grid(row=0,column=2)

kg_label = Label(text="Input kg value: ")
kg_label.grid(row=0, column=0)
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

gram_label = Label(text="Grams")
gram_label.grid(row=1, column=0)
gram_text = Text(window, height=1, width=25)
gram_text.grid(row=2, column=0)

pound_label = Label(text="Pounds")
pound_label.grid(row=1, column=1)
pound_text = Text(window, height=1, width=25)
pound_text.grid(row=2, column=1)

ounces_label = Label(text="Ounces")
ounces_label.grid(row=1, column=2)
ounces_text = Text(window, height=1, width=25)
ounces_text.grid(row=2, column=2)


window.mainloop()