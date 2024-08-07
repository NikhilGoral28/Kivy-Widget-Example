from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty


class WidgetsExample(GridLayout):
    my_text = StringProperty("Hello!")
    def on_button_click(self):
        print("button clicked")
        self.my_text = "you clicked"




class StackLayout(StackLayout):
    pass

class GridLayout(GridLayout):
    pass

class BoxLayout(BoxLayout):
    pass

class MainWidget(Widget):
    pass 
class TheLabApp(App):
    pass

TheLabApp().run()
