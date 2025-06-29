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

from text_input_screen_G_START_DISPOSABLE_AMOUNT import text_input_START_DISPOSABLE_AMOUNT



### """ ###
#
# Systematiser ordningen og navngivningen af klasser i filer

from relativeLayout_screen_G_final_EXPENSE_FORMS import *

from relativeLayout_screen_G_NEW_final_EXPENSE_FORM import NEW_final_EXPENSE_button









### """ ###
#
# forsøg at lave én klasse i en fil for sig, som klassen importeres fra, og der laves flere objekter ud af
class ImageButton(ButtonBehavior, Image):


    pass


### """ ###
#
# forsøg at lave én klasse i en fil for sig, som klassen importeres fra, og der laves flere objekter ud af

class change_BUDGET_NAME_screen_G(Popup):


    def function_SAVING_BUDGET_NAME(self):

    #---BUDGET NAME ENTERED IN TEXT INPUT:

        new_budget_name = self.ids.text_input_CHANGE_BUDGET_NAME.text



    #---LOADING CURRENT BUDGET SHOWING (SO THAT THE NEW BUDGET NAME CAN BE SAVED IN CORRECT FILE)

    ### """ ###
    #
    # Lav/brug en funktion til at læse/dumpe i json.filer

        file_with_current_budget = f"eb_CURRENT_BUDGET_showing.json"

        with open(file_with_current_budget, "r") as file:
            current_budget = json.load(file)




    #---SAVING NEW NAME IN BUDGET NAME FILE

        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer
        file_with_name_of_the_budget = f"eb_a_created_budget_{current_budget}_BUDGET_NAME.json"

        with open(file_with_name_of_the_budget, "w") as file:
            json.dump(new_budget_name, file)


    #---SHOWING NEW BUDGET NAME IN SCREEN J

        App.get_running_app().root.get_screen("screen_G").ids.budget_name_in_top.text = new_budget_name



    #---CLOSING POP UP

        self.dismiss()




### """ ###
#
# forsøg at lave én klasse i en fil for sig, som klassen importeres fra, og der laves flere objekter ud af

class burger_menu_pop_up (Popup):
    pass





class Screen_G(Screen):


#---SIZE_HINT_Y OF EXPENSES MAIN GRID FRAME (IT INCREASES EVERY TIME THE USER ADD AN EXPENSE FORM TO THE SCREEN)--------

    size_hint_y_of_expenses_main_grid_frame = NumericProperty(4)


#---POS_HINT_Y OF GRID FRAME FOR NEW FINAL EXPENSE BUTTON
#---(IT DECREASES FOR EVERY EXPENSE ADDED TO GRID FRAME FOR ALL EXPENSES)-----

    pos_hint_y_of_grid_for_new_final_expense_button = NumericProperty(.994)


    def __init__(self, **kwargs):
        super(Screen_G, self).__init__(**kwargs)






    #---SHOWING START DISPOSABLE AMOUNT/SALDO

        self.text_input_with_start_disposable_amount = text_input_START_DISPOSABLE_AMOUNT()

        self.ids.relative_layout_for_results.add_widget(self.text_input_with_start_disposable_amount)



    #---SHOWING NEW (final) EXPENSE BUTTON:

        self.text_input_with_new_final_expense_button = NEW_final_EXPENSE_button()
        self.ids.grid_frame_for_new_final_expense_button.add_widget(self.text_input_with_new_final_expense_button)



    #---WHEN APP IS OPENED: SHOWING ENTERED EXPENSES IN SCREEN G AND LAST CALCULATED START AMOUNT, TOTAL OF EXPENSES,
    #---REMAINING AMOUNT, TOTAL OF PAID EXPENSES, CURRENT DISPOSABLE AMOUNT --------------------------------------


        file_with_id_of_current_budget_showing_in_screen_G = f"eb_CURRENT_BUDGET_showing.json"

        with open(file_with_id_of_current_budget_showing_in_screen_G, "r") as file:
            current_budget = json.load(file)


        if current_budget == 0:
            pass

        else:



            file_with_budget_name = f"eb_a_created_budget_{current_budget}_BUDGET_NAME.json"

            with open(file_with_budget_name, "r") as file:
                budget_name = json.load(file)

            self.ids.budget_name_in_top.text = budget_name





            file_with_total_of_all_expenses = f"eb_a_created_budget_{current_budget}_TOTAL_OF_ALL_EXPENSES.json"

            with open(file_with_total_of_all_expenses, "r") as file:
                total_of_all_expenses = json.load(file)

                self.ids.label_TOTAL_OF_ALL_EXPENSES.text = total_of_all_expenses





            file_with_remaining_amount = f"eb_a_created_budget_{current_budget}_REMAINING_AMOUNT.json"

            with open(file_with_remaining_amount, "r") as file:
                remaining_amount = json.load(file)

                self.ids.label_REMAINING_AMOUNT.text = remaining_amount






            file_with_total_of_paid_expenses = f"eb_a_created_budget_{current_budget}_TOTAL_OF_PAID_EXPENSES.json"

            with open(file_with_total_of_paid_expenses, "r") as file:
                total_of_paid_expenses = json.load(file)

                self.ids.label_TOTAL_OF_PAID_EXPENSES.text = total_of_paid_expenses






            file_with_current_disposable_amount = f"eb_a_created_budget_{current_budget}_CURRENT_DISPOSABLE_AMOUNT.json"

            with open(file_with_current_disposable_amount, "r") as file:
                current_disposable_amount = json.load(file)

                self.ids.label_CURRENT_DISPOSABLE_AMOUNT.text = current_disposable_amount



            # CREATING DICTIONARY FOR THE EXPENSE FORMS (OBJECTS) SO THEY CAN BE REACHED
            # FROM TEXT INPUTS IN EDIT EXPENSE POP UP

            self.dictionary_with_expense_forms = {}

            list_with_keys = []



            file_with_the_expenses_in_the_current_budget = f"eb_a_created_budget_{current_budget}_THE_EXPENSES.json"

            with open (file_with_the_expenses_in_the_current_budget, "r") as file:

                dictionary_with_multiply_description_etc = json.load(file)




                for key in dictionary_with_multiply_description_etc:


                #---THE KEYS OF EXPENSES ARE PLACED IN A LIST SO THEY CAN BE SORTED
                #--- (I DON'T KNOW OF ANY WAYS TO SORT A DICTIONARY):

                    the_key_for_list_to_order_keys_in = int(key)

                    list_with_keys.append(the_key_for_list_to_order_keys_in)

            # ---SORTING THE KEYS IN DICTIONARY SO THE EXPENSES EVENTUALLY WILL BE SHOWNED IN CORRECT ORDER:
            list_with_keys.sort()



            for key in list_with_keys:

                if key == 0:
                    pass

                else:

                    key_with_expense_information = str(key)



                # GOING THROUGH THE DICTIONARY OF EXPENSES AND READING THE EXPENSES INFORMATION (MULTIPLY
                    # VALUE, DESCRIPTION, AMOUNT, DIVIDE VALUE, TOTAL AMOUNT) OF EVERY EXPENSE

                    with open(file_with_the_expenses_in_the_current_budget, "r") as file:
                        dict_with_multiply_description_etc = json.load(file)


                        list_with_multiply_description_etc = dict_with_multiply_description_etc[key_with_expense_information]



                        value_for_multiply_text_input = list_with_multiply_description_etc[0]

                        text_for_description = list_with_multiply_description_etc[1]

                        value_for_amount = list_with_multiply_description_etc[2]

                        value_for_divide = list_with_multiply_description_etc[3]

                        value_for_total_amount = list_with_multiply_description_etc[4]



                        self.pos_hint_y_of_grid_for_new_final_expense_button -= .0005




                        self.the_final_expenses = final_expenses(key_with_expense_information, value_for_multiply_text_input, text_for_description, value_for_amount, value_for_divide,
                             value_for_total_amount)



                        self.ids.\
                            grid_frame_for_all_expenses.add_widget\
                            (self.the_final_expenses)


                        expense_form_for_dictionary_with_expense_forms = {key_with_expense_information: self.the_final_expenses}

                        self.dictionary_with_expense_forms.update(expense_form_for_dictionary_with_expense_forms)





            #self.dictionary_with_expense_forms = dictionary_with_expense_forms













#---POPUP WITH FORM TO CHANGE BUDGET NAME (WHEN PRESSING LABEL WITH BUDGET NAME)




    def function_CHANGE_BUDGET_NAME(self):

        change_name_popup = change_BUDGET_NAME_screen_G()

        change_name_popup.open()

        pass





#------OPENING BURGER MENU IN CORNER OF SCREEN-------

    def burger_menu_open(self):

        burger_menu_popup = burger_menu_pop_up()

        burger_menu_popup.open()








# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

#----------------------------------------------------------------------------
#-------------------SAVING TEXT AND DATA IN JSON-----------------------------
#----------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------




#---SAVING SCREEN_G AS LAST ENTERED SCREEN SO IF APP IS CLOSED WHILE SCREEN_F IS SHOWED,
# SCREEN_F WILL SHOW NEXT TIME APP IS OPENED--------

    def screen_G_in_last_entered_screen_json_file (self):


        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer
        screen_name_to_dump = "screen_G"

        filename = "the_LAST_ENTERED_screen.json"

        with open(filename, "w") as fileobject:
            json.dump(screen_name_to_dump, fileobject)




#---SAVING SCREEN_A AS LAST ENTERED SCREEN SO IF APP IS CLOSED WHILE SCREEN_A IS SHOWED,
# SCREEN_A WILL SHOW NEXT TIME APP IS OPENED--------

    def screen_A_in_last_entered_screen_json_file(self):

        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer

        screen_name_to_dump = "screen_A"

        filename = "the_LAST_ENTERED_screen.json"

        with open(filename, "w") as fileobject:
            json.dump(screen_name_to_dump, fileobject)














#-----------------------SAVING LAST CALCULATED TOTAL OF ALL EXPENSES----------------------------



### """ ###
#
# Systematiser navngivningen af funktioner (on_text, on_release, on_focus, etc.)

    def saving_TOTAL_OF_ALL_EXPENSES(self):


        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer

        file_with_id_of_current_budget_showing_in_screen_G = f"eb_CURRENT_BUDGET_showing.json"

        with open(file_with_id_of_current_budget_showing_in_screen_G, "r") as file:
            current_budget = json.load(file)

        if current_budget == 0:
            pass

        else:

            ### """ ###
            #
            # Lav/brug en funktion til at læse/dumpe i json.filer

            total_to_save = self.ids.label_TOTAL_OF_ALL_EXPENSES.text

            file_with_last_calculated_total_of_all_expenses = \
                f"eb_a_created_budget_{current_budget}_TOTAL_OF_ALL_EXPENSES.json"

            with open(file_with_last_calculated_total_of_all_expenses, "w") as file:
                json.dump(total_to_save, file)













#--------------------------SAVING LAST CALCULATED REMAINING AMOUNT------------------------------


### """ ###
#
# Systematiser navngivningen af funktioner (on_text, on_release, on_focus, etc.)
    def saving_REMAINING_AMOUNT(self):


        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer

        file_with_id_of_current_budget_showing_in_screen_G = f"eb_CURRENT_BUDGET_showing.json"

        with open(file_with_id_of_current_budget_showing_in_screen_G, "r") as file:
            current_budget = json.load(file)

        if current_budget == 0:
            pass

        else:



            remaining_amount_to_save = self.ids.label_REMAINING_AMOUNT.text

            file_with_last_calculated_remaining_amount = f"eb_a_created_budget_{current_budget}_REMAINING_AMOUNT.json"

            with open(file_with_last_calculated_remaining_amount, "w") as file:
                json.dump(remaining_amount_to_save, file)









#---------------------------SAVING LAST ENTERED TOTAL OF PAID EXPENSES -------------------------------

### """ ###
#
# Systematiser navngivningen af funktioner (on_text, on_release, on_focus, etc.)
    def saving_TOTAL_OF_PAID_EXPENSES(self):



        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer

        file_with_id_of_current_budget_showing_in_screen_G = f"eb_CURRENT_BUDGET_showing.json"

        with open(file_with_id_of_current_budget_showing_in_screen_G, "r") as file:
            current_budget = json.load(file)

        if current_budget == 0:
            pass

        else:


            total_of_paid_expenses_to_save = self.ids.label_TOTAL_OF_PAID_EXPENSES.text

            file_with_last_calculated_total_of_paid_expenses = \
                f"eb_a_created_budget_{current_budget}_TOTAL_OF_PAID_EXPENSES.json"

            with open(file_with_last_calculated_total_of_paid_expenses, "w") as file:
                json.dump(total_of_paid_expenses_to_save, file)














#---SAVING CURRENT DISPOSABLE AMOUNT----

### """ ###
#
# Systematiser navngivningen af funktioner (on_text, on_release, on_focus, etc.)
    def saving_CURRENT_DISPOSABLE_AMOUNT(self):


        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer

        file_with_id_of_current_budget_showing_in_screen_G = f"eb_CURRENT_BUDGET_showing.json"

        with open(file_with_id_of_current_budget_showing_in_screen_G, "r") as file:
            current_budget = json.load(file)

        if current_budget == 0:
            pass

        else:


            current_disposable_amount_to_save = self.ids.label_CURRENT_DISPOSABLE_AMOUNT.text

            file_with_last_calculated_current_disposable_amount = f"eb_a_created_budget_{current_budget}_CURRENT_DISPOSABLE_AMOUNT.json"

            with open(file_with_last_calculated_current_disposable_amount, "w") as file:
                json.dump(current_disposable_amount_to_save, file)







# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

#----------------------------------------------------------------------------
#-----------UPDATING REMAINING AMOUNT AND CURRENT DISPOSABLE AMOUNT----------
#----------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------





#---on_text FUNCTION FOR label_TOTAL_OF_ALL_EXPENSES: SHOWING CORRECT REMAINING AMOUNT ALL THE TIME: ----------------------------------------

### """ ###
#
# Systematiser navngivningen af funktioner (on_text, on_release, on_focus, etc.)

    def on_text_calculating_NEW_REMAINING_AMOUNT(self):

        # Systematiser navngivningen af instanser, id, funktioner, klasser osv. (on_text, on_release, on_focus, etc.)
        start_disposable_amount = float(self.text_input_with_start_disposable_amount.text)

        new_total_of_all_expenses = float(self.ids.label_TOTAL_OF_ALL_EXPENSES.text)



        new_remaining_amount = start_disposable_amount - new_total_of_all_expenses


        self.ids.label_REMAINING_AMOUNT.text = str(new_remaining_amount)






#---SHOWING CORRECT CURRENT DISPOSABLE AMOUNT ALL THE TIME: ----------------------------------------


# Systematiser navngivningen af instanser, id, funktioner, klasser osv. (on_text, on_release, on_focus, etc.)
    def on_text_calculating_NEW_CURRENT_DISPOSABLE_AMOUNT(self):

    # Systematiser navngivningen af instanser, id, funktioner, klasser osv. (on_text, on_release, on_focus, etc.)
        start_disposable_amount = float(self.text_input_with_start_disposable_amount.text)

        new_total_of_paid_expenses = float(self.ids.label_TOTAL_OF_PAID_EXPENSES.text)


        new_current_disposable_amount = start_disposable_amount - new_total_of_paid_expenses


        self.ids.label_CURRENT_DISPOSABLE_AMOUNT.text = str(new_current_disposable_amount)
