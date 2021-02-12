import kivy
from kivy.app import App
from kivy.uix.label import Label
import os


class MyApp(App):
    def build(self):
        return Label(text='Hello World', font_size=72)


if __name__ == '__main__':

    os.environ['DISPLAY']=':0.0'
    print('echo $DISPLAY')
    print()

    MyApp().run()
