import kivy
from kivy.app import App
from kivy.uix.label import Label
import os

# raspberry pi
# https://www.youtube.com/watch?v=dLgquj0c5_U
# Codemy.com Intro To Kivy - Installing Kivy on Windows - Python Kivy GUI Tutorial #1

# sudo dphys-swapfile swapoff   # STOP THE SWAP
# sudo nano /etc/dphys-swapfile  # MODIFY THE SIZE OF THE SWAP
# CONF_SWAPSIZE=1024
# sudo dphys-swapfile swapon  # START THE SWAP
# sudo reboot now

# pi@raspberrypi:~ $ sudo pip3 install kivy==2.0.0rc4
# sudo apt-get install libavcodec-dev 
# sudo apt-get install libsdl2-dev
# sudo apt-get install libavformat-dev 
# sudo apt-get install libavdevice-dev
# sudo pip3 install ffpyplayer
# sudo apt-get install python3-sdl2

# Work

# sodo pip3 install git+https://github.com/kivy/kivy.git@master

# --------------------------------------------------------------- #
# remove the old packages
# sudo apt-get remove --purge *kivy*

#  sudo add-apt-repository ppa:kivy-team/kivy
#  sudo apt-get update
#  sudo apt-get install python3-kivy

#  # Install the dependencies
# sudo apt-get install python3-setuptools libsdl2-dev libavformat-dev libavdevice-dev python3-sdl2

# Install python3-kivy via ppa. Pip install didn't work for me.
# sudo add-apt-repository ppa:kivy-team/kivy
# sudo apt-get update
# sudo apt-get install python3-kivy

# Install ffpyplayer
# python3 -m pip install ffpyplayer

# Run the app
# python3 main.py

# --------------------------------------------------------------- #

# sudo apt-get remove python3-kivy
# sudo pip3 install kivy

# --------------------------------------------------------------- #

class MyApp(App):
    def build(self):
        return Label(text='Hello World', font_size=72)


if __name__ == '__main__':

    os.environ['DISPLAY']=':0.0'
    print('echo $DISPLAY')
    print()

    MyApp().run()
