import kivy
from kivy.app import App
from kivy.uix.label import Label
import os
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class MyToggleButton(BoxLayout):
    def __init__(self, **kwargs):
        super(MyToggleButton, self).__init__(**kwargs)
        self.bind(on_touch_down=self.dn)
        # b = self = BoxLayout()
        
    pass

    def dn(self, event, instance):
        print(event)
        print(instance)
        print()
        print(self.pos)
        print(self.pos_hint)
        print(self.size)
        print(self.size_hint)
        print(self.width)
        print(self.height)
        print(self.x)
        print(self.center_x)
        print(self.y)
        print(self.center_y)
        print(self.ids.lb)
        print(self.ids.rl)
        rl = self.ids.rl
        print(rl.pos)
        print(rl.pos_hint)
        print(rl.size)
        print(rl.size_hint)
        print(rl.width)
        print(rl.height)
        print(rl.x)
        print(rl.center_x)
        print(rl.y)
        print(rl.center_y)





class MyWindow(App):
    def build(self):
        return MyToggleButton()
        # return Label(text='Hello World', font_size=72)

if __name__ == '__main__':

    # при запуске по ssh для развертывание на дисплеи устройства
    os.environ['DISPLAY']=':0.0'
    print('echo $DISPLAY')
    print()

    # self = BoxLayout()

    # отключить мультитач и красные круги от правой и центральной кнопок мыши
    # https://kivy.org/doc/stable/api-kivy.input.providers.mouse.html
    Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

    # во весь экран без рамки окна
    # https://kivy.org/doc/stable/api-kivy.config.html
    from kivy.config import Config
    Config.set('graphics', 'show_cursor', 1)
    Config.set('graphics', 'resizable', 0)
    Config.set('graphics', 'allow_screensaver', 0)
    Config.set('graphics', 'fullscreen', 'auto')
    Config.set('graphics', 'borderless', 1)
    Config.write()

    # 800 480

    MyWindow().run()