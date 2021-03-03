from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import kivy._version as ver


# define different screens
class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

# load design file .kv
# Builder.load_file('screen_1.kv')
# Builder.load_file('screen_2.kv')
kv = Builder.load_file('screen_manager.kv')

class WinApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    print('kivy version:', ver.__version__)
    WinApp().run()