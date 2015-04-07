from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
import random
from kivy.vector import Vector
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
import activite1_easy
import activite1_medium
import menu
import dataBase

class Picture1(Widget):
	#classe representant une des 4 photos qui defilent. sa categorie est Picture1
	category = 'Picture1'
	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)
	velocity = ReferenceListProperty(velocity_x, velocity_y)
	
	def on_touch_down(self, touch):
        
		if self.collide_point(*touch.pos):
			#Si on clique sur l'image son opacite est de 0.2
			self.opacity = 0.2 
			touch.grab(self) 
			return True
	def on_touch_up(self, touch):

        #If this is the correct object
		if touch.grab_current is self:    
            #The Object is ungrabbed
			touch.ungrab(self)  
            #L'opacite initiale est remise              
			self.opacity = 1
			print('la categorie du son est', str(self.parent.category))
			print('Tu touches l image de categorie ', str(self.category))
			#Si la categorie du son ecoute est egale a la categorie de cette photo:
			if (self.category==self.parent.category):
				print("Congratulations !")
				sound = SoundLoader.load('../sound/right.wav')
				sound.play()
				#Update of score
				self.parent.score += 5
				#On enregistre les valeurs des scores et temps pour les stocker dans la bases de donnees
				val = self.parent.score
				tem = self.parent.clock
				#On ouvre la fenetre
				self.parent.on_winning()
                            
				#Saving in dataBase
				self.parent.local_db.insert_into_Table("activite1_difficult",
												["time Date", "score int", "time", "source string", "destination string", "result string" ],
												[time.strftime("%a %d %b %Y %H:%M:%S", time.gmtime()),
												str(val),
												str(tem),
												self.category,
												Activite1_difficult.category,
												"Success"
												]
										)
		
            #Si les deux categories sont differentes, le score est decremente d'un point, et on enregistre les valeurs dans la base de donnees           
			else:
				print("This is the wrong category")
				sound = SoundLoader.load('../sound/wrong.wav');
				sound.play();
				#Update of score
				self.parent.score -= 1
				val = self.parent.score
				tem = self.parent.clock
				#SAving in dataBase
				self.parent.local_db.insert_into_Table("activite1_difficult",
												["time Date", "score integer", "time", "source string", "destination string", "result string" ],
												[time.strftime("%a %d %b %Y %H:%M:%S", time.gmtime()),
												str(val),
												str(tem),
												self.category,
												Activite1_difficult.category,
												"Fail"
												]
											)

	#Methode permettant a l'image de bouger		
	def move(self):
		self.pos = Vector(*self.velocity)*1 + self.pos
		
class Picture2(Widget):
	#classe representant une des 4 photos qui defilent. sa categorie est Picture2
	category = 'Picture2'
	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)
	velocity = ReferenceListProperty(velocity_x, velocity_y)
	
	def on_touch_down(self, touch):
        
		if self.collide_point(*touch.pos):
			#Si on clique sur l'image son opacite est de 0.2
			self.opacity = 0.2 
			touch.grab(self) 
			return True
	def on_touch_up(self, touch):

        #If this is the correct object
		if touch.grab_current is self:    
            #The Object is ungrabbed
			touch.ungrab(self)  
            #On remet l'opacite a 1                
			self.opacity = 1
			print('la categorie du son est', str(self.parent.category))
			print('Tu touches l image de categorie ', str(self.category))
			#Si la categorie du son ecoute est egale a la categorie de cette photo:
			if (self.category==self.parent.category):
				print("Congratulations !")
				sound = SoundLoader.load('../sound/right.wav')
				sound.play()
				#Update of score
				self.parent.score += 5
				#On enregistre les valeurs des scores et temps pour les stocker dans la bases de donnees
				val = self.parent.score
				tem = self.parent.clock
				#On ouvre la fenetre
				self.parent.on_winning()
                            
				#Saving in dataBase
				self.parent.local_db.insert_into_Table("activite1_difficult",
												["time Date", "score int", "time", "source string", "destination string", "result string" ],
												[time.strftime("%a %d %b %Y %H:%M:%S", time.gmtime()),
												str(val),
												str(tem),
												self.category,
												Activite1_difficult.category,
												"Success"
												]
										)
		
            #Si les deux categories sont differentes, le score est decremente d'un point, et on enregistre les valeurs dans la base de donnees           
			else:
				print("This is the wrong category")
				sound = SoundLoader.load('../sound/wrong.wav');
				sound.play();
				#Update of score
				self.parent.score -= 1
				val = self.parent.score
				tem = self.parent.clock
				#SAving in dataBase
				self.parent.local_db.insert_into_Table("activite1_difficult",
												["time Date", "score integer", "time", "source string", "destination string", "result string" ],
												[time.strftime("%a %d %b %Y %H:%M:%S", time.gmtime()),
												str(val),
												str(tem),
												self.category,
												Activite1_difficult.category,
												"Fail"
												]
											)

	#Methode permettant a l'image de bouger		
	def move(self):
		self.pos = Vector(*self.velocity)*1 + self.pos
	
class Picture3(Widget):
	#classe representant une des 4 photos qui defilent. sa categorie est Picture3
	category = 'Picture3'
	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)
	velocity = ReferenceListProperty(velocity_x, velocity_y)
	
	def on_touch_down(self, touch):
        
		if self.collide_point(*touch.pos):
			#Si on clique sur l'image son opacite est de 0.2
			self.opacity = 0.2 
			touch.grab(self) 
			return True
	def on_touch_up(self, touch):

        #If this is the correct object
		if touch.grab_current is self:    
            #The Object is ungrabbed
			touch.ungrab(self)  
            #On remet l'opacite a 1                
			self.opacity = 1
			print('la categorie du son est', str(self.parent.category))
			print('Tu touches l image de categorie ', str(self.category))
			#Si la categorie du son ecoute est egale a la categorie de cette photo:
			if (self.category==self.parent.category):
				print("Congratulations !")
				sound = SoundLoader.load('../sound/right.wav')
				sound.play()
				#Update of score
				self.parent.score += 5
				#On enregistre les valeurs des scores et temps pour les stocker dans la bases de donnees
				val = self.parent.score
				tem = self.parent.clock
				#On ouvre la fenetre
				self.parent.on_winning()
                            
				#Saving in dataBase
				self.parent.local_db.insert_into_Table("activite1_difficult",
												["time Date", "score int", "time", "source string", "destination string", "result string" ],
												[time.strftime("%a %d %b %Y %H:%M:%S", time.gmtime()),
												str(val),
												str(tem),
												self.category,
												Activite1_difficult.category,
												"Success"
												]
										)
		
            #Si les deux categories sont differentes, le score est decremente d'un point, et on enregistre les valeurs dans la base de donnees           
			else:
				print("This is the wrong category")
				sound = SoundLoader.load('../sound/wrong.wav');
				sound.play();
				#Update of score
				self.parent.score -= 1
				val = self.parent.score
				tem = self.parent.clock
				#SAving in dataBase
				self.parent.local_db.insert_into_Table("activite1_difficult",
												["time Date", "score integer", "time", "source string", "destination string", "result string" ],
												[time.strftime("%a %d %b %Y %H:%M:%S", time.gmtime()),
												str(val),
												str(tem),
												self.category,
												Activite1_difficult.category,
												"Fail"
												]
											)

	#Methode permettant a l'image de bouger		
	def move(self):
		self.pos = Vector(*self.velocity)*1 + self.pos
		
class Picture4(Widget):
	#classe representant une des 4 photos qui defilent. sa categorie est Picture4
	category = 'Picture4'
	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)
	velocity = ReferenceListProperty(velocity_x, velocity_y)
	
	def on_touch_down(self, touch):
        
		if self.collide_point(*touch.pos):
			#Si on clique sur l'image son opacite est de 0.2
			self.opacity = 0.2 
			touch.grab(self) 
			return True
	def on_touch_up(self, touch):

        #If this is the correct object
		if touch.grab_current is self:    
            #The Object is ungrabbed
			touch.ungrab(self)  
            #On remet l'opacite a 1                
			self.opacity = 1
			print('la categorie du son est', str(self.parent.category))
			print('Tu touches l image de categorie ', str(self.category))
			#Si la categorie du son ecoute est egale a la categorie de cette photo:
			if (self.category==self.parent.category):
				print("Congratulations !")
				sound = SoundLoader.load('../sound/right.wav')
				sound.play()
				#Update of score
				self.parent.score += 5
				#On enregistre les valeurs des scores et temps pour les stocker dans la bases de donnees
				val = self.parent.score
				tem = self.parent.clock
				#On ouvre la fenetre
				self.parent.on_winning()
                            
				#Saving in dataBase
				self.parent.local_db.insert_into_Table("activite1_difficult",
												["time Date", "score int", "time", "source string", "destination string", "result string" ],
												[time.strftime("%a %d %b %Y %H:%M:%S", time.gmtime()),
												str(val),
												str(tem),
												self.category,
												Activite1_difficult.category,
												"Success"
												]
										)
		
            #Si les deux categories sont differentes, le score est decremente d'un point, et on enregistre les valeurs dans la base de donnees           
			else:
				print("This is the wrong category")
				sound = SoundLoader.load('../sound/wrong.wav');
				sound.play();
				#Update of score
				self.parent.score -= 1
				val = self.parent.score
				tem = self.parent.clock
				#SAving in dataBase
				self.parent.local_db.insert_into_Table("activite1_difficult",
												["time Date", "score integer", "time", "source string", "destination string", "result string" ],
												[time.strftime("%a %d %b %Y %H:%M:%S", time.gmtime()),
												str(val),
												str(tem),
												self.category,
												Activite1_difficult.category,
												"Fail"
												]
											)

	#Methode permettant a l'image de bouger		
	def move(self):
		self.pos = Vector(*self.velocity)*1 + self.pos
		
class Casque(Widget):
	
	#Classe representant l'image "Haut parleur" en haut a droite de la fenetre de jeu
    def on_touch_down(self, touch):
        
        if self.collide_point(*touch.pos):
		#Si l'utilisateur clique dessus, le son courant est joue a nouveau
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

    

class Activite1_difficult(Widget):
         
	#Open a dataBase connexion
	local_db = dataBase.DataBase()  
	table_name = "activite1_difficult"
	table_attributes = ["time Date", "score integer", "source string", "destination string", "result string" ]
	local_db.create_Table(table_name,table_attributes)
    #Save window's size to use later
	windowSave = Window.size;
	#Creation d'une liste de sons
	SoundList =[]
	score = NumericProperty(0)
	clock = NumericProperty(0)
	sound = ''
	category = ''
	picture1 = ObjectProperty(None)
	picture2 = ObjectProperty(None)
	picture3 = ObjectProperty(None)
	picture4 = ObjectProperty(None)

 
    
	def sound_init(self):
	#Cette methode parse le fichier .txt ou se trouve tous les sons et les place dans la liste de sons
	#Elle est appelee dans la methode suivante
        # Opening file reading mode
		loaded_file = open("./activite1_difficult.txt", "r")     
        #read the first line
		line = loaded_file.readline()
        
        #Loading all the file in 2 different lists
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
		#Cette methode appele sound_init et prend un son aleatoirement parmi la liste de son
		self.sound_init()
		size_list_sound= len(self.SoundList)
		rand_sound = random.randint(0, size_list_sound-1)
		loaded_file = open("./activite1_difficult.txt", "r")     
        #read the first line
		line = loaded_file.readline()
		self.sound = self.SoundList[rand_sound]
		#On recupere la categorie du son pioche precedemment
		while (line!="endfile"):
			if (line[0]!='#'):
				tab_res = line.split('&')
				tab_save = tab_res[1].split('/')
				tab_name = tab_save[2].split('.')
				if (tab_res[0]=="Sound"):
					if(tab_res[1]==self.sound):
						Activite1_difficult.category =tab_res[2]
			#read the next line
			line = loaded_file.readline()
			

		
		print('le son qui passe cest', str(self.sound))
		print('Sa categorie est ', str(self.category))
		return self.sound

	
	
	def increment_clock(self, dt):
		self.clock += 1;
		
	#Methode permettant d'initialiser un vecteur de mouvement pour les 4 images.
	#On veut les faire defiler de gauche a droite, donc le vecteur est (1,0)
	def serve(self):
		self.picture1.center = self.center
		self.picture1.velocity = Vector(1, 0)
		
		self.picture2.center = self.center
		self.picture2.velocity = Vector(1, 0)

		self.picture3.center = self.center
		self.picture3.velocity = Vector(1, 0)
		self.picture4.center = self.center
		self.picture4.velocity = Vector(1, 0)		
		
	
	def update(self, dt):
	
		self.picture1.move()
		self.picture2.move()
		self.picture3.move()
		self.picture4.move()
		#Si une image sort de la fenetre elle reapparait de l'autre cote
		if (self.picture1.y < 0):
			self.picture1.y = self.height
		if (self.picture1.y > self.height):
			self.picture1.y =  0
		if (self.picture1.x < 0):
			self.picture1.x = self.width
		if (self.picture1.x > self.width):
			self.picture1.x =  0		
		if (self.picture2.y < 0):
			self.picture2.y = self.height
		if (self.picture2.y > self.height):
			self.picture2.y =  0
		if (self.picture2.x < 0):
			self.picture2.x = self.width
		if (self.picture2.x > self.width):
			self.picture2.x =  0
		
		if (self.picture3.y < 0):
			self.picture3.y = self.height
		if (self.picture3.y > self.height):
			self.picture3.y =  0
		if (self.picture3.x < 0):
			self.picture3.x = self.width
		if (self.picture3.x > self.width):
			self.picture3.x =  0
		if (self.picture4.y < 0):
			self.picture4.y = self.height
		if (self.picture4.y > self.height):
			self.picture4.y =  0
		if (self.picture4.x < 0):
			self.picture4.x = self.width
		if (self.picture4.x > self.width):
			self.picture4.x =  0

	
	def niveaux(self):
	#Cette methode est appelee par on_winning. Il s'agit de la fenetre proposant les differents niveaux de jeu
		l = BoxLayout(orientation='vertical')
		def callback(instance):
			#Si l'utilisateur clique sur "Facile" on ferme la fenetre et retourne le jeu 1 facile
			if (instance.text=='Facile'):
				popup.dismiss();
				activite1_easy.Activite1_easyApp().run();
			#Si l'utilisateur clique sur "Moyen" on ferme la fenetre et on retourne le jeu moyen
			if(instance.text =='Moyen'):
				popup.dismiss();
				activite1_medium.Activite1_mediumApp().run();
			#Si l'utilisateur clique sur "Difficile" on ferme la fenetre, on fait appele a la methode new_round pour choisir un nouveau son 
			#On remet le score et le chrono a zero et on lance le son choisit
			if(instance.text=='Difficile'):
				popup.dismiss();
				self.new_round()
				self.score = 0
				self.clock = 0
				sound = SoundLoader.load(self.sound)
				sound.play()
				
			print('The button <%s> is being pressed' % instance.text)
		#Creation des differents bouttons 
		b1 = Button(text='Facile', size_hint=(1, 0.1))
		b1.bind(on_press=callback)
		b2 =  Button(text='Moyen', size_hint=(1, 0.1))
		b2.bind(on_press=callback)
		b3 =  Button(text='Difficile', size_hint=(1, 0.1))
		b3.bind(on_press=callback)
		l.add_widget(b1)
		l.add_widget(b2)
		l.add_widget(b3)
		popup = Popup(title='Choisis le niveau de difficulte ',
						content=l,
						size_hint=(None, None),
						size=(300, 300),
						auto_dismiss=False
						)
		popup.open();
		
		
		
		
	def on_winning(self):
	#Cette methode est appelee lorsque l'utilisateur clique sur la bonne image
	#On lui propose alors plusieurs boutons 	
		layout = BoxLayout(orientation='vertical')
		def callback(instance):
			#S'il clique sur rejouer on ferme la fenetre, on fait un appele a new_round pour repiocher un son, on met a zero score et temps et on lance le son correspondant
			if (instance.text=='REJOUER'):
				sound1.stop()
				popup.dismiss();
				self.new_round()
				self.clock = 0
				self.score = 0
				sound = SoundLoader.load(self.sound)
				sound.play()
			#S'il clique sur 'changer de niveau' il est redirigie vers la methode niveaux()
			if(instance.text =='CHANGER DE NIVEAU'):
				popup.dismiss();
				sound1.stop()
				self.niveaux();	
			#S'il clique sur "menu", il quitte ce jeu et est redirige vers la fenetre du menu principal	
			if(instance.text=='MENU'):
				sound1.stop()
				popup.dismiss()
				menu.MenuApp().run()
			#S'il clique sur "Quitter le jeu", il quitte toute l'application
			if(instance.text== 'QUITTER LE JEU'):
				sound1.stop()
				popup.dismiss();
				self.parent.stop()
			print('The button <%s> is being pressed' % instance.text)
		""" Creation des bouttons:  """
		btn1 = Button(text='REJOUER') 
		btn1.bind(on_press=callback)
		btn2 = Button(text='MENU') 
		btn2.bind(on_press=callback)
		btn3 = Button(text='CHANGER DE NIVEAU') 
		btn3.bind(on_press = callback)
		btn4 = Button(text='QUITTER LE JEU')
		btn4.bind(on_press=callback)
		layout.add_widget(btn1)
		layout.add_widget(btn2)
		layout.add_widget(btn3)
		layout.add_widget(btn4)
		popup = Popup(title='Felicitations ! \nScore : ' + str(self.score) + '\nTemps: ' + str(self.clock) + ' secondes',
						title_size = '20sp' ,
						title_color = [0.5,1,1,1],
						title_font = 'Red',
						content=layout,
						size_hint=(None, None),
						size=(400, 400),
						auto_dismiss=False)
		popup.open()
		print "popup ouvert"
		sound1 = SoundLoader.load('../sound/public.wav')
		sound1.play()
	#Methode appelee dans le .kv:
	#Si l'utilisateur clique sur le bouton Aide en haut a gauche de la fenetre de jeu, une fenetre expliquant le fonctionnement du jeu apparaitra
	#boutton cree dans le .kv	
	def aide(self):
		l = BoxLayout(orientation='vertical')					
		b = Button(text='Quitter', size_hint=(0.5, 0.1))		
		l.add_widget(b)
	
		popup = Popup(title='Aide',
						content=Label(text='Il faut trouver l image qui correspond \nau son entendu. Tu peux reecouter le son \nen cliquant sur l image en haut a \ndroite correspondante.\n Le but du jeu etant de trouver la bonne image le \nplus vite possible.'),
						size_hint=(None, None),
						size=(400, 200),
						)
		b.bind(on_press=popup.dismiss)
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

class Activite1_difficultApp(App):
    #Classe representant notre application
    
    
    def build(self):
		Config.set('graphics', 'width', 800)
		Config.set('graphics', 'height', 600)
        
		game = Activite1_difficult()
		game.serve()
		son = game.new_round()
		Clock.schedule_interval(game.update, 1.0 / 60.0)
		Clock.schedule_interval(game.increment_clock, 1.0)
		sound = SoundLoader.load(son)
		sound.play()
		return game

if __name__ == '__main__':
	Activite1_difficultApp().run()