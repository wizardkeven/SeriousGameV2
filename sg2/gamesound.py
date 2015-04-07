from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
import time


class Object(Widget):

    def on_touch_down(self, touch):
        """Function called when the object is pressed
        :param touch: finger on the screen     
        """
        if self.collide_point(*touch.pos):
            sound = SoundLoader.load(self.text)
            sound.play()
            self.opacity = 0.2 
            touch.grab(self) 
            return True

    def on_touch_up(self, touch):
        """Function called when the object is released
        :param touch: finger on the screen     
        """
        if touch.grab_current is self:  
            #self.center_x = touch.x
            #self.center_y = touch.y
            self.opacity = 1 
            touch.ungrab(self) 
            return True

    

class Gamesound(Widget):
    """Class to manage the game itself
   
    """       
    def update(self, dt):
        """Game loop
        :param dt: time between two calls
        """
        pass
    
    
    def on_winning(self, touch):
        pass


class GamesoundApp(App):
    """Class to launch the game 1
    """   
    
    def build(self):
        """Function which constructs the game
        """
        game = Gamesound()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        sound = SoundLoader.load('../sound/finished.wav')
        sound.play()
        return game

if __name__ == '__main__':
    GamesoundApp().run()