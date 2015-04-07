__author__ = 'wizar_000'
__author__ = 'wizar_000'
import kivy

kivy.require('1.0.5')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, \
    ObjectProperty
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.layout import Layout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
import random

import dataBase


class SoundObject(Widget):

    #Attributes of the class
    sound = SoundLoader
    music_index = 0
    first_play = True
    pos_base=[0,0]

    def __init__(self,pos,**kwargs):

        Widget.__init__(self, **kwargs)
        self.sound = SoundLoader
        self.music_index = -1
        self.first_play = True

    def on_touch_down(self, touch):
        global sound
        # global music_index
        self.music_index = self.parent.Target_Music_list[0]
        if self.collide_point(*touch.pos):
            sound= SoundLoader.load(self.parent.Music_Directory_List[self.music_index])
            sound.play()

    def on_touch_up(self, touch):
        global sound
        # global music_index
        # global first_play
        sound.stop()
        # print self.first_play
        if self.collide_point(*touch.pos):
            if self.first_play:
                self.first_play = False
            else:
                print self.parent.Last_Displayed_Music
                print self.music_index
                if self.parent.Last_Displayed_Music == -1:
                    self.parent.Last_Displayed_Music = self.music_index
                else:
                    if self.music_index ==  self.parent.chosen_music_index and self.parent.Last_Displayed_Music ==  self.parent.chosen_music_index:
                        if self.parent.current_niveau == self.parent.NIVEAU[0]  :
                            self.parent.score +=1
                        elif self.parent.current_niveau == self.parent.NIVEAU[1]:
                            self.parent.score +=5
                        else:
                            self.parent.score+=10
                        self.parent.on_winning()
                    else:
                        if self.parent.current_niveau == self.parent.NIVEAU[0]  :
                            self.parent.score -=1
                        elif self.parent.current_niveau == self.parent.NIVEAU[1]:
                            self.parent.score -=5
                        else:
                            self.parent.score-=10
                    self.parent.Last_Displayed_Music = -1
            print self.parent.two_same_music_index_array

class TestGame2Game(Widget):
    """
    Class representing the soundGame
"""
    # Open a dataBase connexion
    # local_db = dataBase.DataBase()
    # table_name = "SoundGame"
    # table_attributes = ["time Date", "score integer", "source string", "destination string", "result string" ]
    # local_db.create_Table(table_name,table_attributes)

    #Save window's size to use later
    windowSave = Window.size;

    #Create music directory list
    Music_Directory_List = ["../res/sound/bear_growl_y.wav"
        , "../res/sound/bird.wav"
        , "../res/sound/bird_caw1.wav"
        , "../res/sound/bird_caw2.wav"
        , "../res/sound/bird_chirp.wav"
        , "../res/sound/bird_chirping2.wav"
        , "../res/sound/bison.wav"
        , "../res/sound/cat_big_x.wav"
        , "../res/sound/cat_kitten.wav"
        , "../res/sound/cat_y.wav"
        , "../res/sound/coyote_howl.wav"
        , "../res/sound/dog_bark3.wav"
        , "../res/sound/dog_bark5.wav"
        , "../res/sound/dog_bark6.wav"
        , "../res/sound/dog_bark_x.wav"
        , "../res/sound/dog_x.wav"]
    #for real time music playlist randomly
    Music_PlayList = []
    #Define buttons
    btn1 = ObjectProperty(Button)
    btn2 = ObjectProperty(Button)
    btn3 = ObjectProperty(Button)
    btn4 = ObjectProperty(Button)
    btn5 = ObjectProperty(Button)
    btn6 = ObjectProperty(Button)
    btn7 = ObjectProperty(Button)
    btn8 = ObjectProperty(Button)
    btn9 = ObjectProperty(Button)
    # Music_Directory_List.append(ssSource)
    # print Music_Directory_List
    #Create music name list

    #List to store Form displayed and Object displayed
    Target_Music_list = []  #List to store music displayed in table
    played_music_list = []
    two_same_music_index_array = []
    chosen_music_index = -1
    Last_Displayed_Music =-1  #List to store
    NIVEAU = ['easy','media','difficult']
    current_niveau = NIVEAU[1]

    #when inite the game
    def __init__(self, **kwargs):
        """
        Function called when soundGame is created        :param kwargs:
        :return:
        """
        Widget.__init__(self, **kwargs)
        self.new_round()
        # self.playMusic()

    #score for player
    score = NumericProperty(0)
    clock = NumericProperty(0)


    def playMusic(self):
        print str(self.Music_Directory_List[0])
        sound = SoundLoader.load(str(self.Music_Directory_List[0]))
        sound.play()

    def new_round(self):
        objects_num = 0
        size_Music_List = len(self.Music_Directory_List)
        self.Target_Music_list = []
        if self.current_niveau == self.NIVEAU[0]:
            objects_num = 6
        elif self.current_niveau == self.NIVEAU[1]:
            objects_num = 9
        else:objects_num = 16
        object_counter = 0
        while(object_counter< objects_num-1):
            rand = random.randint(0, size_Music_List-1)
            if rand not in self.Target_Music_list:
                self.Target_Music_list.append(rand)
                object_counter = object_counter+1
        """we choose a music from the target music library
        and choose a random button to put in
        """
        target_music_index = random.randint(0,objects_num-2)
        print self.Target_Music_list
        print target_music_index
        self.two_same_music_index_array.append(target_music_index) # we put the first chosen into the list
        inserted_index = random.randint(0,objects_num-2)
        while inserted_index == target_music_index:
            inserted_index = random.randint(0,objects_num-2)
        print inserted_index
        print self.current_niveau
        self.two_same_music_index_array.append(inserted_index) # we put the second chosen into the list
        self.Target_Music_list.insert(inserted_index,self.Target_Music_list[inserted_index]) # we insert the chosen music into the target music list
        print self.Target_Music_list
        self.chosen_music_index = self.Target_Music_list[inserted_index]
        print self.chosen_music_index

    def increment_clock(self, dt):
        self.clock += 1;
        # if (self.touched!=1):
        #     self.clock += 1;
        # else:
        #     return False;

    def updateWidget(self):
        for obj in self.ObjectList:
            obj.updateCatSize();
            break

    def update(self, dt):
        if (Window.size != self.windowSave):
            self.windowSave = Window.size
            self.updateWidget()
            # if (self.remaining==0):
            #     self.on_winning();
            #     return False;

    def on_winning(self):
        layout = BoxLayout(orientation='vertical')

        def callback(instance):
            if (instance.text == 'Continuer'):
                popup.dismiss()
                self.__init__()
                self.clock = 0
            elif instance.text == 'Changer de jeu':
                popup.dismiss()
                self.change_degree()



        btn1 = Button(text='Continuer')
        btn1.bind(on_press=callback)
        btn2 = Button(text='Changer de jeu')
        btn2.bind(on_press=callback)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        popup = Popup(title='Felicitations !!! Ton score : ' + str(self.score),
                      title_size='20sp',
                      content=layout,
                      size_hint=(None, None),
                      size=(400, 400),
                      auto_dismiss=False)
        popup.open()
        print("popup ouvert")
        sound = SoundLoader.load('../res/finished.wav')
        sound.play()

    def change_degree(self):
        layout = BoxLayout(orientation='vertical')

        def handle_degree(instance):
            if instance.text == 'easy':
                popup.dismiss()
                self.current_niveau = self.NIVEAU[0]
                self.__init__()
            if instance.text == 'medium':
                popup.dismiss()
                self.current_niveau = self.NIVEAU[1]
                self.__init__()
            if instance.text == 'difficult':
                popup.dismiss()
                self.current_niveau = self.NIVEAU[2]
                self.__init__()


        btn1 = Button(text = 'easy')
        btn1.bind(on_press = handle_degree)
        btn2 = Button(text = 'medium')
        btn2.bind(on_press = handle_degree)
        btn3 = Button(text = 'difficult')
        btn3.bind(on_press = handle_degree)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        popup = Popup(title='Choose from below',
                      title_size='20sp',
                      content=layout,
                      size_hint=(None, None),
                      size=(400, 400),
                      auto_dismiss=False)
        popup.open()


    def updateWidget(self):
        for obj in self.ObjectList:
            obj.updateCatSize();
            break

    def aide(self):
        l = BoxLayout(orientation='vertical')
        b = Button(text='Quitter', size_hint=(0.5, 0.1))
        l.add_widget(b)

        popup = Popup(title='Aide',
                      content=Label(text='  Deux de ces cartes emettent le meme son. Il faut les\n'
                                         '  trouver. Vous pouvez ecouter le son emis par chaque\n'
                                         '  carte une seule fois sans perdre de point;sinon vous\n'
                                         '  perdrez des point par mauvaise carte. Bon courage !'),
                      size_hint=(None, None),
                      size=(400, 200),
                      )

        b.bind(on_press=popup.dismiss)
        popup.open()

    # def menu(self):
    #     return menu.MenuApp().run();

    def stop(self):
        return TestGame2App().stop()


class TestGame2App(App):
    def build(self):
        # sound = SoundLoader.load('res/CEstUneBinsa.wav')
        # sound.play()
        Config.set('graphics', 'width', 800)
        Config.set('graphics', 'height', 600)
        game = TestGame2Game()
        # game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        Clock.schedule_interval(game.increment_clock, 1.0)

        # print(Config.get('graphics', 'width'))
        # print(Config.get('graphics', 'height'))
        return game


if __name__ == '__main__':
    TestGame2App().run()
