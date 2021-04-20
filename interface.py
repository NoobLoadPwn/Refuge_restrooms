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
    print(findkoordinater(coords))


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

#----------------------------#----------------------------#----------------------------#----------------------------
        self.inside.add_widget(Label(text="Indtast adresse: "))  # Add a label widget
        self.name = TextInput(multiline=False)  # Create a Text input box stored in the name variable
        self.inside.add_widget(self.name)  # Add the text input widget to the GUI

        self.inside.add_widget(Label(text = "ADA"))
        self.check = CheckBox(active = True)
        self.inside.add_widget(self.check)

        self.inside.add_widget(Label(text="Unisex"))
        self.check = CheckBox(active=True)
        self.inside.add_widget(self.check)

        self.inside.add_widget(Label(text="C++"))
        self.check = CheckBox(active=True)
        self.inside.add_widget(self.check)

        self.add_widget(self.inside)
        self.submit = Button(text="Submit", font_size=40)
        self.add_widget(self.submit)
#----------------------------#----------------------------#----------------------------#----------------------------
<MyGridLayout>:

    label:mylabel
    cols:2
    spacing:10

    Label:
        text:"ADA"
        font_size:30

    CheckBox:
        on_active:root.checkbox_click(self, self.active)

    Label:
        text:"Unisex"
        font_size:30

    CheckBox:
        on_active:root.checkbox_click(self, self.active)

    Label:
        text:"Changing table"
        font_size:30

    CheckBox:
        on_active:root.checkbox_click(self, self.active)

    Label:
        text:"Label"
        font_size:20

    Button:
#----------------------------#----------------------------#----------------------------#----------------------------
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
import requests
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

Builder.load_file('MyApp.kv')

class MyGridLayout(GridLayout):

    def checkbox_click(self, instance, value):
        if value is True:
            self.label.text = "Checkbox Checked"

        else:
            self.label.text = "Checkbox Unchecked"

class CheckBoxEx(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    CheckBoxEx().run()






<MyGrid>:

    name: name

    GridLayout:
        cols:1
        size: root.width - 200, root.height -200
        pos: 100, 100

        GridLayout:
            cols:2

            Label:
                text: "Adresse: "
                font_size:30
            TextInput:
                id: name
                multiline:False

            Label:
                text:"ADA"
                font_size:30
            CheckBox:
                id:ADA
                on_state: root.checkBoxChanged(self, 'ADA')

            Label:
                text:"Unisex"
                font_size:30
            CheckBox:
                id:Unisex
                on_state: root.checkBoxChanged(self, 'Unisex')

            Label:
                text:"Changing table"
                font_size:30
            CheckBox:
                id:CT
                on_state: root.checkBoxChanged(self, 'Changing table')

        Button:
            text:"Submit"
            on_press:
                root.btn()
                app.sm.transition.direction = 'right'
                app.sm.current = 'Welcome'
