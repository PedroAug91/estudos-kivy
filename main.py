from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

Window.size = (350, 600)


global screen
screen = ScreenManager()

class AboutScreen(Screen):
    pass


class InitialScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


screen.add_widget(InitialScreen(name='initial'))
screen.add_widget(LoginScreen(name='login'))
screen.add_widget(AboutScreen(name='about'))

class Apps(MDApp):
    def build(self):
        return Builder.load_file("main.kv")
    
if __name__ == '__main__':
    Apps().run()
