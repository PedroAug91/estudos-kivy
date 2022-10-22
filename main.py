from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager

global screen
screen = ScreenManager()

class AboutScreen(Screen):
    pass

class SplashScreen(Screen):
    pass


class InitialScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


screen.add_widget(SplashScreen(name='splash'))
screen.add_widget(InitialScreen(name='initial'))
screen.add_widget(LoginScreen(name='login'))
screen.add_widget(SplashScreen(name='about'))


class Apps(MDApp):
    def build(self):
        return Builder.load_file("tela.kv")

    
if __name__ == '__main__':
    Apps().run()

