
import os
# при запуске по ssh для развертывание на дисплеи устройства
os.environ['DISPLAY']=':0.0'

# https://pythonhosted.org/pynput/mouse.html

# https://stackoverflow.com/questions/5060710/format-of-dev-input-event
# https://python-evdev.readthedocs.io/en/latest/apidoc.html
# pi@raspberrypi:~/kivy $ python3 -m pip install evdev

# from pynput.mouse import Listener
# from pynput.mouse import Button, Controller

# mouse = Controller()

# def on_move(x, y):
#     global mouse
#     print('Pointer moved to {0}'.format(
#         (x, y)))
#     # Press and release
#     mouse.press(Button.left)
#     mouse.release(Button.left)

# def on_click(x, y, button, pressed):
#     print('{0} at {1}'.format(
#         'Pressed' if pressed else 'Released',
#         (x, y)))
#     if not pressed:
#         # Stop listener
#         # return False
#         return True


# def on_scroll(x, y, dx, dy):
#     print('Scrolled {0}'.format(
#         (x, y)))
    



# Read pointer position
# print('The current pointer position is {0}'.format(
#     mouse.position))




# Collect events until released
# with Listener(
#         on_move=on_move,
#         on_click=on_click,
#         on_scroll=on_scroll) as listener:
#     listener.join()


from pynput.mouse import Listener
from pynput.mouse import Button, Controller
from threading import Thread

def run_listern():
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

    x = Thread(target=run, daemon=True)
    x.start()
    x.join()

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





if __name__ == '__main__':

	x = Thread(target=run_3, daemon=True)
	x.start()
	x.join()
#   run_listern()
