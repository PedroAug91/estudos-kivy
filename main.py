from kivymd.app import MDApp
from kivy.lang import Builder

class Apps(MDApp):
    def build(self):
        return Builder.load_file("telamd.kv")

    
if __name__ == '__main__':
    Apps().run()

