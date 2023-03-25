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




class text_input_MULTIPLY(TextInput):


#---SETTING MAX CHARACTERS TO ENTER IN TEXT INPUT MULTIPLY
    max_characters = NumericProperty(4)


#---MAKING EXPENSE DISABLED OR NOT---------

    expense_DISABLED_OR_NOT = BooleanProperty(False)


    def __init__(self, expense_number, **kwargs):
        super(text_input_MULTIPLY, self).__init__(**kwargs)



        self.expense_number = expense_number


    #---WHEN APP IS OPENED: CHECKING IF EXPENSE SHOULD BE DISABLED------------

        file_telling_if_expense_should_be_disabled = f"expense_{self.expense_number}_state_DISABLED_OR_NOT.json"

        with open(file_telling_if_expense_should_be_disabled, "r") as file:
            disable_check = json.load(file)

        if disable_check == "True":

            self.expense_DISABLED_OR_NOT = True
        else:
            self.expense_DISABLED_OR_NOT = False



    #---WHEN APP IS OPENED: LAST ENTERED VALUE IN MULTIPLY-TEXT INPUT SHOWS--------

        file_with_last_entered_multiply_value = f"expense_{self.expense_number}_text_input_MULTIPLY.json"

        with open(file_with_last_entered_multiply_value, "r") as file:
            value_for_multiply_text_input = json.load(file)

        self.text = value_for_multiply_text_input






    def insert_text(self, substring, from_undo=False):
        if len(self.text) >= self.max_characters and self.max_characters > 0:
            substring = ""
        TextInput.insert_text(self, substring, from_undo)




#---IF NOTHING IS WRITTEN IN DISPOSABLE AMOUNT TEXT INPUT THE TEXT IN IN THE TEXT INPUT CHANGES TO A '0'

    def on_text_if_nothing_then_0_in_MULTIPLY_text_input(self):

        text_in_text_input = self.text

        if text_in_text_input == "":
            self.text = "1"

        if text_in_text_input == "0":
            self.text = "1"



#---SAVING TEXT INPUT OF MULTIPLY-VALUE--------------------

    def saving_text_input_MULTIPLY(self):

        value_to_save = self.text

        file_with_last_entered_value = f"expense_{self.expense_number}_text_input_MULTIPLY.json"

        with open(file_with_last_entered_value, "w") as file:
            json.dump(value_to_save, file)




    pass




class text_input_DIVIDE(TextInput):


#---SETTING MAX CHARACTERS TO ENTER IN TEXT INPUT MULTIPLY
    max_characters = NumericProperty(4)


#---MAKING EXPENSE DISABLED OR NOT---------

    expense_DISABLED_OR_NOT = BooleanProperty(False)


    def __init__(self, expense_number, **kwargs):
        super(text_input_DIVIDE, self).__init__(**kwargs)



        self.expense_number = expense_number


        #-------WHEN APP IS OPENED: CHECKING IF EXPENSE SHOULD BE DISABLED------------

        file_telling_if_expense_should_be_disabled = f"expense_{self.expense_number}_state_DISABLED_OR_NOT.json"

        with open(file_telling_if_expense_should_be_disabled, "r") as file:
            disable_check = json.load(file)

        if disable_check == "True":

            self.expense_DISABLED_OR_NOT = True
        else:
            self.expense_DISABLED_OR_NOT = False




    #---WHEN APP IS OPENED: LAST ENTERED VALUE IN MULTIPLY-TEXT INPUT SHOWS--------

        file_with_last_entered_divide_value = f"expense_{self.expense_number}_text_input_DIVIDE.json"

        with open(file_with_last_entered_divide_value, "r") as file:
            value_for_divide_text_input = json.load(file)

        self.text = value_for_divide_text_input





    def insert_text(self, substring, from_undo=False):
        if len(self.text) >= self.max_characters and self.max_characters > 0:
            substring = ""
        TextInput.insert_text(self, substring, from_undo)




#---IF NOTHING IS WRITTEN IN DISPOSABLE AMOUNT TEXT INPUT THE TEXT IN IN THE TEXT INPUT CHANGES TO A '0'

    def on_text_if_nothing_then_0_in_DIVIDE_text_input(self):

        text_in_text_input = self.text

        if text_in_text_input == "":
            self.text = "1"

        if text_in_text_input == "0":
            self.text = "1"



#---SAVING TEXT INPUT OF MULTIPLY-VALUE--------------------

    def saving_text_input_DIVIDE(self):

        value_to_save = self.text

        file_with_last_entered_value = f"expense_{self.expense_number}_text_input_DIVIDE.json"

        with open(file_with_last_entered_value, "w") as file:
            json.dump(value_to_save, file)




    pass









class text_input_AMOUNT(TextInput):

#---SETTING MAX CHARACTERS TO ENTER IN TEXT INPUT MULTIPLY
    max_characters = NumericProperty(12)


#---MAKING EXPENSE DISABLED OR NOT---------

    expense_DISABLED_OR_NOT = BooleanProperty(False)




#---WHEN APP IS OPENED: CHECKING IF EXPENSE SHOULD BE DISABLED------------

    def __init__(self, expense_number, **kwargs):
        super(text_input_AMOUNT, self).__init__(**kwargs)


        self.expense_number = expense_number



        file_telling_if_expense_should_be_disabled = f"expense_{self.expense_number}_state_DISABLED_OR_NOT.json"

        with open(file_telling_if_expense_should_be_disabled, "r") as file:
            disable_check = json.load(file)

        if disable_check == "True":

            self.expense_DISABLED_OR_NOT = True
        else:
            self.expense_DISABLED_OR_NOT = False



    #---WHEN APP IS OPENED: LAST ENTERED AMOUNT (IN AMOUNT TEXT INPUT) SHOWS--------

        file_with_amount = f"expense_{self.expense_number}_text_input_AMOUNT.json"

        with open(file_with_amount, "r") as file:
            text_to_show_in_amount = json.load(file)

        self.text = text_to_show_in_amount





#---OVERWRITING  insert_text FUNCTION SO THAT USER CAN ONLY ENTER AS MANY CHARACTERS AS GIVEN IN THE
#---NumericProperty(?)


    def insert_text(self, substring, from_undo=False):
        if len(self.text) >= self.max_characters and self.max_characters > 0:
            substring = ""
        TextInput.insert_text(self, substring, from_undo)



#---IF TEXT IS NOTHING:

    def on_text_if_nothing_then_0_in_AMOUNT_text_input(self):

        text_in_text_input = self.text

        if text_in_text_input == "":
            self.text = "0"





#---SAVING TEXT IN TEXT INPUT OF AMOUNT---------------------

    def saving_text_input_AMOUNT(self):

        value_to_save_in_amount = self.text

        file_with_amount = f"expense_{self.expense_number}_text_input_AMOUNT.json"

        with open(file_with_amount, "w") as file:
            json.dump(value_to_save_in_amount, file)


        pass





class text_input_DESCRIPTION(TextInput):

#---SETTING MAX CHARACTERS TO ENTER IN TEXT INPUT MULTIPLY
    max_characters = NumericProperty(22)


#---MAKING EXPENSE DISABLED OR NOT---------

    expense_DISABLED_OR_NOT = BooleanProperty(False)




    def __init__(self, expense_number, **kwargs):
        super(text_input_DESCRIPTION, self).__init__(**kwargs)


        self.expense_number = expense_number




    #---WHEN APP IS OPENED: CHECKING IF EXPENSE SHOULD BE DISABLED------------
        file_telling_if_expense_should_be_disabled = f"expense_{self.expense_number}_state_DISABLED_OR_NOT.json"

        with open(file_telling_if_expense_should_be_disabled, "r") as file:
            disable_check = json.load(file)

        if disable_check == "True":

            self.expense_DISABLED_OR_NOT = True
        else:
            self.expense_DISABLED_OR_NOT = False




    #---WHEN APP IS OPENED: LAST ENTERED DESCRIPTION (IN DESCRIPTION TEXT INPUT) SHOWS-------

        file_with_description = f"expense_{self.expense_number}_text_input_DESCRIPTION.json"

        with open(file_with_description, "r") as file:
            text_to_show_in_description = json.load(file)

        self.text = text_to_show_in_description



    def insert_text(self, substring, from_undo=False):
        if len(self.text) >= self.max_characters and self.max_characters > 0:
            substring = ""
        TextInput.insert_text(self, substring, from_undo)



#---SAVING TEXT IN TEXT INPUT OF DESCRIPTION---------------------

    def saving_text_input_DESCRIPTION(self):

        text_to_save = self.text

        file_to_save_description_in = f"expense_{self.expense_number}_text_input_DESCRIPTION.json"

        with open(file_to_save_description_in, "w") as file:
            json.dump(text_to_save, file)



    pass
















class expense_forms (RelativeLayout):


#---MAKING EXPENSE DISABLED OR NOT---------

    expense_DISABLED_OR_NOT = BooleanProperty(False)


    def __init__(self, expense_number, **kwargs):
        super(expense_forms, self).__init__(**kwargs)

        self.expense_number = expense_number




    #---ADDING TEXT INPUT MULTIPLY TO EXPENSE FORM

        # STORING TEXT INPUT WITH MULTIPLY VALUE IN A SELF.VARIABLE
        self.text_input_MULTIPLY = text_input_MULTIPLY(expense_number)

        self.add_widget(self.text_input_MULTIPLY)



    #---ADDING TEXT INPUT DIVIDE TO EXPENSE FORM
        # STORING TEXT INPUT WITH DIVIDE VALUE IN A SELF.VARIABLE

        self.text_input_DIVIDE = text_input_DIVIDE(expense_number)

        self.add_widget(self.text_input_DIVIDE)




    #---ADDING TEXT INPUT DESCRIPTION TO EXPENSE FORM

        # STORING TEXT INPUT WITH AMOUNT VALUE IN A SELF.VARIABLE
        self.text_input_DESCRIPTION = text_input_DESCRIPTION(expense_number)

        self.add_widget(self.text_input_DESCRIPTION)




    #---ADDING TEXT INPUT AMOUNT TO EXPENSE FORM

        # STORING TEXT INPUT WITH AMOUNT VALUE IN A SELF.VARIABLE
        self.text_input_AMOUNT = text_input_AMOUNT(expense_number)

        self.add_widget(self.text_input_AMOUNT)



    #---WHEN APP IS OPENED: CHECKING IF EXPENSE SHOULD BE DISABLED------------
        file_telling_if_expense_should_be_disabled = f"expense_{self.expense_number}_state_DISABLED_OR_NOT.json"

        with open(file_telling_if_expense_should_be_disabled, "r") as file:
            disable_check = json.load(file)

        if disable_check == "True":

            self.expense_DISABLED_OR_NOT = True
        else:
            self.expense_DISABLED_OR_NOT = False


#-------WHEN APP IS OPENED: LAST CALCULATED TOTAL AMOUNT (IN TOTAL AMOUNT LABEL) SHOWS---------

        file_with_amount = f"expense_{self.expense_number}_label_TOTAL_AMOUNT.json"

        with open(file_with_amount, "r") as file:
            value_to_show_in_total_amount = json.load(file)

        self.ids.label_TOTAL_AMOUNT.text = value_to_show_in_total_amount





#-------WHEN APP IS OPENED: CORRECT TEXT ON ENTER EXPENSE/EDIT EXPENSE BUTTON SHOWS-------

        file_with_text_for_enter_expense_or_edit_expense_button = \
            f"expense_{self.expense_number}_button_text_ENTER_EXPENSE_or_EDIT_EXPENSE.json"

        with open(file_with_text_for_enter_expense_or_edit_expense_button, "r") as file:
            text_for_enter_expense_or_edit_expense_button = json.load(file)

        self.ids.button_ENTER_EXPENSE_or_EDIT_EXPENSE.text = text_for_enter_expense_or_edit_expense_button










    def on_text_if_nothing_then_0_in_DIVIDE_text_input(self):

        text_in_text_input = self.ids.text_input_DIVIDE.text

        if text_in_text_input == "":
            self.ids.text_input_DIVIDE.text = "1"

        if text_in_text_input == "0":
            self.ids.text_input_DIVIDE.text = "1"









# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# -------------------SAVING TEXT AND DATA IN JSON-----------------------------
# ----------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------



















#---SAVING TEXT IN LABEL WITH TOTAL AMOUNT---------------------

    def saving_label_TOTAL_AMOUNT(self):

        value_to_save_in_total_amount = self.ids.label_TOTAL_AMOUNT.text

        file_with_amount = f"expense_{self.expense_number}_label_TOTAL_AMOUNT.json"

        with open(file_with_amount, "w") as file:
            json.dump(value_to_save_in_total_amount, file)




#---SAVING TEXT ON ENTER/EDIT EXPENSE BUTTON----------------------

    def saving_button_text_ENTER_or_EDIT_EXPENSE(self):

        text_on_button_to_save = self.ids.button_ENTER_EXPENSE_or_EDIT_EXPENSE.text

        file_for_text_on_enter_expense_or_edit_expense_button = \
            f"expense_{self.expense_number}_button_text_ENTER_EXPENSE_or_EDIT_EXPENSE.json"

        with open(file_for_text_on_enter_expense_or_edit_expense_button, "w") as file:
            json.dump(text_on_button_to_save, file)




#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
#----------FUNCTIONALITY OF WIDGET IN THE RELATIVE LAYOUT FOR EXPENSE FORMS----------
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


    # ---FUNCTIONS OF THE ARROWS------------------------------------------------------------------------

    def function_of_arrow_UP_MULTIPLY(self):

        value_to_multiply_expense_with = int(self.text_input_MULTIPLY.text)

        value_to_multiply_expense_with += 1

        self.text_input_MULTIPLY.text = str(value_to_multiply_expense_with)


    def function_of_arrow_DOWN_MULTIPLY(self):

        value_to_multiply_expense_with = int(self.text_input_MULTIPLY.text)

        value_to_multiply_expense_with -= 1

        self.text_input_MULTIPLY.text = str(value_to_multiply_expense_with)




    def function_of_arrow_UP_DIVIDE(self):

        value_to_divide_expense_with = int(self.text_input_DIVIDE.text)

        value_to_divide_expense_with += 1

        self.text_input_DIVIDE.text = str(value_to_divide_expense_with)





    def function_of_arrow_DOWN_DIVIDE(self):

        value_to_divide_expense_with = int(self.text_input_DIVIDE.text)

        value_to_divide_expense_with -= 1

        self.text_input_DIVIDE.text = str(value_to_divide_expense_with)







#--------------------------------------------------------------------------------------------------
#---FUNCTIONALITY OF ENTER EXPENSE(/EDIT EXPENSE)--------------------------------------------------


    def function_of_ENTER_EXPENSE_or_EDIT_EXPENSE(self):

    #---TEXT ON BUTTON BEFORE PRESS-------
        text_on_button = self.ids.button_ENTER_EXPENSE_or_EDIT_EXPENSE.text


    #---TOTAL AMOUNT OF EXPENSE------------

        value_to_multiply_amount_with = float(self.text_input_MULTIPLY.text)

        amount = float(self.text_input_AMOUNT.text)

        value_to_divide_amount_with = float(self.text_input_DIVIDE.text)

        total_amount_of_expense = value_to_multiply_amount_with * amount / value_to_divide_amount_with


    #---TOTAL OF ALL EXPENSES BEFORE EXPENSE IS ADDED OR SUBTRACTED--------------------

        total_of_all_expenses_before_expense_is_added_or_subtracted = \
            float(App.get_running_app().root.get_screen("screen_F").ids.label_TOTAL_OF_ALL_EXPENSES.text)




    #---END PRODUCT--------------TOTAL OF ALL EXPENSES PLUS EXPENSE--------------------------

        total_of_all_expenses_PLUS_expense= \
            str(total_of_all_expenses_before_expense_is_added_or_subtracted + total_amount_of_expense)



    #---END PRODUCT----------------TOTAL OF ALL EXPENSES MINUS EXPENSE--------------------------

        total_of_all_expenses_MINUS_expense = \
            str(total_of_all_expenses_before_expense_is_added_or_subtracted - total_amount_of_expense)




    #---REMAINING AMOUNT BEFORE EXPENSE 1 IS ADDED OR SUBTRACTED--------------------

        start_remaining_amount_before_expense_is_added_or_subtracted = \
            float(App.get_running_app().root.get_screen("screen_F").ids.label_REMAINING_AMOUNT.text)




    #---END PRODUCT----------CALCULATING REMAINING AMOUNT WHEN ENTER EXPENSE IS PRESSED-------------------

        remaining_amount_when_expense_is_added = \
            str(start_remaining_amount_before_expense_is_added_or_subtracted - total_amount_of_expense)




    #---END PRODUCT----------CALCULATING REMAINING AMOUNT WHEN EDIT EXPENSE IS PRESSED-------------------

        remaining_amount_when_expense_is_subtracted = \
            str(start_remaining_amount_before_expense_is_added_or_subtracted + total_amount_of_expense)





    #---WHAT HAPPENS WHEN ENTER/EDIT IS PRESSED DEPENDING ON WHETHER THE BUTTON SAYS "ENTER" OR "EDIT":



        if text_on_button == "Enter expense":



        #---CHANGING TEXT ON BUTTON-------------------

            self.ids.button_ENTER_EXPENSE_or_EDIT_EXPENSE.text = "Edit expense"



        #---DISABLING ALL (USER INPUT) WIDGETS IN EXPENSE and SAVING DISABLED STATE IN JSON-----

            # STORING TEXT INPUT IN A VARIABLE TO MAKE IT LOOK MORE SMOOTH WHEN USING THE expense_DISABLED_OR_NOT METHOD

            self.text_input_MULTIPLY.expense_DISABLED_OR_NOT = True

            self.text_input_DIVIDE.expense_DISABLED_OR_NOT = True

            self.text_input_DESCRIPTION.expense_DISABLED_OR_NOT = True

            self.text_input_AMOUNT.expense_DISABLED_OR_NOT = True

            self.text_input_DESCRIPTION.expense_DISABLED_OR_NOT = True


            self.expense_DISABLED_OR_NOT = True





            disabled_state_of_button = "True"

            file_with_state_of_button = f"expense_{self.expense_number}_state_DISABLED_OR_NOT.json"

            with open(file_with_state_of_button, "w") as file:
                json.dump(disabled_state_of_button, file)




        #---CACULATING TOTAL AMOUNT OF EXPENSE----------

            self.ids.label_TOTAL_AMOUNT.text = str(total_amount_of_expense)




        #---CALCULATING TOTAL OF ALL EXPENSES (ADDING EXPENSE TO TOTAL OF ALL EXPENSES)----------

            App.get_running_app().root.get_screen("screen_F").ids.label_TOTAL_OF_ALL_EXPENSES.text = \
                total_of_all_expenses_PLUS_expense




        #---CALCULATING REMAINING AMOUNT (WHEN ADDING EXPENSE TO TOTAL OF ALL EXPENSES)----------

            App.get_running_app().root.get_screen("screen_F").ids.label_REMAINING_AMOUNT.text = \
                remaining_amount_when_expense_is_added



        #---SAVING (enumeration, description, amount, division and total of) EXPENSE --------------

            id_of_expense = str(self.expense_number)


            enumeration_value = self.text_input_MULTIPLY.text

            description = self.text_input_DESCRIPTION.text

            amount = self.text_input_AMOUNT.text

            division_value = self.text_input_DIVIDE.text

            expense_in_total = self.ids.label_TOTAL_AMOUNT.text


            all_values = [enumeration_value, description, amount, division_value, expense_in_total]


            key_and_data_to_add_to_dictionary_in_json = {id_of_expense: all_values}


            file_with_saved_expenses = "eb_EXPENSES_of_the_budget_about_TO_BE_CREATED.json"


            with open(file_with_saved_expenses, "r") as file:
                dictionary_of_data_in_file = json.load(file)

            dictionary_of_data_in_file.update(key_and_data_to_add_to_dictionary_in_json)

            data_to_save_in_json_file = dictionary_of_data_in_file

            with open(file_with_saved_expenses, "w") as file:
                json.dump(data_to_save_in_json_file, file, indent=2)





#---!!!!!!!!!!!!!!!---TJEK OM ALT ER KORREKT HERUNDER OG STEMMER OVERNES MED RESTEN AF KODEN---!!!!!!!!!!!!!!!!!!!!!!!




        #---ENTERING EXPENSE ID IN JSON---------------------------------------

            file_with_ids_of_entered_expenses = "eb_IDS_of_ENTERED_EXPENSES_in_budget_about_TO_BE_CREATED.json"

            with open(file_with_ids_of_entered_expenses, "r") as file:
                list_of_ids = json.load(file)

                expense_id = int(self.expense_number)

                list_of_ids.append(expense_id)

            with open(file_with_ids_of_entered_expenses, "w") as file:
                json.dump(list_of_ids, file, indent=2)






        else:


        #---CHANGING TEXT ON BUTTON-------------------

            self.ids.button_ENTER_EXPENSE_or_EDIT_EXPENSE.text = "Enter expense"



        #---ENABLING ALL (USER INPUT) WIDGETS IN EXPENSE and SAVING ENABLED STATE IN JSON-----

            self.text_input_MULTIPLY.expense_DISABLED_OR_NOT = False

            self.text_input_DIVIDE.expense_DISABLED_OR_NOT = False

            self.text_input_DESCRIPTION.expense_DISABLED_OR_NOT = False


            self.text_input_AMOUNT.expense_DISABLED_OR_NOT = False

            self.text_input_DESCRIPTION.expense_DISABLED_OR_NOT = False


            self.expense_DISABLED_OR_NOT = False



            disabled_state_of_button = "False"

            file_with_state_of_button = f"expense_{self.expense_number}_state_DISABLED_OR_NOT.json"

            with open(file_with_state_of_button, "w") as file:
                json.dump(disabled_state_of_button, file)





        #---CALCULATING REMAINING AMOUNT (WHEN SUBTRACTING EXPENSE FROM TOTAL OF ALL EXPENSES)----------

            App.get_running_app().root.get_screen("screen_F").ids.label_REMAINING_AMOUNT.text = \
                remaining_amount_when_expense_is_subtracted



        #---CALCULATING TOTAL OF ALL EXPENSES (SUBTRACTING EXPENSE FROM TOTAL OF ALL EXPENSES)----------

            App.get_running_app().root.get_screen("screen_F").ids.label_TOTAL_OF_ALL_EXPENSES.text = \
                total_of_all_expenses_MINUS_expense



        #---RESETTING TOTAL AMOUNT OF EXPENSE----------

            self.ids.label_TOTAL_AMOUNT.text = "0"





        #---DELETING (enumeration, description, amount, division and total of) EXPENSE FROM FILE WITH SAVED EXPENSES

            file_with_saved_expenses = f"eb_EXPENSES_of_the_budget_about_TO_BE_CREATED.json"


            id_of_expense = self.expense_number


            key_to_data_to_remove = str(id_of_expense)


            with open(file_with_saved_expenses, "r") as file:
                dictionary_of_data_in_file = json.load(file)

            del dictionary_of_data_in_file[key_to_data_to_remove]

            data_to_save_in_json_file = dictionary_of_data_in_file

            with open(file_with_saved_expenses, "w") as file:
                json.dump(data_to_save_in_json_file, file, indent=2)




        #---DELETING EXPENSE ID FROM JSON WITH EXPENSE IDS-------------------------------

            file_with_ids_of_entered_expenses = "eb_IDS_of_ENTERED_EXPENSES_in_budget_about_TO_BE_CREATED.json"

            with open(file_with_ids_of_entered_expenses, "r") as file:
                list_of_ids = json.load(file)

                expense_id = int(self.expense_number)

                list_of_ids.remove(expense_id)

            with open(file_with_ids_of_entered_expenses, "w") as file:
                json.dump(list_of_ids, file, indent=2)








#--------------------------------------------------------------------------------------------------
#---FUNCTIONALITY OF CLEAR BUTTON------------------------------------------------------------------


    def function_CLEARING_INPUT_BOXES(self):



    #---TEXT ON ENTER/EDIT BUTTON BEFORE CLEAR BUTTON IS PRESSED---------------------------------------

        text_on_enter_or_edit_button_before_clear_is_pressed = \
            self.ids.button_ENTER_EXPENSE_or_EDIT_EXPENSE.text




    #---CALCULATING TOTAL OF ALL EXPENSES AS EXPENSE IS CLEARED - AND SHOWING NEW TOTAL OF ALL EXPENSES-----------

        total_of_expense_before_clearing = float(self.ids.label_TOTAL_AMOUNT.text)

        total_of_all_expenses_before_clearing = \
            float(App.get_running_app().root.get_screen("screen_F").ids.label_TOTAL_OF_ALL_EXPENSES.text)


        App.get_running_app().root.get_screen("screen_F").ids.label_TOTAL_OF_ALL_EXPENSES.text = \
            str(total_of_all_expenses_before_clearing - total_of_expense_before_clearing)



    #---CALCULATING REMAINING AMOUNT AS EXPENSE IS CLEARED - AND SHOWING NEW REMAINING AMOUNT-----------

        start_remaining_amount_before_clearing_expense_1 = \
            float(App.get_running_app().root.get_screen("screen_F").ids.label_REMAINING_AMOUNT.text)

        remaining_amount_when_expense_is_cleared = \
            str(start_remaining_amount_before_clearing_expense_1 + total_of_expense_before_clearing)



        App.get_running_app().root.get_screen("screen_F").ids.label_REMAINING_AMOUNT.text = \
            remaining_amount_when_expense_is_cleared




    #---CLEARING TEXT INPUT BOXES AND LABEL WITH TOTAL AMOUNT OF EXPENSE-----------

        self.text_input_MULTIPLY.text = "1"
        self.text_input_DIVIDE.text = "1"
        self.text_input_DESCRIPTION.text = "Description"
        self.text_input_AMOUNT.text = "0"

        self.ids.label_TOTAL_AMOUNT.text = "0"



    #---CHANGING STATE OF EXPENSE: FROM DISABLED TO ENABLED-----------------------

        self.text_input_MULTIPLY.expense_DISABLED_OR_NOT = False


        self.text_input_DIVIDE.expense_DISABLED_OR_NOT = False


        self.text_input_DESCRIPTION.expense_DISABLED_OR_NOT = False

        self.text_input_AMOUNT.expense_DISABLED_OR_NOT = False

        self.text_input_DESCRIPTION.expense_DISABLED_OR_NOT = False


        self.expense_DISABLED_OR_NOT = False





    #---SAVING STATE OF EXPENSE 1--------------------------------

        state_of_expense = "False"

        file_with_state_of_expense = f"expense_{self.expense_number}_state_DISABLED_OR_NOT.json"


        with open(file_with_state_of_expense, "w") as file:
            json.dump(state_of_expense, file)









    #---WHAT HAPPENS IF TEXT ON ENTER/EDIT EXPENSE BUTTON IS "ENTER" AND IF ITS "EDIT":


        if text_on_enter_or_edit_button_before_clear_is_pressed == "Edit expense":


        #---CHANGING TEXT ON BUTTON WHEN CLEAR IS PRESSED----------------

            self.ids.button_ENTER_EXPENSE_or_EDIT_EXPENSE.text = "Enter expense"



        #---DELETING (enumeration, description, amount, division and total of) EXPENSE FROM FILE WITH SAVED EXPENSES

            file_with_saved_expenses = f"eb_EXPENSES_of_the_budget_about_TO_BE_CREATED.json"


            id_of_expense = self.expense_number


            key_to_data_to_remove = str(id_of_expense)


            with open(file_with_saved_expenses, "r") as file:
                dictionary_of_data_in_file = json.load(file)

            del dictionary_of_data_in_file[key_to_data_to_remove]

            data_to_save_in_json_file = dictionary_of_data_in_file

            with open(file_with_saved_expenses, "w") as file:
                json.dump(data_to_save_in_json_file, file, indent=2)



        #---DELETING EXPENSE ID FROM JSON WITH EXPENSE IDS-------------------------------

            file_with_ids_of_entered_expenses = "eb_IDS_of_ENTERED_EXPENSES_in_budget_about_TO_BE_CREATED.json"

            with open(file_with_ids_of_entered_expenses, "r") as file:
                list_of_ids = json.load(file)

                expense_id = int(self.expense_number)

                list_of_ids.remove(expense_id)

            with open(file_with_ids_of_entered_expenses, "w") as file:
                json.dump(list_of_ids, file, indent=2)










#----------------------------------------------------------------------------------------------------
#---FUNCTIONALITY OF X BUTTON (IN THE CORNER) - REMOVING EXPENSE FORM--------------------------------




    def function_REMOVING_expense_FORM(self):

        widget_to_remove = self



    #---BEFORE ADDING NEW EXPENSE FORM: EXPANDING SIZE OF SCREEN TO SCROLL----------------------------------------

        App.get_running_app().root.get_screen("screen_F").size_hint_y_of_expenses_main_grid_frame -= .6



    #---BEFORE ADDING NEW EXPENSE FORM: LOWERING THE NEW EXPENSE BUTTON (MAKING ROOM FOR THE EXPENSE FORM)---------

        App.get_running_app().root.get_screen("screen_F").top_size_hint_grid_frame_for_NEW_EXPENSE_button += .0025



    #---BEFORE ADDING NEW EXPENSE FORM: LOWERING THE LABELS WITH THE RESULTS OF
    #---CALCULATIONS OF TOTAL OF ALL EXPENSES, REMAINING AMOUNT AND START AMOUNT
    #---(MAKING ROOM FOR THE EXPENSE FORM)-----------------------------------------------------------------------

        App.get_running_app().root.get_screen("screen_F").top_size_hint_grid_frame_for_THE_RESULTS += .0025





    #---DELETING EXPENSE ID NUMBER IN JSON FILE WITH LIST OF ID'S TO SHOW IN SCREEN D---------------

        expense_number_to_delete = self.expense_number

        file_with_list_of_current_expense_forms_in_screen_F = "eb_LIST_of_current_EXPENSE_FORMS_count.json"

        with open(file_with_list_of_current_expense_forms_in_screen_F, "r") as file:
            list_from_file = json.load(file)

        list_from_file.remove(expense_number_to_delete)

        with open(file_with_list_of_current_expense_forms_in_screen_F, "w") as file:
            json.dump(list_from_file, file)










    #---SUBTRACTING TOTAL OF EXPENSE FROM TOTAL OF ALL EXPENSES-------------------------

        total_of_expense_before_removing_expense_form = float(self.ids.label_TOTAL_AMOUNT.text)

        total_of_all_expenses_before_removing_expense_form = \
            float(App.get_running_app().root.get_screen("screen_F").ids.label_TOTAL_OF_ALL_EXPENSES.text)


        total_of_all_expenses_after_subtracting_total_of_expense = str(total_of_all_expenses_before_removing_expense_form - total_of_expense_before_removing_expense_form)




        start_remaining_amount_before_removing_expense_form = \
            float(App.get_running_app().root.get_screen("screen_F").ids.label_REMAINING_AMOUNT.text)

        remaining_amount_when_expense_form_is_removed = \
            str(start_remaining_amount_before_removing_expense_form + total_of_expense_before_removing_expense_form)


    #---CALCULATING TOTAL OF ALL EXPENSES AND REMAINING AMOUNT -
    #---DEPENDING ON WHETHER ENTER/EDIT BUTTON SAYS ENTER OR EDIT

        text_on_enter_or_edit_button_before_removing_expense_form = \
            self.ids.button_ENTER_EXPENSE_or_EDIT_EXPENSE.text



        if text_on_enter_or_edit_button_before_removing_expense_form == "Edit expense":


        #---SHOWING CORRECT TOTAL OF ALL EXPENSES AFTER REMOVING EXPENSE FORM---------------

            App.get_running_app().root.get_screen("screen_F").ids.label_TOTAL_OF_ALL_EXPENSES.text = \
                total_of_all_expenses_after_subtracting_total_of_expense


        #---SHOWING CORRECT REMAINING AMOUNT AFTER REMOVING EXPENSE FORM--------------------

            App.get_running_app().root.get_screen("screen_F").ids.label_REMAINING_AMOUNT.text = \
                remaining_amount_when_expense_form_is_removed




        #---REMOVING EXPENSE ID FROM JSON---------------------------------------

            file_with_ids_of_entered_expense = "eb_IDS_of_ENTERED_EXPENSES_in_budget_about_TO_BE_CREATED.json"

            with open(file_with_ids_of_entered_expense, "r") as file:
                list_of_ids = json.load(file)

                expense_number = self.expense_number

                list_of_ids.remove(expense_number)

            with open(file_with_ids_of_entered_expense, "w") as file:
                json.dump(list_of_ids, file, indent=2)



        #---DELETING (enumeration, description, amount, division and total of) EXPENSE FROM FILE WITH SAVED EXPENSES

            file_with_saved_expenses = f"eb_EXPENSES_of_the_budget_about_TO_BE_CREATED.json"

            id_of_expense = self.expense_number

            key_to_data_to_remove = str(id_of_expense)

            with open(file_with_saved_expenses, "r") as file:
                dictionary_of_data_in_file = json.load(file)

            del dictionary_of_data_in_file[key_to_data_to_remove]

            data_to_save_in_json_file = dictionary_of_data_in_file

            with open(file_with_saved_expenses, "w") as file:
                json.dump(data_to_save_in_json_file, file, indent=2)



    #---REMOVING JSON FILES CONNECTED TO THE EXPENSE:

        os.remove(f"expense_{self.expense_number}_button_text_ENTER_EXPENSE_OR_EDIT_EXPENSE.json")
        os.remove(f"expense_{self.expense_number}_label_TOTAL_AMOUNT.json")
        os.remove(f"expense_{self.expense_number}_state_DISABLED_OR_NOT.json")
        os.remove(f"expense_{self.expense_number}_text_input_AMOUNT.json")
        os.remove(f"expense_{self.expense_number}_text_input_DESCRIPTION.json")
        os.remove(f"expense_{self.expense_number}_text_input_MULTIPLY.json")
        os.remove(f"expense_{self.expense_number}_text_input_DIVIDE.json")




    #---REMOVING WIDGET--------------------------------------------------

        App.get_running_app().root.get_screen("screen_F").ids.grid_frame_for_expense_forms.remove_widget(widget_to_remove)


pass