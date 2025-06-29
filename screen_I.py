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
# from kivy.uix.tabbedpanel import TabbedPanel
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


from relativeLayout_eb_list_of_BUDGETS import eb_budgets




### """ ###
#
# forsøg at lave én klasse i en fil for sig, som klassen importeres fra, og der laves flere objekter ud af

class ImageButton(ButtonBehavior, Image):
    pass


### """ ###
#
# forsøg at lave én klasse i en fil for sig, som klassen importeres fra, og der laves flere objekter ud af
class burger_menu_pop_up(Popup):
    pass





class Screen_I (Screen):



    size_hint_y_of_expenses_main_grid_frame = NumericProperty(3)




    def __init__(self, **kwargs):
        super(Screen_I, self).__init__(**kwargs)




    #---SHOWING LIST OF CREATED BUDGETS IN SCREEN I: -------------------


        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer

        file_with_list_of_ids_of_current_budget_showing = f"eb_LIST_of_BUDGET_IDS.json"

        with open(file_with_list_of_ids_of_current_budget_showing, "r") as file:
            budgets_to_show_in_screen_I = json.load(file)



        for id in budgets_to_show_in_screen_I:

            if id == 0:
                pass

            else:

                budget_to_add = eb_budgets(id)

                self.ids.grid_frame_for_all_eb_budgets.add_widget(budget_to_add)




#---SHOWING LIST OF BUDGETS WHEN A BUDGETS NAME HAS BEEN CHANGED

    def on_enter_LIST_OF_BUDGETS_after_CHANGED_BUDGET_NAME(self):

        # CLEARING SCREEN J SO THERE IS ROOM FOR NEW LIST OF BUDGETS WITH THE
        # UPDATED BUDGET NAME FOR CURRENT BUDGET SHOWING

        App.get_running_app().root.get_screen("screen_I").ids.grid_frame_for_all_eb_budgets.clear_widgets()


        # LOADING LIST WITH BUDGETS (BUDGET IDS) TO BE SHOWN IN SCREEN I
        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer

        file_with_list_of_budget_ids = f"eb_LIST_of_BUDGET_IDS.json"

        with open(file_with_list_of_budget_ids, "r") as file:
            list_with_budget_ids = json.load(file)


            # DISPLAYING LIST OF BUDGETS WITH UPDATED NAME OF CURRENT BUDGET

            for id in list_with_budget_ids:

                if id == 0:
                    pass

                else:
                    budget_id = str(id)

                    App.get_running_app().root.get_screen("screen_I").ids.grid_frame_for_all_eb_budgets.add_widget(
                        eb_budgets(budget_id))



    #---OPENING BURGER MENU IN CORNER OF SCREEN-------

    def burger_menu_open(self):
        burger_menu_popup = burger_menu_pop_up()

        burger_menu_popup.open()




#---SAVING SCREEN_I AS LAST ENTERED SCREEN SO IF APP IS CLOSED WHILE SCREEN_I IS SHOWED,
#---SCREEN_I WILL SHOW NEXT TIME APP IS OPENED--------


    def screen_I_in_last_entered_screen_json_file(self):


        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer

        screen_name_to_dump = "screen_I"

        filename = "the_LAST_ENTERED_screen.json"

        with open(filename, "w") as fileobject:
            json.dump(screen_name_to_dump, fileobject)



#---SAVING SCREEN_A AS LAST ENTERED SCREEN SO IF APP IS CLOSED WHILE SCREEN_A IS SHOWED,
#---SCREEN_A WILL SHOW NEXT TIME APP IS OPENED--------

    def screen_A_in_last_entered_screen_json_file(self):


        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer


        screen_name_to_dump = "screen_A"

        filename = "the_LAST_ENTERED_screen.json"

        with open(filename, "w") as fileobject:
            json.dump(screen_name_to_dump, fileobject)





    pass