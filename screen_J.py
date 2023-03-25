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

from relativeLayout_screen_J_final_EXPENSE_FORMS import expenses_screen_J
from relativeLayout_screen_J_NEW_final_EXPENSE_FORMS import button_NEW_EXPENSE_screen_J


### """ ###
#
# forsøg at lave én klasse i en fil for sig, som klassen importeres fra, og der laves flere objekter ud af

class ImageButton(ButtonBehavior, Image):
    pass




### """ ###
#
# forsøg at lave én klasse i en fil for sig, som klassen importeres fra, og der laves flere objekter ud af

class change_BUDGET_NAME_screen_J(Popup):



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

        App.get_running_app().root.get_screen("screen_J").ids.budget_name_in_top.text = new_budget_name



    #---CLOSING POP UP

        self.dismiss()


    pass



### """ ###
#
# forsøg at lave én klasse i en fil for sig, som klassen importeres fra, og der laves flere objekter ud af

class burger_menu_pop_up(Popup):
    pass








class Screen_J (Screen):



    size_hint_y_of_expenses_main_grid_frame = NumericProperty(3)


#---POS_HINT_Y OF GRID FRAM FOR NEW (FINAL) EXPENSES-----------------

    pos_hint_y_of_grid_for_new_final_expense_button = NumericProperty(.994)



    def __init__(self, **kwargs):
        super(Screen_J, self).__init__(**kwargs)



    #---SHOWING NEW (final) EXPENSE BUTTON:

        self.ids.grid_frame_for_new_final_expense_button.add_widget(button_NEW_EXPENSE_screen_J())


    #---WHEN APP IS OPENED: DISPLAYING ENTERED EXPENSES IN SCREEN G AND LAST CALCULATED START AMOUNT, TOTAL OF EXPENSES,
    #---REMAINING AMOUNT, TOTAL OF PAID EXPENSES, CURRENT DISPOSABLE AMOUNT --------------------------------------

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

            file_with_budget_name = f"eb_a_created_budget_{current_budget}_BUDGET_NAME.json"

            with open(file_with_budget_name, "r") as file:
                budget_name = json.load(file)

            self.ids.budget_name_in_top.text = budget_name





            file_with_start_disposable_amount = f"eb_a_created_budget_{current_budget}_DISPOSABLE_AMOUNT.json"

            with open(file_with_start_disposable_amount, "r") as file:
                disposable_amount = json.load(file)

                self.ids.label_START_DISPOSABLE_AMOUNT.text = disposable_amount





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



            list_with_keys = []


            ### """ ###
            #
            # Lav/brug en funktion til at læse/dumpe i json.filer

            file_with_the_expenses_in_the_current_budget = f"eb_a_created_budget_{current_budget}_THE_EXPENSES.json"

            with open(file_with_the_expenses_in_the_current_budget, "r") as file:
                dictionary_with_multiply_description_etc = json.load(file)




                for key in dictionary_with_multiply_description_etc:



                    # ---SORTING THE KEYS FROM THE DICTIONARY SO THE EXPENSES
                    # EVENTUALLY WILL BE SHOWNED IN CORRECT ORDER:

                    the_key_for_list_to_order_keys_in = int(key)

                    list_with_keys.append(the_key_for_list_to_order_keys_in)


            list_with_keys.sort()


            for key in list_with_keys:

                if key == 0:
                    pass

                else:

                    key_with_expense_information = str(key)

                    with open(file_with_the_expenses_in_the_current_budget, "r") as file:
                        dict_with_multiply_description_etc = json.load(file)

                        list_with_multiply_description_etc = dict_with_multiply_description_etc[
                            key_with_expense_information]

                        value_for_multiply_text_input = list_with_multiply_description_etc[0]

                        text_for_description = list_with_multiply_description_etc[1]

                        value_for_amount = list_with_multiply_description_etc[2]

                        value_for_divide = list_with_multiply_description_etc[3]

                        value_for_total_amount = list_with_multiply_description_etc[4]



                        self.pos_hint_y_of_grid_for_new_final_expense_button -= .0005

                        self.size_hint_y_of_expenses_main_grid_frame += .08

                        self.ids. \
                            grid_frame_for_all_expenses.add_widget \
                            (expenses_screen_J
                             (key_with_expense_information, value_for_multiply_text_input, text_for_description, value_for_amount, value_for_divide,
                              value_for_total_amount))






#---POPUP WITH FORM TO CHANGE BUDGET NAME (WHEN PRESSING LABEL WITH BUDGET NAME)

    ### """ ###
    #
    # forsøg at lave én klasse i en fil for sig, som klassen importeres fra, og der laves flere objekter ud af

    def function_CHANGE_BUDGET_NAME(self):

        change_name_popup = change_BUDGET_NAME_screen_J()

        change_name_popup.open()

        pass



#---OPENING BURGER MENU IN CORNER OF SCREEN-------

    ### """ ###
    #
    # forsøg at lave én klasse i en fil for sig, som klassen importeres fra, og der laves flere objekter ud af
    def burger_menu_open(self):
        burger_menu_popup = burger_menu_pop_up()

        burger_menu_popup.open()





#---MAKING SURE THERE IS ALWAYS A INT/FLOAT TYPE SIGN IN SALDO TEXT INPUT


### """ ###
#
# Maybe change this, so that it's okay that there isn't float/int/double in saldo TextInput.
# Do this by creating if statements all the places where saldo is used in calculations - if statements
# that says if saldo == "" then saldo == "0"

    def on_text_if_nothing_then_0_in_SALDO_text_input(self):

        text_in_text_input = self.ids.label_START_DISPOSABLE_AMOUNT.text

        if text_in_text_input == "":
            self.ids.label_START_DISPOSABLE_AMOUNT.text = "0"



#---SAVING SCREEN_I AS LAST ENTERED SCREEN SO IF APP IS CLOSED WHILE SCREEN_I IS SHOWED,
#---SCREEN_I WILL SHOW NEXT TIME APP IS OPENED--------


    def screen_J_in_last_entered_screen_json_file(self):

        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer

        screen_name_to_dump = "screen_J"

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








#---------------------------SAVING LAST ENTERED DISPOSABLE AMOUNT-------------------------------

    def saving_DISPOSABLE_AMOUNT(self):

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

            disposable_amount_to_save = self.ids.label_START_DISPOSABLE_AMOUNT.text

            file_with_last_entered_disposable_amount = f"eb_a_created_budget_{current_budget}_DISPOSABLE_AMOUNT.json"

            with open(file_with_last_entered_disposable_amount, "w") as file:
                json.dump(disposable_amount_to_save, file)





    def on_text_calculating_REMAINING_AMOUNT_and_CURRENT_DISPOSABLE_AMOUNT(self):

        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer

        file_with_id_of_current_budget_showing_in_screen_G = f"eb_CURRENT_BUDGET_showing.json"

        with open(file_with_id_of_current_budget_showing_in_screen_G, "r") as file:
            current_budget = json.load(file)

        if current_budget == 0:
            pass

        else:

            string_with_start_disposable_amount = self.ids.label_START_DISPOSABLE_AMOUNT.text

            if string_with_start_disposable_amount == "":


                self.ids.label_START_DISPOSABLE_AMOUNT.text = "0"


                total_of_expected_expenses = self.ids.label_TOTAL_OF_ALL_EXPENSES.text


                self.ids.label_REMAINING_AMOUNT.text = f"-{total_of_expected_expenses}"


                total_of_paid_expenses = self.ids.label_TOTAL_OF_PAID_EXPENSES.text

                self.ids.label_CURRENT_DISPOSABLE_AMOUNT.text = f"-{total_of_paid_expenses}"



            else:


                start_disposable_amount = float(self.ids.label_START_DISPOSABLE_AMOUNT.text)

                total_of_expected_expenses = float(self.ids.label_TOTAL_OF_ALL_EXPENSES.text)

                total_of_paid_expenses = float(self.ids.label_TOTAL_OF_PAID_EXPENSES.text)

                self.ids.label_REMAINING_AMOUNT.text = str(start_disposable_amount - total_of_expected_expenses)

                self.ids.label_CURRENT_DISPOSABLE_AMOUNT.text = str(start_disposable_amount - total_of_paid_expenses)



#-----------------------SAVING LAST CALCULATED TOTAL OF ALL EXPENSES----------------------------


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





#---SHOWING CORRECT REMAINING AMOUNT ALL THE TIME: ----------------------------------------

    def on_text_calculating_NEW_REMAINING_AMOUNT(self):


        start_disposable_amount = float(self.ids.label_START_DISPOSABLE_AMOUNT.text)

        new_total_of_all_expenses = float(self.ids.label_TOTAL_OF_ALL_EXPENSES.text)


        new_remaining_amount = start_disposable_amount - new_total_of_all_expenses


        self.ids.label_REMAINING_AMOUNT.text = str(new_remaining_amount)






#--------------------------SAVING LAST CALCULATED REMAINING AMOUNT------------------------------

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

            ### """ ###
            #
            # Lav/brug en funktion til at læse/dumpe i json.filer

            total_of_paid_expenses_to_save = self.ids.label_TOTAL_OF_PAID_EXPENSES.text

            file_with_last_calculated_total_of_paid_expenses = \
                f"eb_a_created_budget_{current_budget}_TOTAL_OF_PAID_EXPENSES.json"

            with open(file_with_last_calculated_total_of_paid_expenses, "w") as file:
                json.dump(total_of_paid_expenses_to_save, file)



#---SHOWING CORRECT CURRENT DISPOSABLE AMOUNT ALL THE TIME: ----------------------------------------


    def on_text_calculating_NEW_CURRENT_DISPOSABLE_AMOUNT(self):


        start_disposable_amount = float(self.ids.label_START_DISPOSABLE_AMOUNT.text)


        new_total_of_paid_expenses = float(self.ids.label_TOTAL_OF_PAID_EXPENSES.text)


        new_current_disposable_amount = start_disposable_amount - new_total_of_paid_expenses


        self.ids.label_CURRENT_DISPOSABLE_AMOUNT.text = str(new_current_disposable_amount)




#---SAVING CURRENT DISPOSABLE AMOUNT----------------------


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

            ### """ ###
            #
            # Lav/brug en funktion til at læse/dumpe i json.filer

            current_disposable_amount_to_save = self.ids.label_CURRENT_DISPOSABLE_AMOUNT.text

            file_with_last_calculated_current_disposable_amount = f"eb_a_created_budget_{current_budget}_CURRENT_DISPOSABLE_AMOUNT.json"

            with open(file_with_last_calculated_current_disposable_amount, "w") as file:
                json.dump(current_disposable_amount_to_save, file)