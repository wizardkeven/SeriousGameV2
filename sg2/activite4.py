from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.graphics import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.layout import Layout
from kivy.uix.popup import Popup
from kivy.uix.video import Video
from kivy.uix.widget import Widget
import random
import time
import cProfile
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.uix.popup import Popup

import dataBase
import menu

class Bonhomme(Widget):
	pass
class Porte1(Widget):
	
    #Classe correspondant a la porte de "face". sa categorie est Porte1.
	#Tous les sons generes sur les deux oreille seront de categorie Porte1.

    category='Porte1'

 
    def on_touch_down(self, touch):
        """Function called when the object is double clicked
        
        :param touch: finger on the screen     
        
        """
        #Get the object touched by the user    
        if self.collide_point(*touch.pos): 
            #Set opacity to display the current selected object
            self.opacity = 0.2
            touch.grab(self)
            return True

    def on_touch_up(self, touch):

        #If this is the correct object
        if touch.grab_current is self:    
            #The Object is ungrabbed
            touch.ungrab(self)  
            #The initial opacity is set                
            self.opacity = 1
			#On verifie si les categories son et porte touchees sont les memes
            if (self.category==self.parent.category):
				print("Congratulations !")
				sound = SoundLoader.load('../sound/right.wav')
				sound.play()
				#Update of score
				self.parent.score += 5
				#On sauvegarde le score et le temps pour les bases de donnees
				val = self.parent.score
				tem = self.parent.clock
				#Lancement de la fenetre
				self.parent.on_winning()
                            
				#Saving in dataBase
				self.parent.local_db.insert_into_Table("activite4",
												["time Date", "score int","time", "source string", "destination string", "result string" ],
												[time.strftime("%a %d %b %Y %H:%M:%S", time.gmtime()),
												str(val),
												str(tem),
												self.category,
												Activite4.category,
												"Success"
												]
										)
		
            #Si les categories sont differentes, on lance un son "mauvais" et on enregistre dans la base de donnees            
            else:
				print("This is the wrong category")
				sound = SoundLoader.load('../sound/wrong.wav');
				sound.play();
				#Update of score
				self.parent.score -= 1
				#The object is moved back to the initial position
				val = self.parent.score
				tem = self.parent.clock
				#SAving in dataBase
				self.parent.local_db.insert_into_Table("activite4",
												["time Date", "score integer", "time", "source string", "destination string", "result string" ],
												[time.strftime("%a %d %b %Y %H:%M:%S", time.gmtime()),
												str(val),
												str(tem),
												self.category,
												Activite4.category,
												"Fail"
												]
											)
										
		
class Porte2(Widget):
	
    #Classe correspondant a la porte de "droite". sa categorie est Porte2.
	#Tous les sons generes sur l'oreille droite seront de categorie Porte2.

    category='Porte2'

 
    def on_touch_down(self, touch):
        """Function called when the object is double clicked
        
        :param touch: finger on the screen     
        
        """
        #Get the object touched by the user    
        if self.collide_point(*touch.pos): 
            #Set opacity to display the current selected object
            self.opacity = 0.2
            print(self.name)
            #The object is grabbed
            touch.grab(self)
            return True

    def on_touch_up(self, touch):

        #If this is the correct object
        if touch.grab_current is self:    
            #The Object is ungrabbed
            touch.ungrab(self)  
            #The initial opacity is set                
            self.opacity = 1
			#On verifie si les categories son et porte touchees sont les memes
            if (self.category==self.parent.category):
				print("Congratulations !")
				sound = SoundLoader.load('../sound/right.wav')
				sound.play()
				#Update of score
				self.parent.score += 5
				#On sauvegarde le score et le temps pour les bases de donnees
				val = self.parent.score
				tem = self.parent.clock
				#Lancement de la fenetre
				self.parent.on_winning()
                            
				#Saving in dataBase
				self.parent.local_db.insert_into_Table("activite4",
												["time Date", "score int", "time", "source string", "destination string", "result string" ],
												[time.strftime("%a %d %b %Y %H:%M:%S", time.gmtime()),
												str(val),
												str(tem),
												self.category,
												Activite4.category,
												"Success"
												]
										)
		
            #Si les categories sont differentes, on lance un son "mauvais" et on enregistre dans la base de donnees             
            else:
				print("This is the wrong category")
				print("My category is", str(self.category))
				print('And the category of this sound is', str(Activite4.category))
				sound = SoundLoader.load('../sound/wrong.wav');
				sound.play();
				#Update of score
				self.parent.score -= 1
				#The object is moved back to the initial position
				val = self.parent.score
				tem = self.parent.clock
				#SAving in dataBase
				self.parent.local_db.insert_into_Table("activite4",
												["time Date", "score integer", "time", "source string", "destination string", "result string" ],
												[time.strftime("%a %d %b %Y %H:%M:%S", time.gmtime()),
												str(val),
												str(tem),
												self.category,
												Activite4.category,
												"Fail"
												]
											)

		
class Porte3(Widget):
	#Classe correspondant a la porte de "gauche". sa categorie est Porte3.
	#Tous les sons generes sur l'oreille gauche seront de categorie Porte3.

    category='Porte3'

 
    def on_touch_down(self, touch):
        """Function called when the object is double clicked
        
        :param touch: finger on the screen     
        
        """
        #Get the object touched by the user    
        if self.collide_point(*touch.pos): 
            #Set opacity to display the current selected object
            self.opacity = 0.2
            print(self.name)
            #The object is grabbed
            touch.grab(self)
            return True

    def on_touch_up(self, touch):

        #If this is the correct object
        if touch.grab_current is self:    
            #The Object is ungrabbed
            touch.ungrab(self)  
            #The initial opacity is set                
            self.opacity = 1
			#On verifie si les categories son et porte touchees sont les memes
            if (self.category==self.parent.category):
				print("Congratulations !")
				sound = SoundLoader.load('../sound/right.wav')
				sound.play()
				#Update of score
				self.parent.score += 5
				#Sauvegarde du score et du temps pour les stocker dans la base de donnees
				val = self.parent.score
				tem = self.parent.clock
				self.parent.on_winning()
                            
				#Saving in dataBase
				self.parent.local_db.insert_into_Table("activite4",
												["time Date", "score int", "source string", "time", "destination string", "result string" ],
												[time.strftime("%a %d %b %Y %H:%M:%S", time.gmtime()),
												str(val),
												str(tem),
												self.category,
												Activite4.category,
												"Success"
												]
										)
				
			#Si les categories sont differentes, on lance un son "mauvais" et on enregistre dans la base de donnees 
            else:
				print("This is the wrong category")
				sound = SoundLoader.load('../sound/wrong.wav');
				sound.play();
				#Update of score
				self.parent.score -= 1
				#The object is moved back to the initial position
				val = self.parent.score
				tem = self.parent.clock
				#SAving in dataBase
				self.parent.local_db.insert_into_Table("activite4",
												["time Date", "score integer", "source string", "time", "destination string", "result string" ],
												[time.strftime("%a %d %b %Y %H:%M:%S", time.gmtime()),
												str(val),
												str(tem),
												self.category,
												Activite4.category,
												"Fail"
												]
											)
									
class Casque(Widget):
	
#Classe correspondant a l'image "haut parleur" en haut a droite de la fenetre
#A chaque fois que l'enfant cliquera dessus, le son courant se lancera de nouveau.	
    def on_touch_down(self, touch):
        
        if self.collide_point(*touch.pos):
            sound = SoundLoader.load(self.parent.sound)
            sound.play()
            self.opacity = 0.2 
            touch.grab(self) 
            return True

    def on_touch_up(self, touch):
        
        if touch.grab_current is self:  
            self.opacity = 1		
            touch.ungrab(self) 
            return True 
        
class Activite4(Widget):

	
    #Open a dataBase connexion
	local_db = dataBase.DataBase()  
	table_name = "activite4"
	table_attributes = ["time Date", "score integer", "source string", "destination string", "result string" ]
	local_db.create_Table(table_name,table_attributes)
    #Save window's size to use later
	windowSave = Window.size;
    

    
    #Creation d'une liste de sons ou seront stockees tous les sons avec leurs categories respectives
	SoundList =[]
	score = NumericProperty(0)
	clock = NumericProperty(0)
	porte1 = ObjectProperty(None)
	porte2 = ObjectProperty(None)
	porte3 = ObjectProperty(None)
	sound = SoundLoader
	category = ''
 

	def sound_init(self):
	#Dans cette methode on remplit notre liste de sons en parcourant le fichier ou se trouvent tous les noms des sons avec leurs categories
	#Cete methode est appelee dans la methode new_round
        # Opening file reading mode
		loaded_file = open("./activite4.txt", "r")     
        #read the first line
		line = loaded_file.readline()
      
		while (line!="endfile"):
			if (line[0]!='#'):
				tab_res = line.split('&')
				tab_save = tab_res[1].split('/')
				tab_name = tab_save[2].split('.')
				if (tab_res[0]=="Sound"):
					sound = tab_res[1]
                    #updating form's list
					self.SoundList.append(sound)
            #read the next line
			line = loaded_file.readline()
			

  
    
	def new_round(self):  
	#Cette fonction est appelee quand le joueur gagne une partie et souhaite rejouer.
		#On choisit un nombre aleatoiret afin de tirer un nouveau son de la liste.
		self.sound_init()
		size_list_sound= len(self.SoundList)
		rand_sound = random.randint(0, size_list_sound-1)
		loaded_file = open("./activite4.txt", "r")     
        #read the first line
		line = loaded_file.readline()
		self.sound = self.SoundList[rand_sound]
		#On met a jour la categorie de la classe courante = categorie du nouveau son tire
		while (line!="endfile"):
			if (line[0]!='#'):
				tab_res = line.split('&')
				tab_save = tab_res[1].split('/')
				tab_name = tab_save[2].split('.')
				if (tab_res[0]=="Sound"):
					if(tab_res[1]==self.sound):
						Activite4.category =tab_res[2]
						print('est', str(self.category))
			#read the next line
			line = loaded_file.readline()
			

		
		print('la categorie du son', str(self.sound))
		print('est', str(self.category))
		return self.sound

            
	def increment_clock(self, dt):
			self.clock += 1;
	

        
    
	def update(self, dt):
		if (Window.size != self.windowSave):
			self.windowSave = Window.size;
			self.updateWidget();
			return False;
	
	def on_winning(self):
	#Methode mettant en place une fenetre avec differents boutons:	
		layout = BoxLayout(orientation='vertical')
		def callback(instance):
			#Si l'utilisateur clique sur rejouer, on remet le score et la date a 0, on refait appel a new_round et on lance le nouveau son
			if (instance.text=='REJOUER'):
				sound1.stop()
				self.new_round();
				popup.dismiss();
				self.score = 0
				self.clock = 0
				sound = SoundLoader.load(self.sound)
				sound.play()
			#Si l'utilisateur clique sur Menu on lance le Menu
			if(instance.text == 'MENU'):
				sound1.stop()
				popup.dismiss();
				return menu.MenuApp().run()
			#Si l'utilisateur clique sur "quitter" on stoppe l'application
			if(instance.text=='QUITTER LE JEU'):
				sound1.stop()
				popup.dismiss();
				Activite1_difficultApp().stop(); 
				
			print('The button <%s> is being pressed' % instance.text)
		#Creation du boutton 1 "rejouer" 
		btn1 = Button(text='REJOUER') 
		btn1.bind(on_press=callback)
		#Creation du boutton 2 Menu
		btn2 = Button(text='MENU') 
		btn2.bind(on_press=callback)
		
		#Creation du boutton 3 Quitter Le jeu
		btn3 = Button(text='QUITTER LE JEU')
		btn3.bind(on_press=callback)
		layout.add_widget(btn1)
		layout.add_widget(btn2)
		layout.add_widget(btn3)
		popup = Popup(title='Felicitations ! \nScore : ' + str(self.score) + '\nTemps: ' + str(self.clock) + ' secondes',
						title_size = '20sp' ,
						title_color = [0.5,1,1,1],
						title_font = 'Red',
						content=layout,
						size_hint=(None, None),
						size=(400, 400),
						auto_dismiss=False)
		popup.open()
		sound1 = SoundLoader.load('../sound/finished.wav')
		sound1.play()
    #Methode appelee dans le .kv:
	#Si l'utilisateur clique sur le bouton Aide en haut a gauche de la fenetre de jeu, une fenetre expliquant le fonctionnement du jeu apparaitra
	#boutton cree dans le .kv
	def aide(self):
		l = BoxLayout(orientation='vertical')				
	
		popup = Popup(title='Aide',
						content=Label(text='Laisse toi guider par le son pour trouver \nla bonne porte. Si le son vient de la droite,\n clique sur la porte de droite, si le son\n vient de la gauche, clique sur la partie gauche, sinon,\n clique sur la porte en face ! .'),
						size_hint=(None, None),
						size=(400, 200),
						)
		popup.open();
	
	#Methode appelee dans le .kv:
	#Si l'utilisateur clique sur le bouton Menu en haut a gauche de la fenetre de jeu, il sera redirige vers le Menu
	#Boutton cree dans le .kv
	def menu(self):
		return menu.MenuApp().run();
		
	#Methode appellee dans le .kv:
	#Si l'utilisateur clique le boutton Quitter en haut a gauche de la fenetre de jeu, l'application s'arretera
	#Boutton cree dans le .kv
	def stop(self):
		return Activite1_difficultApp().stop();

    
class Activite4App(App):

	
    #Classe representant notre application
    def build(self):
		

        #Start the game
		game = Activite4()
		son = game.new_round()
		Clock.schedule_interval(game.update, 1.0 / 60.0)
		Clock.schedule_interval(game.increment_clock, 1.0)
		sound = SoundLoader.load(son)
		sound.play()
		return game

if __name__ == '__main__':
	Activite4App().run()