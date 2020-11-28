### Setup Kivy on Raspberri Py 3b+
[kivy.org Installation on Raspberry Pi](https://kivy.org/doc/stable/installation/installation-rpi.html)
```sh
sudo apt update
sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
   pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   python-setuptools libgstreamer1.0-dev git-core \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} python-dev libmtdev-dev \
   xclip xsel libjpeg-dev]
```
```sh
python3 -m pip install --upgrade pip setuptools
python3 -m pip install --upgrade Cython pillow
```
```sh
python3 -m pip install kivy
```
