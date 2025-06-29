
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


### """ ###
#
# HUSK class names med STORT forbogstav

class eb_budgets (RelativeLayout):


    def __init__(self, budget_id, **kwargs):
        super(eb_budgets, self).__init__(**kwargs)


        self.budget_id = budget_id


        file_with_budget_name_for_budget = f"eb_a_created_budget_{budget_id}_BUDGET_NAME.json"

        with open(file_with_budget_name_for_budget, "r") as file:
            budget_name = json.load(file)

        self.ids.label_BUDGET_NAME.text = budget_name




    def function_SEE_BUDGET(self):

        App.get_running_app().root.get_screen(
            "screen_J").size_hint_y_of_expenses_main_grid_frame = 3

        App.get_running_app().root.get_screen("screen_J").pos_hint_y_of_grid_for_new_final_expense_button = .994

        App.get_running_app().root.get_screen("screen_J").ids.grid_frame_for_all_expenses.clear_widgets()




        budget_id_for_current_budget_showing = self.budget_id



        file_for_id_of_current_budget_showing_in_screen_J = f"eb_CURRENT_BUDGET_showing.json"


        with open(file_for_id_of_current_budget_showing_in_screen_J, "w") as file:
            json.dump(budget_id_for_current_budget_showing, file)


        file_with_budget_name = f"eb_a_created_budget_{budget_id_for_current_budget_showing}_BUDGET_NAME.json"

        with open(file_with_budget_name, "r") as file:
            budget_name = json.load(file)

        App.get_running_app().root.get_screen("screen_J").ids.budget_name_in_top.text = budget_name





        file_with_start_disposable_amount = f"eb_a_created_budget_{budget_id_for_current_budget_showing}_DISPOSABLE_AMOUNT.json"

        with open(file_with_start_disposable_amount, "r") as file:
            disposable_amount = json.load(file)

            App.get_running_app().root.get_screen("screen_J").ids.label_START_DISPOSABLE_AMOUNT.text = disposable_amount





        file_with_total_of_all_expenses = f"eb_a_created_budget_{budget_id_for_current_budget_showing}_TOTAL_OF_ALL_EXPENSES.json"

        with open(file_with_total_of_all_expenses, "r") as file:
            total_of_all_expenses = json.load(file)

            App.get_running_app().root.get_screen("screen_J").ids.label_TOTAL_OF_ALL_EXPENSES.text = total_of_all_expenses







        file_with_remaining_amount = f"eb_a_created_budget_{budget_id_for_current_budget_showing}_REMAINING_AMOUNT.json"

        with open(file_with_remaining_amount, "r") as file:
            remaining_amount = json.load(file)

            App.get_running_app().root.get_screen("screen_J").ids.label_REMAINING_AMOUNT.text = remaining_amount








        file_with_total_of_paid_expenses = f"eb_a_created_budget_{budget_id_for_current_budget_showing}_TOTAL_OF_PAID_EXPENSES.json"

        with open(file_with_total_of_paid_expenses, "r") as file:
            total_of_paid_expenses = json.load(file)

            App.get_running_app().root.get_screen("screen_J").ids.label_TOTAL_OF_PAID_EXPENSES.text = total_of_paid_expenses







        #file_with_current_disposable_amount = f"eb_a_created_budget_{budget_id_for_current_budget_showing}_CURRENT_DISPOSABLE_AMOUNT.json"

        #with open(file_with_current_disposable_amount, "r") as file:
         #   current_disposable_amount = json.load(file)

          #  App.get_running_app().root.get_screen("screen_J").ids.label_CURRENT_DISPOSABLE_AMOUNT.text = current_disposable_amount







    #---SHOWING THE EXPENSES IN THE BUDGET


        # CREATING A LIST FOR SORTING KEYS IN THE DICTIONARY WITH ALL EXPENSES

        list_with_keys = []




        # LOADING DICTIONARY WITH THE EXPENSES OF THE BUDGET

        file_with_the_expenses_in_the_current_budget = f"eb_a_created_budget_{budget_id_for_current_budget_showing}_THE_EXPENSES.json"

        with open(file_with_the_expenses_in_the_current_budget, "r") as file:

            dictionary_with_multiply_description_etc = json.load(file)


            # APPENDING KEYS TO THE CREATED LIST WITH KEYS (list_with_keys=

            for key in dictionary_with_multiply_description_etc:



                the_key_to_append_to_list_to_order_keys_in = int(key)

                list_with_keys.append(the_key_to_append_to_list_to_order_keys_in)



        # SORTING THE KEYS FROM THE DICTIONARY SO THE EXPENSES EVENTUALLY WILL BE SHOWNED IN CORRECT ORDER:

        list_with_keys.sort()


        # CREATING VARIABLE WITH NEW DICTIONARY FOR EXPENSES SO THE EXPENSES FROM NOW ON WILL
        # BE IN ASCENDING ORDER IN THE FILE WITH THE DICTIONARY WITH EXPENSES (THIS SO IT DOESN'T HAVE
        # TO BE ORDERED EVERY TIME THE USER EDIT, DELETE OR ADD AN EXPENSE IN THE BUDGET)

        new_dictionary_with_expenses_in_ascending_order = {"0": "No expenses"}



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

                    App.get_running_app().root.get_screen(
                        "screen_J").pos_hint_y_of_grid_for_new_final_expense_button -= .0005

                    App.get_running_app().root.get_screen(
                        "screen_J").size_hint_y_of_expenses_main_grid_frame += .08

                    App.get_running_app().root.get_screen("screen_J").ids.grid_frame_for_all_expenses.add_widget\
                        (expenses_screen_J(key_with_expense_information, value_for_multiply_text_input,
                                        text_for_description, value_for_amount, value_for_divide,
                          value_for_total_amount))





                    # STORING ALL EXPENSE INFORMATION IN A LIST IN A VARIABLE SO IT KAN BE STORED IN A DICTIONARY IN A VARIABLE
                    # THAT CAN BE ADDED TO THE NEW DICTIONARY CREATED FOR STORING THE EXPENSES IN ASCENDING ORDER
                    # IN FILE WITH DICTIONARY WITH EXPENSES

                    all_expense_information = [value_for_multiply_text_input, text_for_description, value_for_amount,
                                               value_for_divide, value_for_total_amount]




                    # STORING EXPENSE KEY AND EXPENSE INFORMATION IN A DICTIONARY IN A VARIABLE SO IT KAN BE STORED IN
                    # THE NEW DICTIONARY CREATED FOR STORING THE EXPENSES IN ASCENDING ORDER IN FILE WITH
                    # DICTIONARY WITH EXPENSES

                    key_and_expense_information_for_new_dictionary = {key_with_expense_information: all_expense_information}


                    new_dictionary_with_expenses_in_ascending_order.update(key_and_expense_information_for_new_dictionary)



        with open (file_with_the_expenses_in_the_current_budget, "w") as file:
            json.dump(new_dictionary_with_expenses_in_ascending_order, file, indent= 2)








    def function_DELETING_BUDGET(self):

        widget_to_remove = self



    #---REMOVING ALL FILES CONNECTED ONLY TO THIS BUDGET (self): -------------

        file_with_expenses_of_budget = f"eb_a_created_budget_{self.budget_id}_THE_EXPENSES.json"

        with open(file_with_expenses_of_budget, "r") as file:
            dictionary_with_expenses = json.load(file)


            for key in dictionary_with_expenses:

                if key == "0":
                    pass

                else:

                    os.remove(f"eb_a_created_budget_{self.budget_id}_expense_{key}_BUTTON_text_PAID_OR_UNPAID.json")



        os.remove(f"eb_a_created_budget_{self.budget_id}_BUDGET_NAME.json")
        os.remove(f"eb_a_created_budget_{self.budget_id}_CURRENT_DISPOSABLE_AMOUNT.json")
        os.remove(f"eb_a_created_budget_{self.budget_id}_REMAINING_AMOUNT.json")
        os.remove(f"eb_a_created_budget_{self.budget_id}_DISPOSABLE_AMOUNT.json")
        os.remove(f"eb_a_created_budget_{self.budget_id}_THE_EXPENSES.json")
        os.remove(f"eb_a_created_budget_{self.budget_id}_TOTAL_OF_ALL_EXPENSES.json")
        os.remove(f"eb_a_created_budget_{self.budget_id}_TOTAL_OF_PAID_EXPENSES.json")



    #---RESETTING FILE WITH LIST OF BUDGET IDS:

        file_with_list_of_budget_ids = f"eb_LIST_of_BUDGET_IDS.json"

        with open(file_with_list_of_budget_ids, "r") as file:
            list_with_ids = json.load(file)

            id_of_the_budget_to_remove = int(self.budget_id)

            list_with_ids.remove(id_of_the_budget_to_remove)

            list_to_dump = list_with_ids

        with open(file_with_list_of_budget_ids, "w") as file:
            json.dump(list_to_dump, file)




    #---RESETTING FILE WITH CURRENT BUDGET SHOWING:

        file_with_id_of_current_budget = f"eb_CURRENT_BUDGET_showing.json"

        new_id_for_file_with_current_budget_id = 0

        with open(file_with_id_of_current_budget, "w") as file:
            json.dump(new_id_for_file_with_current_budget_id, file)





        App.get_running_app().root.get_screen("screen_I").ids.grid_frame_for_all_eb_budgets.remove_widget(
            widget_to_remove)









    pass