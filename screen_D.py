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





### """ ###
#
# forsøg at lave én klasse i en fil for sig, som klassen importeres fra, og der laves flere objekter ud af

class text_input_GIVE_BUDGET_NAME(TextInput):

    ### """ ###
    max_characters = NumericProperty(20)

    def __init__(self, **kwargs):
        super(text_input_GIVE_BUDGET_NAME, self).__init__(**kwargs)


    #-------MAKING LAST ENTERED BUDGET NAME APPEAR IN TEXT INPUT FOR BUDGET NAMING-----------


### """ ###
#
# Lav en funktion til at gemme last enterede screen/brug den til at gemme tekst

        filename_with_budget_name = "eb_BUDGET_NAME_for_the_budget_about_TO_BE_CREATED.json"

        with open(filename_with_budget_name, "r") as fileobject:
            budget_name = json.load(fileobject)

        self.text = budget_name




### """ ###
#
# Lav den her method om til den der bruges i Screen_G

    def insert_text(self, substring, from_undo=False):
        if len(self.text) >= self.max_characters and self.max_characters > 0:
            substring = ""
        TextInput.insert_text(self, substring, from_undo)


    def saving_current_budget_name(self):

        budget_name = self.text

        ### """ ###
        #
        # Lav en funktion til at gemme last enterede screen/brug den til at gemme tekst

        filename = "eb_BUDGET_NAME_for_the_budget_about_TO_BE_CREATED.json"

        with open(filename, "w") as fileobject:
            json.dump(budget_name, fileobject)


    pass














class Screen_D (Screen):



    def __init__(self, **kwargs):
        super(Screen_D, self).__init__(**kwargs)



    # -------MAKING LAST ENTERED BUDGET NAME APPEAR IN TEXT INPUT FOR BUDGET NAMING-----------

        #filename_with_budget_name = "eb_BUDGET_NAME_for_the_budget_about_TO_BE_CREATED.json"

        #with open(filename_with_budget_name, "r") as fileobject:
         #   budget_name = json.load(fileobject)

        #self.ids.text_input_for_budget_name.text = budget_name

        self.text_input_with_budget_name = text_input_GIVE_BUDGET_NAME()

        self.ids.relative_layout_for_GIVE_BUDGET_NAME.add_widget(self.text_input_with_budget_name)





# ---------------------------------------------------------------------
# -----------------------POP UP WINDOWS--------------------------------
# ---------------------------------------------------------------------



#------OPENING BURGER MENU IN CORNER OF SCREEN-------

    def burger_menu_open(self):

        burger_menu_popup = burger_menu_pop_up()

        burger_menu_popup.open()





# ---------------------------------------------------------------------------
# -------------------SAVING TEXT AND DATA IN JSON----------------------------
# ---------------------------------------------------------------------------




#-------SAVING SCREEN_D AS LAST ENTERED SCREEN SO IF APP IS CLOSED WHILE SCREEN_D IS SHOWED,
# SCREEN_D WILL SHOW NEXT TIME APP IS OPENED--------



### """ ###
#
# Lav en funktion til at gemme last enterede screen/brug den til at gemme tekst
    def screen_D_in_last_entered_screen_json_file (self):

        screen_name_to_dump = "screen_D"

        filename = "the_LAST_ENTERED_screen.json"

        with open(filename, "w") as fileobject:
            json.dump(screen_name_to_dump, fileobject)




# -------SAVING SCREEN_A AS LAST ENTERED SCREEN SO IF APP IS CLOSED WHILE SCREEN_A IS SHOWED,
# SCREEN_A WILL SHOW NEXT TIME APP IS OPENED--------




### """ ###
#
# Lav en funktion til at gemme last enterede screen/brug den til at gemme tekst
    def screen_A_in_last_entered_screen_json_file(self):
        screen_name_to_dump = "screen_A"

        filename = "the_LAST_ENTERED_screen.json"

        with open(filename, "w") as fileobject:
            json.dump(screen_name_to_dump, fileobject)




#------SAVING BUDGET NAME------------




    pass



#-----------------------------------------------------------------------------
#---------------MANIPULATING TEXT IN APP WHEN APP IS RUNNING------------------
#-----------------------------------------------------------------------------



#-------PUTTING THE ENTERED BUDGET NAME IN TOP OF SCREENS--------

    def putting_budget_name_in_top_of_screens(self):


        text_input_with_budget_name = text_input_GIVE_BUDGET_NAME()

        budget_name = text_input_with_budget_name.text


### """ ###
#
# Evt. brug en for loop her
        App.get_running_app().root.get_screen("screen_E").ids.budget_name_in_top.text = budget_name
        App.get_running_app().root.get_screen("screen_F").ids.budget_name_in_top.text = budget_name
        App.get_running_app().root.get_screen("screen_G").ids.budget_name_in_top.text = budget_name