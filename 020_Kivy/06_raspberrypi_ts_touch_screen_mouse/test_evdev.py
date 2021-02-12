import evdev
import os
from evdev import UInput, _input, ecodes as e

# https://python-evdev.readthedocs.io/en/latest/usage.html
print(evdev.list_devices())

# devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
# print(devices)
# for device in devices:
#     print(device)
    # print(device.path, device.name, device.phys)

path_dev = '/dev/input/event0'
# devices = evdev.InputDevice(path)
# print(devices)

fd = os.open(path_dev, os.O_RDONLY | os.O_NONBLOCK)

#: A non-blocking file descriptor to the device file.
# self.fd = fd

# Returns (bustype, vendor, product, version, name, phys, capabilities).
info_res = _input.ioctl_devinfo(fd)

os.close(fd)

#: A :class:`DeviceInfo <evdev.device.DeviceInfo>` instance.
# self.info = DeviceInfo(*info_res[:4])

#: The name of the event device.
# self.name = info_res[4]

print(info_res[4])
print(info_res)

device = evdev.InputDevice('/dev/input/event0')  # '/dev/input/event0'  '/dev/input/event2'
print(device)
print(device.capabilities(verbose=True))
print(e.ecodes)

# sudo
# ui = UInput.from_device('/dev/input/event0', name='test-controller')
# from evdev import UInput, ecodes as e
ui = UInput()
ui.write(e.BTN_MOUSE, e.BTN_LEFT, 1)
ui.write(e.BTN_MOUSE, e.BTN_LEFT, 0)
ui.syn()
# ui.close()

print(evdev.list_devices())


def run():
    device = evdev.InputDevice('/dev/input/event1')
    print(device)
    for event in device.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            print(evdev.categorize(event))


from threading import Thread
#  device /dev/input/event1, name "USB Keyboard", phys "usb-0000:00:12.1-2/input0"
x = Thread(target=run, daemon=True)
x.start()


# read_one() read()
for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        r = evdev.categorize(event)
        print(type(r), r.scancode, r.keystate, r.keycode)  # <class 'evdev.events.KeyEvent'> 330 1 BTN_TOUCH   <class 'evdev.events.KeyEvent'> 330 0 BTN_TOUCH
        # r.keystate key_up= 0 key_down= 1 key_hold= 2
        print(r)
        # if 'BTN_TOUCH' in str(r):
        #     print('ts down')
        #     print('ts up')

        
        if r.keycode in 'BTN_TOUCH':
            if r.keystate == r.key_down:
                print('ts down')
                ui.write(e.EV_KEY, e.BTN_LEFT, 1)

            if r.keystate == r.key_up:
                print('ts up')
                ui.write(e.EV_KEY, e.BTN_LEFT, 0)
            ui.syn()

ui.close()

# ['/dev/input/event5', '/dev/input/event4', '/dev/input/event3', '/dev/input/event2', '/dev/input/event1', '/dev/input/event0']
# raspberrypi-ts
# (25, 0, 0, 0, 'raspberrypi-ts', '', '')
# device /dev/input/event0, name "raspberrypi-ts", phys ""
# key event at 1612459950.471755, 330 (BTN_TOUCH), down
# key event at 1612459950.591766, 330 (BTN_TOUCH), up
# key event at 1612459951.311769, 330 (BTN_TOUCH), down
# key event at 1612459951.371766, 330 (BTN_TOUCH), up
# key event at 1612459951.581760, 330 (BTN_TOUCH), down
# key event at 1612459951.671778, 330 (BTN_TOUCH), up
# key event at 1612459951.911755, 330 (BTN_TOUCH), down
# key event at 1612459951.941756, 330 (BTN_TOUCH), up
# key event at 1612459952.091757, 330 (BTN_TOUCH), down
# key event at 1612459952.181752, 330 (BTN_TOUCH), up
# key event at 1612459952.331765, 330 (BTN_TOUCH), down
# key event at 1612459952.421747, 330 (BTN_TOUCH), up
# key event at 1612459952.571759, 330 (BTN_TOUCH), down
# key event at 1612459952.661749, 330 (BTN_TOUCH), up
# key event at 1612459952.811761, 330 (BTN_TOUCH), down
# key event at 1612459952.931751, 330 (BTN_TOUCH), up
# key event at 1612459953.051761, 330 (BTN_TOUCH), down
# key event at 1612459953.141748, 330 (BTN_TOUCH), up
# key event at 1612459953.291760, 330 (BTN_TOUCH), down
# key event at 1612459953.351769, 330 (BTN_TOUCH), up
# key event at 1612459953.471758, 330 (BTN_TOUCH), down
# key event at 1612459953.561749, 330 (BTN_TOUCH), up
# key event at 1612459953.681763, 330 (BTN_TOUCH), down

# device /dev/input/event2, name "MOSART Semi. 2.4G Keyboard Mouse", phys "usb-0000:01:00.0-1.3/input1"
# key event at 1612460036.837949, 272 (['BTN_LEFT', 'BTN_MOUSE']), down
# key event at 1612460036.965956, 272 (['BTN_LEFT', 'BTN_MOUSE']), up
# key event at 1612460038.246124, 273 (BTN_RIGHT), down
# key event at 1612460038.310139, 273 (BTN_RIGHT), up
# key event at 1612460039.702333, 272 (['BTN_LEFT', 'BTN_MOUSE']), down
# key event at 1612460039.830340, 272 (['BTN_LEFT', 'BTN_MOUSE']), up
# key event at 1612460041.910619, 272 (['BTN_LEFT', 'BTN_MOUSE']), down
# key event at 1612460041.990627, 272 (['BTN_LEFT', 'BTN_MOUSE']), up
# key event at 1612460042.470691, 272 (['BTN_LEFT', 'BTN_MOUSE']), down
# key event at 1612460042.518697, 272 (['BTN_LEFT', 'BTN_MOUSE']), up
# key event at 1612460044.342925, 273 (BTN_RIGHT), down
# key event at 1612460044.406938, 273 (BTN_RIGHT), up

# ['/dev/input/event5', '/dev/input/event4', '/dev/input/event3', '/dev/input/event2', '/dev/input/event1', '/dev/input/event0']
# raspberrypi-ts
# (25, 0, 0, 0, 'raspberrypi-ts', '', '')
# device /dev/input/event0, name "raspberrypi-ts", phys ""
# {('EV_SYN', 0): [('SYN_REPORT', 0), ('SYN_CONFIG', 1), ('SYN_DROPPED', 3)], ('EV_KEY', 1): [('BTN_TOUCH', 330)], ('EV_ABS', 3): 
# [(('ABS_X', 0), AbsInfo(value=249, min=0, max=479, fuzz=0, flat=0, resolution=0)), (('ABS_Y', 1), AbsInfo(value=514, min=0, max=799, fuzz=0, flat=0, resolution=0)), 
# (('ABS_MT_SLOT', 47), AbsInfo(value=0, min=0, max=9, fuzz=0, flat=0, resolution=0)), (('ABS_MT_POSITION_X', 53), 
# AbsInfo(value=0, min=0, max=479, fuzz=0, flat=0, resolution=0)), (('ABS_MT_POSITION_Y', 54), AbsInfo(value=0, min=0, max=799, fuzz=0, flat=0, resolution=0)), 
# (('ABS_MT_TRACKING_ID', 57), AbsInfo(value=0, min=0, max=65535, fuzz=0, flat=0, resolution=0))]}

# device /dev/input/event2, name "MOSART Semi. 2.4G Keyboard Mouse", phys "usb-0000:01:00.0-1.3/input1"
# {('EV_SYN', 0): [('SYN_REPORT', 0), ('SYN_CONFIG', 1), ('SYN_MT_REPORT', 2), ('?', 4)], ('EV_KEY', 1): 
# [(['BTN_LEFT', 'BTN_MOUSE'], 272), ('BTN_RIGHT', 273), ('BTN_MIDDLE', 274), ('BTN_SIDE', 275), ('BTN_EXTRA', 276)],
#  ('EV_REL', 2): [('REL_X', 0), ('REL_Y', 1), ('REL_HWHEEL', 6), ('REL_WHEEL', 8), ('?', 11), ('?', 12)], ('EV_MSC', 4): [('MSC_SCAN', 4)]}