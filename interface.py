from tkinter import *
from data_koordinater import findkoordinater

window = Tk()
window.title("Interface")
window.geometry('800x200')

#opt = ["Unisex", "ADA"]

#variable = StringVar(window)
#variable.set(opt[0])

#dropdown = OptionMenu(window, variable, *opt)
#dropdown.grid(column=0, row=1)


def click():
    coords = txt.get()
    print("Finder toiletter for: "+ coords)
    print("begge",(findkoordinater(coords)))
    print((findkoordinater(coords)[0]))
    print((findkoordinater(coords)[1]))
#str(findkoordinater(data_lokation)[0])

var1 = IntVar()
Checkbutton(window, text="Unisex", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(window, text="ADA", variable=var2).grid(row=2, sticky=W)

label = Label(window, text="Indtast adresse: ")
label.grid(column=0, row=0)


btn = Button(window, text="Show Toilets", command=click)
btn.grid(row=3)

txt = Entry(window,width=40)
txt.grid(column=1, row=0)


window.mainloop()
	if len(decodeddatadict['data']) > 0 and isinstance(decodeddatadict['data'][0], dict):
		latitude = decodeddatadict['data'][0]['latitude'] #tager latitude fra decodeddatadict
		longitude = decodeddatadict['data'][0]['longitude'] #tager longitude fra decodeddatadict
	else:
		latitude, longitude = findkoordinater(lokation)
	return latitude, longitude #returnere latitude og longitude
