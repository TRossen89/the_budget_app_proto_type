from kivy.app import App
from kivy.uix import widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.properties import DictProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition
from kivy.uix.screenmanager import SlideTransition
#from kivy.uix.tabbedpanel import TabbedPanel
from kivy.metrics import dp
from kivy.uix.slider import Slider
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.clock import Clock
from functools import partial
from kivy.uix.popup import Popup
import json
import os
import datetime



### """ ###
#
# forsøg at lave én klasse i en fil for sig, som klassen importeres fra, og der laves flere objekter ud af
class ImageButton(ButtonBehavior, Image):
    pass



### """ ###
#
# forsøg at lave én klasse i en fil for sig, som klassen importeres fra, og der laves flere objekter ud af
class burger_menu_pop_up (Popup):
    pass





class Screen_B(Screen):



#------OPENING BURGER MENU IN CORNER OF SCREEN-------

    def burger_menu_open(self):

        burger_menu_popup = burger_menu_pop_up()

        burger_menu_popup.open()




#-------SAVING SCREEN_B AS LAST ENTERED SCREEN SO IF APP IS CLOSED WHILE SCREEN_B IS SHOWED,
# SCREEN_B WILL SHOW NEXT TIME APP IS OPENED--------




### """ ###
#
# Lav en funktion til at gemme last enterede screen/brug den til at gemme tekst

    def screen_B_in_last_entered_screen_json_file (self):

        screen_name_to_dump = "screen_B"

        filename = "the_LAST_ENTERED_screen.json"

        with open(filename, "w") as fileobject:
            json.dump(screen_name_to_dump, fileobject)




# -------SAVING SCREEN_A AS LAST ENTERED SCREEN SO IF APP IS CLOSED WHILE SCREEN_A IS SHOWED,
# SCREEN_A WILL SHOW NEXT TIME APP IS OPENED--------


## """ ###
#
# Lav en funktion til at gemme last enterede screen/brug den til at gemme tekst
    def screen_A_in_last_entered_screen_json_file(self):
        screen_name_to_dump = "screen_A"

        filename = "the_LAST_ENTERED_screen.json"

        with open(filename, "w") as fileobject:
            json.dump(screen_name_to_dump, fileobject)



    pass