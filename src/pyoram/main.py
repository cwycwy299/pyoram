import data

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from pyoram.ui import SignupScreen, LoginScreen, MainScreen
from pyoram import utils
from pyoram.crypto.keyfile import KeyFile

from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '300')

# Create the screen manager
sm = ScreenManager()
# first added screen is shown
sm.add_widget(SignupScreen(name='signup'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(MainScreen(name='main'))


class PyORAMApp(App):

    def build(self):
        if self.has_signed_up():
            sm.current = 'login'
        return sm

    def has_signed_up(self):
        return data.file_exists(utils.KEY_MAP_FILE_NAME) & KeyFile.verify_content()


if __name__ == '__main__':
    PyORAMApp().run()
