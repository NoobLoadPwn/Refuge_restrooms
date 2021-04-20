import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from data_koordinater import findkoordinater


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Indtast adresse: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

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
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        adresse = self.name.text

        print("Finder toiletter for:", adresse)
        print(findkoordinater(adresse))

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
