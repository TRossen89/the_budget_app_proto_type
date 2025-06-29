#from kivy.uix.tabbedpanel import TabbedPanel

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
# Systematiser filerne med popups og andre ikke-Screen-klasser
from popup_calculator_for_disposable_amount import *


### """ ###
#
# Hvorfor er det her TextInput en klasse? Er der en god grund til det?
from text_input_screen_E_DISPOSABLE_AMOUNT import text_input_DISPOSABLE_AMOUNT



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



class Screen_E(Screen):

    def __init__(self, **kwargs):
        super(Screen_E, self).__init__(**kwargs)

    #-------MAKING LAST ENTERED BUDGET NAME APPEAR IN TOP OF SCREEN-----------


### """ ###
#
# Lav/brug en funktion til at læse/dumpe i json.filer

        filename_with_budget_name = "eb_BUDGET_NAME_for_the_budget_about_TO_BE_CREATED.json"

        with open(filename_with_budget_name, "r") as fileobject:
            budget_name = json.load(fileobject)

        self.ids.budget_name_in_top.text = budget_name



    #---ADDING TEXT INPUT FOR DISPOSABLE AMOUNT ON SCREEN

        self.text_input_with_disposable_amount = text_input_DISPOSABLE_AMOUNT()

        self.ids.relative_layout_for_DISPOSABLE_AMOUNT.add_widget(self.text_input_with_disposable_amount)



#---------------------------------------------------------------------
#-----------------------POP UP WINDOWS--------------------------------
#---------------------------------------------------------------------



#------OPENING BURGER MENU IN CORNER OF SCREEN-------

    def burger_menu_open(self):

        self.burger_menu_popup = burger_menu_pop_up()

        self.burger_menu_popup.open()




#------OPENING CALCULATOR FOR CALCULATING DISPOSABLE AMOUNT--------

    def open_calculator_for_disposable_amount(self):

        self.calculator = popup_calculator_for_disposable_amount()

        self.calculator.open()




# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

#----------------------------------------------------------------------------
#-------------------SAVING TEXT AND DATA IN JSON-----------------------------
#----------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------



#-------SAVING SCREEN_E AS LAST ENTERED SCREEN SO IF APP IS CLOSED WHILE SCREEN_E IS SHOWED,
# SCREEN_E WILL SHOW NEXT TIME APP IS OPENED--------

    def screen_E_in_last_entered_screen_json_file (self):

### """ ###
#
# Lav/brug en funktion til at læse/dumpe i json.filer

        screen_name_to_dump = "screen_E"

        filename = "the_LAST_ENTERED_screen.json"

        with open(filename, "w") as fileobject:
            json.dump(screen_name_to_dump, fileobject)







#-------SAVING SCREEN_A AS LAST ENTERED SCREEN SO IF APP IS CLOSED WHILE SCREEN_A IS SHOWED,
# SCREEN_A WILL SHOW NEXT TIME APP IS OPENED--------

### """ ###
#
# Lav/brug en funktion til at læse/dumpe i json.filer
    def screen_A_in_last_entered_screen_json_file(self):
        screen_name_to_dump = "screen_A"

        filename = "the_LAST_ENTERED_screen.json"

        with open(filename, "w") as fileobject:
            json.dump(screen_name_to_dump, fileobject)






# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# ------------------FUNCTIONALITY OF WIDGETS IN SCREEN E------------------------------
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------




#-------------------SHOWING ENTERED DISPOSABLE AMOUNT IN NEXT SCREEN----------------------------


    def function_showing_START_DISPOSABLE_amount_IN_NEXT_SCREEN(self):


        start_disposable_amount = self.text_input_with_disposable_amount.text

        App.get_running_app().root.get_screen("screen_F").ids.label_START_DISPOSABLE_AMOUNT.text = start_disposable_amount


        #------SAVING LAST ENTERED DISPOSABLE AMOUNT----------

### """ ###
#
# Lav/brug en funktion til at læse/dumpe i json.filer
        file_with_disposable_amount = "eb_DISPOSABLE_AMOUNT.json"

        with open(file_with_disposable_amount, "w") as file:
            json.dump(start_disposable_amount, file)





#------------------UPDATING REMAINING AMOUNT SHOWING IN NEXT SCREEN-----------------------------



    def function_showing_CORRECT_REMAINING_amount_IN_NEXT_SCREEN (self):



        start_amount = float(self.text_input_with_disposable_amount.text)

        total_of_all_expenses = float(App.get_running_app().root.get_screen("screen_F").ids.label_TOTAL_OF_ALL_EXPENSES.text)

        calculation_of_remaining_amount = start_amount - total_of_all_expenses


        the_remaining_amount = str(calculation_of_remaining_amount)


        App.get_running_app().root.get_screen("screen_F").ids.label_REMAINING_AMOUNT.text = the_remaining_amount






        #-------------SAVING CORRECT REMAINING AMOUNT---------------------

### """ ###
#
# Lav/brug en funktion til at læse/dumpe i json.filer

        file_with_remaining_amount = "eb_REMAINING_AMOUNT.json"


        with open(file_with_remaining_amount, "w") as file:
            json.dump(the_remaining_amount, file)



    pass