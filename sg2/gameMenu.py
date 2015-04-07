import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
import time
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

#from game2 import Game2App
#from game3 import Game3App
import activite1_easy
import activite1_difficult
import activite1_medium


kivy.require('1.8.0') 

class Object(Widget):
	
	
    def on_touch_down(self, touch):
        
        if self.collide_point(*touch.pos):
			self.opacity = 0.2 
			touch.grab(self) 
			return True

    def on_touch_up(self, touch):
        
        if touch.grab_current is self: 
            self.opacity = 1		
            touch.ungrab(self) 
            return True

class GameMenu(BoxLayout):
    """Class to represent the menu
    """   
    def update(self, dt):
        pass
    
    def launchGame1(self):
        """Function which launch the first game
        """
        return activite1_easy.Activite1_easyApp().run();
    
    def launchGame2(self):
		"""Function which launch the second game"""
		return activite1_difficult.Activite1_difficultApp().run();
		
    def launchGame3(self):
		return activite1_medium.Activite1_mediumApp().run();
    
class GameMenuApp(App):
    """Class to launch the menu
    """   
    def build(self):
		Config.set('graphics', 'width', 800)
		Config.set('graphics', 'height', 600)
		Clock.schedule_interval(GameMenu.update(), 1.0 / 60.0)
		return GameMenu();

if __name__ == '__main__':
	GameMenuApp().run()