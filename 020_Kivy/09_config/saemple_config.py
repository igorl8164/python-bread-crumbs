if __name__ == '__main__':
    
    from kivy.config import Config
    Config.set('graphics', 'width', '480')
    Config.set('graphics', 'height', '800')
    Config.set('graphics', 'show_cursor', 1)
    Config.set('graphics', 'resizable', 0)
    #Config.write()

    # во весь экран без рамки окна
    # https://kivy.org/doc/stable/api-kivy.config.html
    #from kivy.config import Config
    Config.set('graphics', 'allow_screensaver', 0)
    Config.set('graphics', 'fullscreen', 'auto')
    Config.set('graphics', 'borderless', 1)
    # Config.write()

    # Dynamically after the Window was created:
    # from kivy.core.window import Window
    # Window.size = (300, 100)

    # https://kivy.org/doc/stable/api-kivy.input.providers.hidinput.html
    # https://kivy.org/doc/stable/api-kivy.input.providers.mtdev.html
    # отключить мультитач и красные круги от правой и центральной кнопок мыши
    # https://kivy.org/doc/stable/api-kivy.input.providers.mouse.html
    #Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
    Config.set('modules', 'touchring', 'show_cursor=true')
    Config.set('modules', 'cursor', '1')
    # Config.set('input', 'mouse', 'probesysfs,provider=hidinput')
    # Config.set('input', 'mouse', 'mouse,disable_multitouch')
    # Config.set('input', 'mtdev', 'probesysfs,provider=hidinput')

    Config.write()
    
