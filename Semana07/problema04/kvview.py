from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file('whats.kv')

class KvView(App):
    
    def build(self):
        return GUI

KvView().run()
