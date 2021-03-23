from tkinter import *

window = Tk()
window.title("Interface")
window.geometry('800x200')

#opt = ["Unisex", "ADA"]

#variable = StringVar(window)
#variable.set(opt[0])

#dropdown = OptionMenu(window, variable, *opt)
#dropdown.grid(column=0, row=1)

var1 = IntVar()
Checkbutton(window, text="Unisex", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(window, text="ADA", variable=var2).grid(row=2, sticky=W)

label = Label(window, text="Indtast adresse: ")
label.grid(column=0, row=0)

def click():
    coords = txt.get()
    if coords == "Vordingborg":
        print("ZBC")


btn = Button(window, text="Show Toilets", command=click)
btn.grid(row=3)

txt = Entry(window,width=40)
txt.grid(column=1, row=0)


window.mainloop()
