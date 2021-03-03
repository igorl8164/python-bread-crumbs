

### Kivy install on rpi4

```
pi@raspberrypi:~ $ python3 -m pip install --upgrade pip setuptools virtualenv

pi@raspberrypi:~ $ python3 -m pip install kivy[full] kivy_examples
```

For the Raspberry Pi, you must additionally install the dependencies listed in source dependencies before installing Kivy above.

sudo apt update
sudo apt install python3-setuptools git-core python3-dev

sudo apt update
sudo apt install pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   libgstreamer1.0-dev \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} libmtdev-dev \
   xclip xsel libjpeg-dev

sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev

### Hello World
```
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
```



(Installing Kivy)[https://kivy.org/doc/stable/gettingstarted/installation.html]
