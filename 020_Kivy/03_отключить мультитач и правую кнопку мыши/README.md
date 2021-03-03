from kivy.config import Config
# убрать круги при нажатии правой и центральной кнопки мыши (мультитач)
    # https://kivy.org/doc/stable/api-kivy.input.providers.mouse.html
    Config.set('input', 'mouse', 'mouse,multitouch_on_demand')