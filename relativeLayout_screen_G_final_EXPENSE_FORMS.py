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
from kivy.properties import ColorProperty
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


from text_input_screen_G_START_DISPOSABLE_AMOUNT import text_input_START_DISPOSABLE_AMOUNT




class Too_many_character_Popup(Popup):


    def __init__(self, expense_id, **kwargs):
        super(Too_many_character_Popup, self).__init__(**kwargs)

        self.expense_id = expense_id


        # LOADING ID OF CURRENT BUDGET SHOWING (SO THE CORRECT FILE WITH EXPENSES CAN BE LOADED)

        file_with_current_budget_showing = f"eb_CURRENT_BUDGET_showing.json"

        with open(file_with_current_budget_showing, "r") as file:
            self.budget_id = json.load(file)


    def close_pop_up(self):
        #edit_expense_POP_UP.ids.text_input_AMOUNT.do_undo()





        self.dismiss()

    pass


def function_deleting_elements_from_the_end_of_a_list_in_file(number_of_elements_to_delete, budget_id, expense_id, specifikation_name):


    filename = f"eb_a_created_budget_{budget_id}_expense_{expense_id}_{specifikation_name}.json"

    with open(filename, "r") as file:
        list_with_elements = json.load(file)

        for element in range(number_of_elements_to_delete):

            list_with_elements.pop()

    with open(filename, "w") as file:
        json.dump(list_with_elements, file)



def function_creating_file_with_regular_text (default_text_to_dumpt, budget_id, expense_id, specifikation_name):


    to_dump_in_file_as_default = f"{default_text_to_dumpt}"

    filename = f"eb_a_created_budget_{budget_id}_expense_{expense_id}_{specifikation_name}.json"

    with open(filename, "w") as file:
        json.dump(to_dump_in_file_as_default, file)




def function_creating_file_with_list (default_text_to_dumpt, budget_id, expense_id, specifikation_name):

    to_dump_in_file_as_default = default_text_to_dumpt

    filename = f"eb_a_created_budget_{budget_id}_expense_{expense_id}_{specifikation_name}.json"

    with open(filename, "w") as file:
        json.dump(to_dump_in_file_as_default, file)





def function_reading_file_with_regular_text (budget_id, expense_id, specifikation_name):

    filename = f"eb_a_created_budget_{budget_id}_expense_{expense_id}_{specifikation_name}.json"

    with open(filename, "r") as file:
        text_in_file = json.load(file)

    return text_in_file


def function_reading_file_with_list (budget_id, expense_id, specifikation_name):

    filename = f"eb_a_created_budget_{budget_id}_expense_{expense_id}_{specifikation_name}.json"

    with open(filename, "r") as file:
        list_in_file = json.load(file)

    return list_in_file




def function_tracking_on_text_characters_in_text_input(characters_in_text_input, budget_id, expense_id, specifikation_name):



    file_to_store_text_input_from_amount = f"eb_a_created_budget_{budget_id}_expense_{expense_id}_{specifikation_name}.json"

    with open(file_to_store_text_input_from_amount, "r") as file:
        list_with_characters = json.load(file)

        list_with_characters.append(characters_in_text_input)

    with open(file_to_store_text_input_from_amount, "w") as file:
        json.dump(list_with_characters, file)





def function_tracking_on_text_event(on_text_and_NAME_of_widget, budget_id, expense_id):

    last_event = on_text_and_NAME_of_widget


    file_with_updating_last_text_input_event = f"eb_a_created_budget_{budget_id}_expense_{expense_id}_AMOUNT_last_event.json"


    with open(file_with_updating_last_text_input_event, "r") as file:
        list_with_events = json.load(file)

        list_with_events.append(last_event)

    with open(file_with_updating_last_text_input_event, "w") as file:
        json.dump(list_with_events, file)










class edit_expense_POP_UP (Popup):

    background_color_of_text_input_MULTIPLY = ColorProperty((.2, .2, .2, .2))
    background_color_of_text_input_DIVIDE = ColorProperty((.2, .2, .2, .2))
    background_color_of_text_input_AMOUNT = ColorProperty((.2, .2, .2, .2))
    background_color_of_text_input_DESCRIPTION = ColorProperty((.2, .2, .2, .2))


    def __init__(self, expense_id, **kwargs):
        super(edit_expense_POP_UP, self).__init__(**kwargs)




        self.expense_id = expense_id


        self.has_text_been_pasted_in = False



        self.list_with_events = []
        self.list_with_characters = []



        self.list_storing_arrow_press = ["No"]




    #---SHOWING THE EXPENSE (INFORMATION IN THE TEXT INPUT BOXES AND LABEL WIDGET WHICH IS) SHOWING IN THE POP UP
    #---THAT POPS UP WHEN THE "EDIT" BUTTON IS PRESSED:


        # LOADING ID OF CURRENT BUDGET SHOWING (SO THE CORRECT FILE WITH EXPENSES CAN BE LOADED)

        file_with_current_budget_showing = f"eb_CURRENT_BUDGET_showing.json"

        with open(file_with_current_budget_showing, "r") as file:
            self.budget_id = json.load(file)




        # LOADING DICITIONARY WITH EXPENSES OF THE BUDGET SHOWING (USING BUDGET ID LOADED JUST BEFORE)

        file_with_expense_information = f"eb_a_created_budget_{self.budget_id}_THE_EXPENSES.json"

        with open(file_with_expense_information, "r") as file:
            dictionary_with_expenses = json.load(file)



            # FETCHING THE CORRECT LIST WITH EXPENSE INFORMATION OF THE EXPENSE THE USER IS ABOUT TO EDIT
            # THE self.expense_id IS THE KEY OF THE CORRECT LIST OF EXPENSE INFORMATION

            list_with_expense_information = dictionary_with_expenses[self.expense_id]



            multiply_value = list_with_expense_information[0]

            description = list_with_expense_information[1]

            amount = list_with_expense_information[2]

            divide_value = list_with_expense_information[3]

            total_amount = list_with_expense_information[4]













        # SHOWING THE EXPENSE INFORMATION IN THE POP UP



        self.ids.text_input_MULTIPLY.text = multiply_value

        self.ids.text_input_DIVIDE.text = divide_value

        self.ids.text_input_DESCRIPTION.text = description

        self.ids.text_input_AMOUNT.text = amount


        self.ids.label_TOTAL_AMOUNT.text = total_amount






#-------------------------------------------------------
#-------------------------------------------------------
#----------------FUNCTIONS/METHODS----------------------
#-------------------------------------------------------
#-------------------------------------------------------









    def on_focus_tracking_if_text_input_DESCRIPTION_was_last_in_focus(self):

        function_creating_file_with_regular_text("DESCRIPTION_in_focus", self.budget_id, self.expense_id, "text_input_IN_FOCUS")



    def on_focus_tracking_if_text_input_AMOUNT_was_last_in_focus(self):

        function_creating_file_with_regular_text("AMOUNT_in_focus", self.budget_id, self.expense_id,
                                                     "text_input_IN_FOCUS")


    def on_focus_tracking_if_text_input_MULTIPLY_was_last_in_focus(self):

        function_creating_file_with_regular_text("MULTIPLY_in_focus", self.budget_id, self.expense_id,
                                                     "text_input_IN_FOCUS")



    def on_focus_tracking_if_text_input_DIVIDE_was_last_in_focus(self):

        function_creating_file_with_regular_text("DIVIDE_in_focus", self.budget_id, self.expense_id,
                                                     "text_input_IN_FOCUS")







    def on_release_do_UNDO(self):


        text_input_in_focus = function_reading_file_with_regular_text(self.budget_id, self.expense_id, "text_input_IN_FOCUS")



        if text_input_in_focus == "AMOUNT_in_focus":

            self.ids.text_input_AMOUNT.do_undo()


        if text_input_in_focus == "DESCRIPTION_in_focus":

            self.ids.text_input_DESCRIPTION.do_undo()


        if text_input_in_focus == "MULTIPLY_in_focus":

            self.ids.text_input_MULTIPLY.do_undo()


        if text_input_in_focus == "DIVIDE_in_focus":

            self.ids.text_input_DIVIDE.do_undo()




    def on_release_do_REDO(self):


        text_input_in_focus = function_reading_file_with_regular_text(self.budget_id, self.expense_id, "text_input_IN_FOCUS")



        if text_input_in_focus == "AMOUNT_in_focus":

            self.ids.text_input_AMOUNT.do_redo()


        if text_input_in_focus == "DESCRIPTION_in_focus":

            self.ids.text_input_DESCRIPTION.do_redo()


        if text_input_in_focus == "MULTIPLY_in_focus":

            self.ids.text_input_MULTIPLY.do_redo()


        if text_input_in_focus == "DIVIDE_in_focus":

            self.ids.text_input_DIVIDE.do_redo()




    def on_text_warning_to_many_CHARACTERS_in_text_input_MULTIPLY(self):

        # Storing text in TextInput (to 1: track it and to 2: control how many characters can be entered)
        characters_in_text_input = self.ids.text_input_MULTIPLY.text

        if len(characters_in_text_input) < 4:

            self.background_color_of_text_input_MULTIPLY = (.2, .2, .2, .2)

        else:
            self.background_color_of_text_input_MULTIPLY = (1, 0, 0, .4)





    def on_text_warning_to_many_CHARACTERS_in_text_input_DIVIDE(self):

        # Storing text in TextInput (to 1: track it and to 2: control how many characters can be entered)
        characters_in_text_input = self.ids.text_input_DIVIDE.text

        if len(characters_in_text_input) < 4:

            self.background_color_of_text_input_DIVIDE = (.2, .2, .2, .2)

        else:
            self.background_color_of_text_input_DIVIDE = (1, 0, 0, .4)







    def on_text_warning_to_many_CHARACTERS_in_text_input_DESCRIPTION(self):

        # Storing text in TextInput (to 1: track it and to 2: control how many characters can be entered)
        characters_in_text_input = self.ids.text_input_DESCRIPTION.text

        if len(characters_in_text_input) < 20:

            self.background_color_of_text_input_DESCRIPTION = (.2, .2, .2, .2)

        else:
            self.background_color_of_text_input_DESCRIPTION = (1, 0, 0, .4)







    def on_text_warning_to_many_CHARACTERS_in_text_input_AMOUNT(self):


        # Storing text in TextInput (to 1: track it and to 2: control how many characters can be entered)
        characters_in_text_input = self.ids.text_input_AMOUNT.text


        if len(characters_in_text_input) < 15:

            self.background_color_of_text_input_AMOUNT = (.2, .2, .2, .2)

        else:
            self.background_color_of_text_input_AMOUNT = (1, 0, 0, .4)










    def function_CALCULATING_TOTAL_AMOUNT_when_on_text_MULTIPLY(self):



    #---CALCULATING TOTAL AMOUNT

        multiply_text_input = self.ids.text_input_MULTIPLY.text

        if multiply_text_input == "" or self.ids.text_input_AMOUNT.text == "":
            pass

        else:

            if self.ids.text_input_DIVIDE.text == "":

                self.ids.text_input_DIVIDE.text = "1"


            # LOADING MULTIPLY VALUE AND MAKING IT A FLOAT
            multiply_value_to_save = float(self.ids.text_input_MULTIPLY.text)

            # LOADING AMOUNT VALUE AND MAKING IT A FLOAT

            amount_to_save = float(self.ids.text_input_AMOUNT.text)


            # LOADING DIVIDE VALUE AND MAKING IT A FLOAT
            divide_value_to_save = float(self.ids.text_input_DIVIDE.text)

            # CALCULATING TOTAL AMOUNT OF EXPENSE
            calculated_total_amount = multiply_value_to_save * amount_to_save / divide_value_to_save

            self.ids.label_TOTAL_AMOUNT.text = str(calculated_total_amount)






    def function_CALCULATING_TOTAL_AMOUNT_when_on_text_DIVIDE(self):


        # ---CALCULATING TOTAL AMOUNT

        divide_text_input = self.ids.text_input_DIVIDE.text

        if divide_text_input == "" or self.ids.text_input_AMOUNT.text == "":
            pass

        else:

            if self.ids.text_input_MULTIPLY.text == "":
                self.ids.text_input_MULTIPLY.text = "1"


            # LOADING MULTIPLY VALUE AND MAKING IT A FLOAT
            multiply_value_to_save = float(self.ids.text_input_MULTIPLY.text)

            # LOADING AMOUNT VALUE AND MAKING IT A FLOAT

            amount_to_save = float(self.ids.text_input_AMOUNT.text)

            # LOADING DIVIDE VALUE AND MAKING IT A FLOAT
            divide_value_to_save = float(self.ids.text_input_DIVIDE.text)

            # CALCULATING TOTAL AMOUNT OF EXPENSE
            calculated_total_amount = multiply_value_to_save * amount_to_save / divide_value_to_save

            self.ids.label_TOTAL_AMOUNT.text = str(calculated_total_amount)





    def function_CALCULATING_TOTAL_AMOUNT_when_on_text_AMOUNT(self):





    #---CALCULATING TOTAL AMOUNT

        amount_text_input = self.ids.text_input_AMOUNT.text

        if amount_text_input == "":
            self.ids.label_TOTAL_AMOUNT.text = "0"

        else:

            if self.ids.text_input_DIVIDE.text == "":

                self.ids.text_input_DIVIDE.text = "1"

            if self.ids.text_input_MULTIPLY.text == "":

                self.ids.text_input_MULTIPLY.text = "1"

            # LOADING MULTIPLY VALUE AND MAKING IT A FLOAT
            multiply_value_to_save = float(self.ids.text_input_MULTIPLY.text)

            # LOADING AMOUNT VALUE AND MAKING IT A FLOAT

            amount_to_save = float(self.ids.text_input_AMOUNT.text)

            # LOADING DIVIDE VALUE AND MAKING IT A FLOAT
            divide_value_to_save = float(self.ids.text_input_DIVIDE.text)

            # CALCULATING TOTAL AMOUNT OF EXPENSE
            calculated_total_amount = multiply_value_to_save * amount_to_save / divide_value_to_save

            self.ids.label_TOTAL_AMOUNT.text = str(calculated_total_amount)







#--------------------------------------------------------------------------------------------------
#---FUNCTIONS OF THE ARROWS------------------------------------------------------------------------

    def function_of_arrow_UP_MULTIPLY(self):


        is_arrow_pressed = "Yes"

        self.list_storing_arrow_press.append(is_arrow_pressed)



        value_to_multiply_expense_with = int(self.ids.text_input_MULTIPLY.text)

        value_to_multiply_expense_with += 1

        self.ids.text_input_MULTIPLY.text = str(value_to_multiply_expense_with)











    def function_of_arrow_DOWN_MULTIPLY(self):

        value_to_multiply_expense_with = int(self.ids.text_input_MULTIPLY.text)

        value_to_multiply_expense_with -= 1

        self.ids.text_input_MULTIPLY.text = str(value_to_multiply_expense_with)





    def function_of_arrow_UP_DIVIDE(self):

        value_to_divide_expense_with = int(self.ids.text_input_DIVIDE.text)

        value_to_divide_expense_with += 1

        self.ids.text_input_DIVIDE.text = str(value_to_divide_expense_with)





    def function_of_arrow_DOWN_DIVIDE(self):

        value_to_divide_expense_with = int(self.ids.text_input_DIVIDE.text)

        value_to_divide_expense_with -= 1

        self.ids.text_input_DIVIDE.text = str(value_to_divide_expense_with)






    def function_ENTER_EXPENSE(self):


    #----------------------------
    #---PREPERATION COMMANDS:----
    #----------------------------



    #---EXPENSE INFORMATION TO SAVE:

        multiply_value_to_save = self.ids.text_input_MULTIPLY.text
        description_to_save = self.ids.text_input_DESCRIPTION.text
        amount_to_save = self.ids.text_input_AMOUNT.text
        divide_value_to_save = self.ids.text_input_DIVIDE.text


        total_amount_to_save = self.ids.label_TOTAL_AMOUNT.text




    #---LOADING DICTIONARY WITH EXPENSES OF THE BUDGET SHOWING (USING BUDGET ID LOADED JUST BEFORE)

        file_with_expense_information = f"eb_a_created_budget_{self.budget_id}_THE_EXPENSES.json"

        with open(file_with_expense_information, "r") as file:
            dictionary_with_expenses = json.load(file)

            the_dictionary_with_all_expenses = dictionary_with_expenses



    #---CLEARING SCREEN J (AND SCREEN G) SO A UPDATED LIST OF EXPENSES CAN BE SHOWN


            App.get_running_app().root.get_screen("screen_G").ids.grid_frame_for_all_expenses.clear_widgets()


            for key in the_dictionary_with_all_expenses:

                if key == "0":
                    pass

                else:

                    App.get_running_app().root.get_screen("screen_G") \
                        .pos_hint_y_of_grid_for_new_final_expense_button += .0005






    #---------------------------------------------
    #---SHOWING AND SAVING CHANGES----------------
    #---------------------------------------------


    #---CALCULATING AND SHOWING CHANGES IN TOTAL OF EXPENSES


            # - CALCULATING TOTAL OF ALL EXPENSES WITHOUT THE EDITED EXPENSE:



            # STORING TOTAL OF ALL EXPENSES BEFORE THIS EXPENSE (self.expense_id) IS EDITTED

            the_total_of_all_expenses_before_expenses_is_edited = \
                float(App.get_running_app().root.get_screen("screen_G").ids.label_TOTAL_OF_ALL_EXPENSES.text)


            # LOADING THE TOTAL OF THIS EXPENSE (self.expense_id) BEFORE IT IS EDITED
            # AND STORING IT IN A VARIABLE

            list_with_expense_information = dictionary_with_expenses[self.expense_id]

            the_total_of_expense_before_it_is_edited = float(list_with_expense_information[4])




            # CALCULATING THE TOTAL OF ALL EXPENSES WITHOUT THIS EXPENSE (self.expense_id)

            the_total_of_all_expenses_without_the_expense_about_to_be_edited = \
                the_total_of_all_expenses_before_expenses_is_edited - the_total_of_expense_before_it_is_edited



            # CALCULATING THE NEW TOTAL OF ALL EXPENSES - THAT IS: WITH THE NEW TOTAL OF THIS EXPENSE (self.expense_id)

            expense_amount_to_add_to_total_of_expenses = float(total_amount_to_save)

            calculation_of_total_of_expenses = the_total_of_all_expenses_without_the_expense_about_to_be_edited + expense_amount_to_add_to_total_of_expenses



            # SHOWING THE NEW TOTAL OF ALL EXPENSES



            App.get_running_app().root.get_screen("screen_G").ids.label_TOTAL_OF_ALL_EXPENSES.text = str(
                calculation_of_total_of_expenses)






        #---SAVING CHANGES IN JSON FILES:


            # STORING LIST WITH EXPENSE INFORMATION (FROM DICTIONARY) IN A VARIABLE

            list_with_expense_information_to_update = dictionary_with_expenses[self.expense_id]



            # CLEARING LIST SO NEW EXPENSE INFORMATION CAN BE APPENDED

            list_with_expense_information_to_update.clear()



            # APPENDING NEW EXPENSE INFORMATION

            list_with_expense_information_to_update.append(multiply_value_to_save)

            list_with_expense_information_to_update.append(description_to_save)

            list_with_expense_information_to_update.append(amount_to_save)

            list_with_expense_information_to_update.append(divide_value_to_save)

            list_with_expense_information_to_update.append(total_amount_to_save)







            # STORING EXPENSE ID AS KEY FOR DICTIONARY TO UPDATE:

            key = self.expense_id

            # STORING KEY AND LIST WITH EXPENSE INFORMATION IN A VARIABLE SO THE DICTIONARY WITH EXPENSES
            # CAN BE UPDATED

            key_and_list_with_expense_information = {key: list_with_expense_information_to_update}








            # UPDATING DICTIONARY WITH EXPENSES

            dictionary_with_expenses.update(key_and_list_with_expense_information)



            dictionary_for_json_file = dictionary_with_expenses





            # DUMPING UPDATED DICTIONARY WITH EXPENSE INFORMATION IN JSON FILE

            with open(file_with_expense_information, "w") as file:
                json.dump(dictionary_for_json_file, file, indent= 2)












    #---SHOWING EXPENSES WITH THE CHANGES IN THIS (self.expense_id) EXPENSE:




        # CREATING A LIST FOR SORTING KEYS IN THE DICTIONARY WITH ALL EXPENSES

        list_with_keys = []



        # LOADING DICTIONARY WITH THE EXPENSES OF THE BUDGET

        file_with_the_expenses_in_the_current_budget = f"eb_a_created_budget_{self.budget_id}_THE_EXPENSES.json"

        with open(file_with_the_expenses_in_the_current_budget, "r") as file:

            dictionary_with_multiply_description_etc = json.load(file)

            # APPENDING KEYS TO THE CREATED LIST list_with_keys

            for key in dictionary_with_multiply_description_etc:
                the_key_to_append_to_list_to_order_keys_in = int(key)

                list_with_keys.append(the_key_to_append_to_list_to_order_keys_in)




        # SORTING THE KEYS FROM THE DICTIONARY SO THE EXPENSES EVENTUALLY WILL BE SHOWNED IN CORRECT ORDER:

        list_with_keys.sort()




        # FOR LOOPING LIST WITH KEYS AND LOADING EXPENSES FROM DICTIONARY

        for key in list_with_keys:

            if key == 0:
                pass

            else:

                key_with_expense_information = str(key)

                # LOADING DICTIONARY WITH EXPENSES
                with open(file_with_the_expenses_in_the_current_budget, "r") as file:
                    dict_with_multiply_description_etc = json.load(file)

                    # LOADING LIST (CONTAINING EXPENSE INFORMATION) FROM DICTIONARY USING KEYS FROM
                    # THE ORDERED LIST WITH KEYS: list_with_keys

                    list_with_multiply_description_etc = dict_with_multiply_description_etc[
                        key_with_expense_information]

                    # LOADING AND STORING THE DIFFERENT EXPENSE INFORMATIONS IN VARIABLES - THAT IS:
                    # THE MULTIPLY VALUE IS LOADED FROM THE LIST IN DICTIONARY AND STORED IN A VARIABLE
                    # AND SO ON

                    value_for_multiply_text_input = list_with_multiply_description_etc[0]

                    text_for_description = list_with_multiply_description_etc[1]

                    value_for_amount = list_with_multiply_description_etc[2]

                    value_for_divide = list_with_multiply_description_etc[3]

                    value_for_total_amount = list_with_multiply_description_etc[4]

                    # EXPENSES ARE ADDED TO THE GRID FRAME FOR EXPENSES IN SCREEN J - THAT IS: EXPENSES ARE SHOWN
                    # IN SCREEN J
                    # AND:
                    # EXPENSE ID ARE PASSED AS key_with_expense_information TO THE final_expense CLASS, SO THAT
                    # THE EDIT BUTTON CAN OPEN A POP WITH CORRECT EXPENSE INFORMATION AND SAVE THE CHANGES IN CORRECT
                    # FILES








                App.get_running_app().root.get_screen("screen_G")\
                    .pos_hint_y_of_grid_for_new_final_expense_button -= .0005


                App.get_running_app().root.get_screen("screen_G").ids.grid_frame_for_all_expenses.add_widget \
                    (final_expenses(key_with_expense_information, value_for_multiply_text_input,
                                    text_for_description,
                                    value_for_amount, value_for_divide,
                                    value_for_total_amount))





    #---CLOSING POP UP WITH EXPENSE
        self.dismiss()












    def function_REMOVING_EXPENSE_FROM_BUDGET(self):



    #---PREPARATION: CLEARING SCREEN G FOR EXPENSES AND RAISING POS_HINT_Y OF GRID FRAME FOR "NEW EXPENSE" BUTTON:


        # LOADING DICTIONARY WITH EXPENSES OF THE BUDGET SHOWING (USING BUDGET ID LOADED JUST BEFORE)

        file_with_expenses = f"eb_a_created_budget_{self.budget_id}_THE_EXPENSES.json"

        with open(file_with_expenses, "r") as file:
            dictionary_with_expenses = json.load(file)




            # CLEARING SCREEN G SO A UPDATED LIST OF EXPENSES CAN BE SHOWN

            App.get_running_app().root.get_screen("screen_G").ids.grid_frame_for_all_expenses.clear_widgets()


            # RAISING POS_HINT_Y OF GRID FRAME FOR "NEW EXPENSE" BUTTON

            App.get_running_app().root.get_screen("screen_G").pos_hint_y_of_grid_for_new_final_expense_button = .994






    #---UPDATING TOTAL OF ALL EXPENSES, REMAINING EXPENSES, TOTAL OF PAID EXPENSES AND CURRENT DISPOSABLE AMOUNT
    #---(BY UPDATING TOTAL OF ALL EXPENSES AND TOTAL OF PAID EXPENSES. THE REST IS DONE BY THE FUNCTIONS:
    #---on_text_calculating_NEW_RAMINING_AMOUNT - AND - on_text_calculating_NEW_CURRENT_DISPOSABLE_AMOUNT
    #---IN SCREEN G



        # - UPDATING TOTAL OF ALL EXPENSES


            # TOTAL OF ALL EXPENSES BEFORE EXPENSE IS REMOVED

            total_of_all_expenses_before_expense_is_removed = \
                float(App.get_running_app().root.get_screen("screen_G").ids.label_TOTAL_OF_ALL_EXPENSES.text)


            # TOTAL OF EXPENSE TO BE REMOVED BEFORE "EDIT" BUTTON WAS PRESSED


                # STORING EXPENSE ID IN VARIABLE TO BE USED AS KEY TO FETCHING THE LIST WITH EXPENSE INFORMATION
                # (EVENTUALLY TO GET THE VALUE OF THE TOTAL AMOUNT OF EXPENSE)

            key_for_expense_in_dictionary = str(self.expense_id)



                # STORING LIST WITH EXPENSE INFORMATION (FROM DICTIONARY WITH EXPENSES) IN A VARIABLE

            list_with_expense_information = dictionary_with_expenses[key_for_expense_in_dictionary]



                # STORING TOTAL AMOUNT OF EXPENSE IN VARIBALE

            total_of_expense_to_be_removed = float(list_with_expense_information[4])



            # CALCULATING NEW TOTAL OF ALL EXPENSES:

            new_total_of_all_expenses = total_of_all_expenses_before_expense_is_removed - total_of_expense_to_be_removed



            # SHOWING NEW TOTAL OF ALL EXPENSES IN SCREEN G

            App.get_running_app().root.get_screen("screen_G").ids.label_TOTAL_OF_ALL_EXPENSES.text = str(new_total_of_all_expenses)







        # - UPDATING TOTAL OF PAID EXPENSES


            # LOADING TEXT ON PAID OR UNPAID BUTTON (BECAUSE TOTAL OF PAID EXPENSES ONLY NEEDS TO BE CALCULATED IF
            # THE TEXT ON THE BUTTON "P" - THAT IS: IF THE EXPENSES IS PAID

            file_with_text_on_PAID_OR_UNPAID_button = \
                f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_BUTTON_text_PAID_OR_UNPAID.json"

            with open (file_with_text_on_PAID_OR_UNPAID_button, "r") as file:
                text_on_PAID_OR_UNPAID_button = json.load(file)




            # A IF STATEMENT MAKING SURE TOTAL OF PAID EXPENSES IS ONLY RECALCULATED IF THE TEXT ON THE PAID OR UNPAID
            # BUTTON IS PRESSED

            if text_on_PAID_OR_UNPAID_button == "unP":
                pass

            else:


            # TOTAL OF PAID EXPENSES BEFORE EXPENSE IS REMOVED

                total_of_paid_expenses_before_expense_is_removed = \
                    float(App.get_running_app().root.get_screen("screen_G").ids.label_TOTAL_OF_PAID_EXPENSES.text)




                # TOTAL OF EXPENSE TO BE REMOVED BEFORE "EDIT" BUTTON WAS PRESSED

                    # STORING EXPENSE ID IN VARIABLE TO BE USED AS KEY TO FETCHING THE LIST WITH EXPENSE INFORMATION
                    # (EVENTUALLY TO GET THE VALUE OF THE TOTAL AMOUNT OF EXPENSE)

                key_for_expense_in_dictionary = str(self.expense_id)



                    # STORING LIST WITH EXPENSE INFORMATION (FROM DICTIONARY WITH EXPENSES) IN A VARIABLE

                list_with_expense_information = dictionary_with_expenses[key_for_expense_in_dictionary]



                    # STORING TOTAL AMOUNT OF EXPENSE IN VARIBALE

                total_of_expense_to_be_removed = float(list_with_expense_information[4])




                # CALCULATING NEW TOTAL OF PAID EXPENSES:

                new_total_of_paid_expenses = total_of_paid_expenses_before_expense_is_removed - total_of_expense_to_be_removed




                # SHOWING NEW TOTAL OF ALL EXPENSES IN SCREEN G

                App.get_running_app().root.get_screen("screen_G").ids.label_TOTAL_OF_PAID_EXPENSES.text = str(
                    new_total_of_paid_expenses)










        #---DELETING THE EXPENSE FROM FILE WITH DICTIONARY WITH EXPENSES AND FROM SCREEN G


            # STORING EXPENSE ID IN VARIABLE:

            expense_id = str(self.expense_id)



            # DELETING THE EXPENSE FROM DICTIONARY WITH EXPENSES

            del dictionary_with_expenses[expense_id]



            # LOWERING/REPOSITIONING THE POS_HINT_Y OF GRID FRAME FOR NEW EXPENSE BUTTON (IT WAS RAISED WHEN
            # "NEW EXPENSE" BUTTON WAS PRESSED - IT WAS PREPARATION FOR THE BUTTON TO BE LOWERED TO CORRECT
            # POSITION IF ALL EXPENSES WITH THE NEW EXPENSE WHERE TO BE ADDED TO THE GRID FRAME FOR ALL EXPENSES,
            # THAT IS: IF THE "ENTER EXPENSE" BUTTON WAS TO BE PRESSED)

            for key in dictionary_with_expenses:

                if key == "0":

                    pass


                else:

                    # STORING LIST WITH EXPENSE INFORMATION OF (EVERY) EXPENSE (KEY) IN A VARIABLE
                    list_with_multiply_description_etc = dictionary_with_expenses[key]



                    # LOADING AND STORING THE DIFFERENT EXPENSE INFORMATIONS IN VARIABLES - THAT IS:
                    # THE MULTIPLY VALUE IS LOADED FROM THE LIST IN DICTIONARY AND STORED IN A VARIABLE
                    # AND SO ON

                    value_for_multiply_text_input = list_with_multiply_description_etc[0]

                    text_for_description = list_with_multiply_description_etc[1]

                    value_for_amount = list_with_multiply_description_etc[2]

                    value_for_divide = list_with_multiply_description_etc[3]

                    value_for_total_amount = list_with_multiply_description_etc[4]





                    # REPOSITIONING GRID FRAME WITH "NEW EXPENSE" BUTTON:

                    App.get_running_app().root.get_screen("screen_G"). \
                        pos_hint_y_of_grid_for_new_final_expense_button -= .0005


                    #final_expenses = App.get_running_app().root.get_screen("screen_G").final_expenses(key, value_for_multiply_text_input,
                     #                      text_for_description,
                      #                     value_for_amount, value_for_divide,
                       #                    value_for_total_amount)

                    App.get_running_app().root.get_screen("screen_G").ids.grid_frame_for_all_expenses.add_widget \
                        (final_expenses(key, value_for_multiply_text_input,
                                           text_for_description,
                                           value_for_amount, value_for_divide,
                                           value_for_total_amount))





            # DUMPING DICTIONARY WITHOUT THE EXPENSE CREATED WHEN "NEW EXPENSE" BUTTON WAS PRESSED

            dictionary_with_expense_deleted = dictionary_with_expenses



        with open(file_with_expenses, "w") as file:
            json.dump(dictionary_with_expense_deleted, file, indent=2)






    #---REMOVING FILE WITH TEXT ON PAID OR UNPAID BUTTON

        os.remove(f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_BUTTON_text_PAID_OR_UNPAID.json")




        # CLOSING POP UP WITH NEW EXPENSE FORM

        self.dismiss()






    def function_CLOSE_edit_expense_pop_up(self):

        self.dismiss()












class final_expenses (RelativeLayout):


    multiply_in_screen = StringProperty("")
    amount_in_screen = StringProperty("")
    division_in_screen = StringProperty("")


    def __init__(self, expense_id, multiply, description, amount, divide, total_of_expense, **kwargs):
        super(final_expenses, self).__init__(**kwargs)






        self.expense_id = expense_id

        self.multiply = multiply
        self.description = description
        self.amount = amount
        self.divide = divide
        self.total_of_expense = total_of_expense



        self.text_input_START_DISPOSABLE_AMOUNT = text_input_START_DISPOSABLE_AMOUNT()




        file_with_current_budget = f"eb_CURRENT_BUDGET_showing.json"

        with open(file_with_current_budget) as file:
            self.budget_id = json.load(file)



        if self.does_the_json_file_exists\
                    (f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_BUTTON_text_PAID_OR_UNPAID.json"):


            file_with_saved_text_on_paid_or_unpaid_button = \
                f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_BUTTON_text_PAID_OR_UNPAID.json"

            with open(file_with_saved_text_on_paid_or_unpaid_button, "r") as file:
                text_for_button = json.load(file)



                self.ids.button_text_PAID_OR_UNPAID.text = text_for_button

                if text_for_button == "unP":

                    self.ids.button_text_PAID_OR_UNPAID.background_color = (0, 0, 0, .8)

                else:

                    self.ids.button_text_PAID_OR_UNPAID.background_color = (0, .7, .5, 1)





        else:

            current_text_on_button = "unP"

            filename_of_file_to_create_to_save_text_un_paid_or_unpaid_button = \
                f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_BUTTON_text_PAID_OR_UNPAID.json"

            with open(filename_of_file_to_create_to_save_text_un_paid_or_unpaid_button, "w") as file:
                json.dump(current_text_on_button, file)




        self.ids.label_DESCRIPTION.text = description

        self.multiply_in_screen = self.multiply

        self.amount_in_screen = self.amount

        self.division_in_screen = self.divide



        self.ids.label_TOTAL_OF_EXPENSE.text = total_of_expense





    def function_EDIT_EXPENSE(self):

        function_creating_file_with_regular_text("False", self.budget_id, self.expense_id,
                                                 "AMOUNT_too_many_char")

        list_for_last_entered_in_AMOUNT = []

        function_creating_file_with_list(list_for_last_entered_in_AMOUNT, self.budget_id, self.expense_id, "AMOUNT_last_entered_text")

        function_creating_file_with_regular_text("No", self.budget_id, self.expense_id, "UNDO_pressed_or_not")



        #is_UNDO_pressed_as_last_event = "No"

        #file_controlling_if_undo_button_has_been_pressed = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_UNDO_pressed_or_not.json"

        #with open(file_controlling_if_undo_button_has_been_pressed, "w") as file:
         #   json.dump(is_UNDO_pressed_as_last_event, file)



        list_with_events = []

        function_creating_file_with_list(list_with_events, self.budget_id, self.expense_id, "AMOUNT_last_event")

        #file_with_updating_last_text_input_event = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_AMOUNT_last_event.json"

        #with open(file_with_updating_last_text_input_event, "w") as file:
         #   json.dump(list_with_events, file)



        # CREATING AF FILE WHERE LAST TEXT IN TEXT INPUT FOR AMOUNT IS STORED. THIS IS FOR THE ON_TEXT FUNCTION MAKING
        # SURE YOU CAN'T ENTER MORE THAN 12 CHARACTERS IN THE TEXT INPUT

        list_for_last_text_in_text_input_amount = []

        function_creating_file_with_list(list_for_last_text_in_text_input_amount, self.budget_id, self.expense_id, "AMOUNT_limited")

        #file_with_last_text_in_text_input_amount = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_AMOUNT_limited.json"

        #with open(file_with_last_text_in_text_input_amount, "w") as file:
         #   json.dump(list_for_last_text_in_text_input_amount, file)


        list_for_selected_text = []

        function_creating_file_with_list(list_for_selected_text, self.budget_id, self.expense_id,
                               "AMOUNT_saved_selected")



        #file_with_saved_selected_text = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_AMOUNT_saved_selected.json"

        #with open(file_with_saved_selected_text, "w") as file:
         #   json.dump(list_for_selected_text, file)




        # STORING THE POPUP CLASS FOR EDIT EXPENSE (THAT IS: THE POPUP WITH THE EDIT EXPENSE FORM SHOWING WHEN
        # "EDIT EXPENSE" BUTTON IS PRESSED

        self.the_edit_expense_pop_up = edit_expense_POP_UP(self.expense_id)



        # OPENING THE POPUP WITH THE EDIT EXPENSE FORM

        self.the_edit_expense_pop_up.open()




    def does_the_json_file_exists(self, fileAndPath):
        return os.path.exists(fileAndPath)













    def function_PAID_OR_UNPAID(self):

        print(App.get_running_app().root.get_screen("screen_G").dictionary_with_expense_forms)

        text_on_paid_or_unpaid_button = self.ids.button_text_PAID_OR_UNPAID.text


        if text_on_paid_or_unpaid_button == "unP":


            # CHANGING COLOR OF BUTTON

            self.ids.button_text_PAID_OR_UNPAID.background_color = (0, .7, .5, 1)



            # CHANGING TEXT ON BUTTON

            self.ids.button_text_PAID_OR_UNPAID.text = "P"



            # TOTAL OF PAID EXPENSES BEFORE PAID/UNPAID BUTTON IS PRESSED

            total_of_paid_expenses_before_paid_or_unpaid_button_is_pressed = \
                float(App.get_running_app().root.get_screen("screen_G").ids.label_TOTAL_OF_PAID_EXPENSES.text)



            # TOTAL OF THIS EXPENSE (self.expense_id) BEFORE OR AS THE BUTTON IS PRESSED

            total_of_this_expense_as_paid_or_unpaid_button_is_pressed = float(self.total_of_expense)




            # CALCULATING TOTAL OF PAID EXPENSES AFTER BUTTON IS PRESSED

            total_of_paid_expenses_after_paid_or_unpaid_button_is_pressed = \
                total_of_paid_expenses_before_paid_or_unpaid_button_is_pressed + \
                total_of_this_expense_as_paid_or_unpaid_button_is_pressed





            # START DISPOSABLE AMOUNT

            start_disposable_amount = \
                float(self.text_input_START_DISPOSABLE_AMOUNT.text)




            # CALCULATING CURRENT DISPOSABLE AMOUNT

            current_disposable_amount_after_button_is_pressed = \
                start_disposable_amount - total_of_this_expense_as_paid_or_unpaid_button_is_pressed



            # SHOWING TOTAL PAID EXPENSES IN SCREEN G AND SCREEN J

            App.get_running_app().root.get_screen("screen_G").ids.label_TOTAL_OF_PAID_EXPENSES.text = \
                str(total_of_paid_expenses_after_paid_or_unpaid_button_is_pressed)








            # SAVING TEXT ON BUTTON
            current_text_on_button = "P"

            filename_of_file_to_create_to_save_text_un_paid_or_unpaid_button = \
                f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_BUTTON_text_PAID_OR_UNPAID.json"



            with open(filename_of_file_to_create_to_save_text_un_paid_or_unpaid_button, "w") as file:
                json.dump(current_text_on_button, file)



        else:

            self.ids.button_text_PAID_OR_UNPAID.background_color = (0, 0, 0, .8)

            self.ids.button_text_PAID_OR_UNPAID.text = "unP"



            total_of_paid_expenses_before_paid_or_unpaid_button_is_pressed = \
                float(App.get_running_app().root.get_screen("screen_G").ids.label_TOTAL_OF_PAID_EXPENSES.text)



            total_of_this_expense_as_paid_or_unpaid_button_is_pressed = float(self.total_of_expense)

            total_of_paid_expenses_after_paid_or_unpaid_button_is_pressed = \
                total_of_paid_expenses_before_paid_or_unpaid_button_is_pressed - \
                total_of_this_expense_as_paid_or_unpaid_button_is_pressed




            App.get_running_app().root.get_screen("screen_G").ids.label_TOTAL_OF_PAID_EXPENSES.text = \
                str(total_of_paid_expenses_after_paid_or_unpaid_button_is_pressed)






            # SAVING TEXT ON BUTTON

            current_text_on_button = "unP"

            filename_of_file_to_create_to_save_text_un_paid_or_unpaid_button = \
                f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_BUTTON_text_PAID_OR_UNPAID.json"

            with open(filename_of_file_to_create_to_save_text_un_paid_or_unpaid_button, "w") as file:
                json.dump(current_text_on_button, file)









    pass
