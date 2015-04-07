from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
import time
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import activite1_easy
import activite1_medium
import activite1_difficult
import activite4
import game2
import game3

class Object(Widget):
    """Class which represent the object on the screen
   
    """   
    
    def on_touch_move(self, touch):
        """Function called when the object is moved
        :param touch: finger on the screen     
        """
        if touch.grab_current is self: 
            self.center_x = touch.x 
            self.center_y = touch.y 

    
    def on_touch_down(self, touch):
        """Function called when the object is pressed
        :param touch: finger on the screen     
        """
        if self.collide_point(*touch.pos):
            if touch.is_double_tap: 
                sound = SoundLoader.load(self.text)
                sound.play()
                return;
            self.opacity = 0.2 
            touch.grab(self) 
            return True

    def on_touch_up(self, touch):
        """Function called when the object is released
        :param touch: finger on the screen     
        """
        if touch.grab_current is self:  
            self.center_x = touch.x
            self.center_y = touch.y
            self.opacity = 1 
            touch.ungrab(self)
            return True

    

class Menu(Widget):
	def version1(self):
		l = BoxLayout(orientation='vertical')
		def callback(instance):
			if (instance.text=='Jeu 1'):
				popup.dismiss();
				game2.Game2App().run()
			if(instance.text =='Jeu 2'):
				popup.dismiss();
				game3.Game3App().run()
				
			print('The button <%s> is being pressed' % instance.text)
		b1 = Button(text='Jeu 1', size_hint=(1, 0.1), background_color=(0.25,0.25,0.25,0.25))
		b1.bind(on_press=callback)
		b2 =  Button(text='Jeu 2', size_hint=(1, 0.1), background_color=(0.25,0.25,0.25,0.25))
		b2.bind(on_press=callback)
		l.add_widget(b1)
		l.add_widget(b2)
		popup = Popup(title='A quel jeu veux-tu jouer ?',
						content=l,
						size_hint=(None, None),
						size=(300, 300),
						auto_dismiss=False
						)
		#button.bind(on_press=popup.dismiss)
		popup.open();

	def version2(self):
		l = BoxLayout(orientation='vertical')
		def callback(instance):
			if (instance.text=='Jeu 1'):
				popup.dismiss();
				self.jeu1()
			if(instance.text =='Jeu 2'):
				popup.dismiss();
			if(instance.text=='Jeu 3'):
				popup.dismiss();
				return activite4.Activite4App().run()
				
			print('The button <%s> is being pressed' % instance.text)
		b1 = Button(text='Jeu 1', size_hint=(1, 0.1), background_color=(0.25,0.25,0.25,0.25))
		b1.bind(on_press=callback)
		b2 =  Button(text='Jeu 2', size_hint=(1, 0.1), background_color=(0.25,0.25,0.25,0.25))
		b2.bind(on_press=callback)
		b3 =  Button(text='Jeu 3', size_hint=(1, 0.1), background_color=(0.25,0.25,0.25,0.25))
		b3.bind(on_press=callback)
		l.add_widget(b1)
		l.add_widget(b2)
		l.add_widget(b3)
		popup = Popup(title='A quel jeu veux-tu jouer ?',
						content=l,
						size_hint=(None, None),
						size=(300, 300),
						auto_dismiss=False
						)
		#button.bind(on_press=popup.dismiss)
		popup.open();
    
	def jeu1(self):
		l = BoxLayout(orientation='vertical')
		def callback(instance):
			if (instance.text=='Facile'):
				popup.dismiss();
				return activite1_easy.Activite1_easyApp().run()
			if(instance.text =='Moyen'):
				popup.dismiss();
				return activite1_medium.Activite1_mediumApp().run()
			if(instance.text=='Difficile'):
				popup.dismiss();
				return activite1_difficult.Activite1_difficultApp().run()
				
			print('The button <%s> is being pressed' % instance.text)
		b1 = Button(text='Facile', size_hint=(1, 0.1), background_color=(0.25,0.25,0.25,0.25))
		b1.bind(on_press=callback)
		b2 =  Button(text='Moyen', size_hint=(1, 0.1), background_color=(0.25,0.25,0.25,0.25))
		b2.bind(on_press=callback)
		b3 =  Button(text='Difficile', size_hint=(1, 0.1), background_color=(0.25,0.25,0.25,0.25))
		b3.bind(on_press=callback)
		l.add_widget(b1)
		l.add_widget(b2)
		l.add_widget(b3)
		popup = Popup(title='Choisis le niveau de jeu !',
						content=l,
						size_hint=(None, None),
						size=(300, 300),
						auto_dismiss=False
						)
		#button.bind(on_press=popup.dismiss)
		popup.open();
	
	def update(self, dt):
		pass
    
    
	def on_winning(self, touch):
		pass
		
	def aide(self):
		l = BoxLayout(orientation='vertical')					
		b = Button(text='Quitter', size_hint=(0.5, 0.1))		
		l.add_widget(b)
	
		popup = Popup(title='Aide',
						content=Label(text='Pour jouer aux jeux de la version 1 \nclique sur "version 1". Pour jouer aux jeux \nde la version 2 clique sur "version 2"'),
						size_hint=(None, None),
						size=(400, 200),
						)
		b.bind(on_press=popup.dismiss)
		popup.open();	
		
	


class MenuApp(App):
    """Class to launch the game 1
    """   
    def build(self):
		"""Function which constructs the game
		"""
		game = Menu()
		Clock.schedule_interval(game.update, 1.0 / 60.0)
		#sound = SoundLoader.load('../sound/menu.wav')
		#sound.play()
		return game

if __name__ == '__main__':
    MenuApp().run()