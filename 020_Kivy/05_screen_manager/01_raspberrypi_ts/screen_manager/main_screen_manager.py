
# import kivy module 
import kivy 
  
# base Class of your App inherits from the App class. 
# app:always refers to the instance of your application 
from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import kivy._version as ver
import os

print('kivy version:', ver.__version__)

os.environ['DISPLAY']=':0.0'
print('echo $DISPLAY')
print()


# touch screen to mouse

# key event at 330 (BTN_TOUCH), down, up
# -->
# key event at 272 (['BTN_LEFT', 'BTN_MOUSE']), down
# key event at 272 (['BTN_LEFT', 'BTN_MOUSE']), up

from pynput.mouse import Listener
from pynput.mouse import Button, Controller
from threading import Thread

def run_listern_btn_ts():

    mouse = Controller()
    def on_move(x, y):
        mouse
        print('Pointer moved to {0}'.format((x, y)))
        # Press and release
        mouse.press(Button.left)
        mouse.release(Button.left)

    def run():
        with Listener(on_move=on_move) as listener:
            listener.join()

    from evdev import UInput, ecodes as e
    import time
    ui = UInput()
    ui = UInput.from_device('/dev/input/event0', name='ts_mouse')
    def run2():
        while True:        
            ui.write(e.EV_KEY, e.BTN_LEFT, 1)
            ui.syn()
            time.sleep(0.5)
            ui.write(e.EV_KEY, e.BTN_LEFT, 0)
            ui.syn()
            print('BTN_LEFT')
            time.sleep(1)

    # ui.close()
    import evdev
    def run_3():
        device = evdev.InputDevice('/dev/input/event0')

        mouse = Controller()

        for event in device.read_loop():
            if event.type == evdev.ecodes.EV_KEY:
                r = evdev.categorize(event)
                print(type(r), r.scancode, r.keystate, r.keycode)  # <class 'evdev.events.KeyEvent'> 330 1 BTN_TOUCH   <class 'evdev.events.KeyEvent'> 330 0 BTN_TOUCH
                # r.keystate key_up= 0 key_down= 1 key_hold= 2
                print(r)
                # if 'BTN_TOUCH' in str(r):
                #     print('ts down')
                #     print('ts up')
                #                 
                if r.keycode in 'BTN_TOUCH':
                    if r.keystate == r.key_down:
                        print('ts down')
                        mouse.press(Button.left)
                        
                    if r.keystate == r.key_up:
                        print('ts up')
                        mouse.release(Button.left)

    x = Thread(target=run_3, daemon=True)
    x.start()


# this restrict the kivy version i.e 
# below this kivy version you cannot  
# use the app or software 
# not coumpulsary to write it 
# kivy.require('1.9.1') 

# define different screens
class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

#  How to use Multiple kv files in kivy  https://www.geeksforgeeks.org/python-how-to-use-multiple-kv-files-in-kivy/
Builder.load_file('screen_01.kv')
kvfile = Builder.load_file('kivy_screen_manager.kv')

from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'show_cursor', 1)
Config.set('graphics', 'resizable', 0)
Config.write()

# define the App class 
# and just pass rest write on kvfile 
# not necessary to pass 
# can also define function in it 
class kvfileApp(App): 
    def build(self):
        return kvfile

run_listern_btn_ts()

kv = kvfileApp() 
kv.run() 