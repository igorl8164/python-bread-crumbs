def area_of_country(country, area):
    land_area = 148940000
    percent_area = area * 100 / land_area
    return f"{country} is {round(percent_area, 2)}% of the total world's landmass"


import time
import mouse

def callback():
    print('callback ')

def callback_x():
    print('callback x')

def callback_x2():
    print('callback x2')

X = 'x'
X2 = 'x2'

UP = 'up'
DOWN = 'down'

# mouse.on_middle_click(callback, args=())

mouse.on_button(callback_x, args=(), buttons=(X, ), types=(DOWN, ))
mouse.on_button(callback_x2, args=(), buttons=(X2, ), types=(DOWN, ))


from pynput import mouse


while True:
    time.sleep(0.01)

    with mouse.Events() as events:
        # Block at most one second
        event = events.get(1.0)
        if event is None:
            print('You did not interact with the mouse within one second')
        else:
            print('Received event {}'.format(event))

exit(0)

