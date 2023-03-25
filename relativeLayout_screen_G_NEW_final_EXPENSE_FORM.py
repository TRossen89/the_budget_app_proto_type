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

from relativeLayout_screen_G_final_EXPENSE_FORMS import final_expenses



class text_input_screen_G_new_expense_MULTIPLY(TextInput):


    max_characters = NumericProperty(4)


    def __init__(self, expense_id, **kwargs):
        super(text_input_screen_G_new_expense_MULTIPLY, self).__init__(**kwargs)

        self.expense_id = expense_id



    #---SHOWING THE EXPENSE (INFORMATION IN THE TEXT INPUT BOXES AND LABEL WIDGET WHICH IS) SHOWING IN THE POP UP
    #---THAT POPS UP WHEN THE "EDIT" BUTTON IS PRESSED:


        # LOADING ID OF CURRENT BUDGET SHOWING (SO THE CORRECT FILE WITH EXPENSES CAN BE LOADED)

        file_with_current_budget_showing = f"eb_CURRENT_BUDGET_showing.json"

        with open(file_with_current_budget_showing, "r") as file:
            self.budget_id = json.load(file)




        # LOADING DICTIONARY WITH EXPENSES OF THE BUDGET SHOWING (USING BUDGET ID LOADED JUST BEFORE)

        file_with_expense_information = f"eb_a_created_budget_{self.budget_id}_THE_EXPENSES.json"

        with open(file_with_expense_information, "r") as file:
            dictionary_with_expenses = json.load(file)



            # FETCHING THE CORRECT LIST WITH EXPENSE INFORMATION OF THE EXPENSE THE USER IS ABOUT TO EDIT
            # THE self.expense_id IS THE KEY OF THE CORRECT LIST OF EXPENSE INFORMATION

            list_with_expense_information = dictionary_with_expenses[self.expense_id]




            # STORING THE EXPENSE INFORMATION IN VARIABLES

            multiply_value = list_with_expense_information[0]



        # SHOWING THE EXPENSE INFORMATION IN THE POP UP

        self.text = multiply_value




    def insert_text(self, substring, from_undo=False):
        if len(self.text) >= self.max_characters and self.max_characters > 0:
            substring = ""
        TextInput.insert_text(self, substring, from_undo)




    #---IF NOTHING IS WRITTEN IN DISPOSABLE AMOUNT TEXT INPUT THE TEXT IN THE TEXT INPUT CHANGES TO A '0'


    def on_text_if_nothing_then_0_in_MULTIPLY_text_input(self):

        text_in_text_input = self.text

        if text_in_text_input == "":
            self.text = "1"

        if text_in_text_input == "0":
            self.text = "1"





    def function_CALCULATING_TOTAL_AMOUNT_when_on_text_MULTIPLY(self):



        # ---CALCULATING TOTAL AMOUNT

        multiply_text_input = self.text

        if multiply_text_input == "":
            pass

        else:

            # LOADING MULTIPLY VALUE AND MAKING IT A FLOAT
            multiply_value_to_save = float(self.text)

            # LOADING AMOUNT VALUE AND MAKING IT A FLOAT

            amount_to_save = float(App.get_running_app().root.get_screen("screen_G").
                                   text_input_with_new_final_expense_button.new_final_expense_form.text_input_AMOUNT.text)



            # LOADING DIVIDE VALUE AND MAKING IT A FLOAT
            divide_value_to_save = float(App.get_running_app().root.get_screen("screen_G").
                                   text_input_with_new_final_expense_button.new_final_expense_form.text_input_DIVIDE.text)



            # CALCULATING TOTAL AMOUNT OF EXPENSE
            calculated_total_amount = multiply_value_to_save * amount_to_save / divide_value_to_save

            App.get_running_app().root.get_screen("screen_G").\
                text_input_with_new_final_expense_button.new_final_expense_form.ids.label_TOTAL_AMOUNT.text = str(calculated_total_amount)



    pass











class text_input_screen_G_new_expense_DIVIDE(TextInput):

    max_characters = NumericProperty(4)

    def __init__(self, expense_id, **kwargs):
        super(text_input_screen_G_new_expense_DIVIDE, self).__init__(**kwargs)


        self.expense_id = expense_id




        # ---SHOWING THE EXPENSE (INFORMATION IN THE TEXT INPUT BOXES AND LABEL WIDGET WHICH IS) SHOWING IN THE POP UP
        # ---THAT POPS UP WHEN THE "EDIT" BUTTON IS PRESSED:

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



            # STORING THE EXPENSE INFORMATION IN VARIABLES

            divide_value = list_with_expense_information[3]



        # SHOWING THE EXPENSE INFORMATION IN THE POP UP

        self.text = divide_value



    def insert_text(self, substring, from_undo=False):
        if len(self.text) >= self.max_characters and self.max_characters > 0:
            substring = ""
        TextInput.insert_text(self, substring, from_undo)



    def on_text_if_nothing_then_0_in_DIVIDE_text_input(self):

        text_in_text_input = self.text

        if text_in_text_input == "":
            self.text = "1"

        if text_in_text_input == "0":
            self.text = "1"





    def function_CALCULATING_TOTAL_AMOUNT_when_on_text_DIVIDE(self):

        # ---CALCULATING TOTAL AMOUNT OF EXPENSE

        divide_text_input = self.text

        if divide_text_input == "":
            pass

        else:

            # LOADING MULTIPLY VALUE AND MAKING IT A FLOAT
            multiply_value_to_save = float(App.get_running_app().root.get_screen("screen_G").
                                   text_input_with_new_final_expense_button.new_final_expense_form.text_input_MULTIPLY.text)




            # LOADING AMOUNT VALUE AND MAKING IT A FLOAT
            amount_to_save = float(App.get_running_app().root.get_screen("screen_G").
                                   text_input_with_new_final_expense_button.new_final_expense_form.text_input_AMOUNT.text)

            # LOADING DIVIDE VALUE AND MAKING IT A FLOAT
            divide_value_to_save = float(self.text)

            # CALCULATING TOTAL AMOUNT OF EXPENSE
            calculated_total_amount = multiply_value_to_save * amount_to_save / divide_value_to_save

            if amount_to_save == 0:
                pass

            else:
                App.get_running_app().root.get_screen("screen_G").text_input_with_new_final_expense_button.\
                    new_final_expense_form.ids.label_TOTAL_AMOUNT.text = str(calculated_total_amount)



















class text_input_screen_G_new_expense_DESCRIPTION(TextInput):

    max_characters = NumericProperty(22)


    def __init__(self, expense_id, **kwargs):
        super(text_input_screen_G_new_expense_DESCRIPTION, self).__init__(**kwargs)

        self.expense_id = expense_id



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



            # STORING THE EXPENSE INFORMATION IN VARIABLES

            description = list_with_expense_information[1]



        # SHOWING THE EXPENSE INFORMATION IN THE POP UP

        self.text = description



    def insert_text(self, substring, from_undo=False):
        if len(self.text) >= self.max_characters and self.max_characters > 0:
            substring = ""
        TextInput.insert_text(self, substring, from_undo)










class text_input_screen_G_new_expense_AMOUNT(TextInput):


    max_characters = NumericProperty(12)


    def __init__(self, expense_id, **kwargs):
        super(text_input_screen_G_new_expense_AMOUNT, self).__init__(**kwargs)

        self.expense_id = expense_id



        # ---SHOWING THE EXPENSE (INFORMATION IN THE TEXT INPUT BOXES AND LABEL WIDGET WHICH IS) SHOWING IN THE POP UP
        # ---THAT POPS UP WHEN THE "EDIT" BUTTON IS PRESSED:

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




            # STORING THE EXPENSE INFORMATION IN VARIABLES

            amount = list_with_expense_information[2]



        # SHOWING THE EXPENSE INFORMATION IN THE POP UP

        self.text = amount




    def insert_text(self, substring, from_undo=False):
        if len(self.text) >= self.max_characters and self.max_characters > 0:
            substring = ""
        TextInput.insert_text(self, substring, from_undo)




    def on_text_if_nothing_then_0_in_AMOUNT_text_input(self):

        text_in_text_input = self.text

        if text_in_text_input == "":
            self.text = "0"





    def function_CALCULATING_TOTAL_AMOUNT_when_on_text_AMOUNT(self):

        # ---CALCULATING TOTAL AMOUNT OF EXPENSE

        # LOADING TEXT FROM THE TextInput THAT THIS FUNCTION IS CONNECTED TO (THROUGH on_text)
        # THIS IS TO AVOID ERROR WHEN THERE IS NOTHING IN THE TextInput BOX (FOR EXAMPLE BECAUSE
        # THE USER HAS DELETED THE TEXT TO WRITE NEW TEXT)

        amount_text_input = self.text

        # IF STATEMENT THAT SAYS THE FUNCTION SHOULDN'T DO ANYTHING IF THERE IS
        # NO TEXT IN THE TEXT INPUT.
        # THIS IS TO AVOID ERROR WHEN THERE IS NO TEXT IN THE TEXT INPUT

        if amount_text_input == "":
            pass


        else:

            # LOADING MULTIPLY VALUE AND MAKING IT A FLOAT

            multiply_value_to_save = float(App.get_running_app().root.get_screen("screen_G").
                                           text_input_with_new_final_expense_button.new_final_expense_form.text_input_MULTIPLY.text)


            # LOADING AMOUNT VALUE AND MAKING IT A FLOAT
            amount_to_save = float(self.text)

            # LOADING DIVIDE VALUE AND MAKING IT A FLOAT
            divide_value_to_save = float(App.get_running_app().root.get_screen("screen_G").
                                         text_input_with_new_final_expense_button.new_final_expense_form.text_input_DIVIDE.text)

            # CALCULATING TOTAL AMOUNT OF EXPENSE
            calculated_total_amount = multiply_value_to_save * amount_to_save / divide_value_to_save


            if self.text == "0":
                pass

            else:
                # SHOWING CALCULATED TOTAL AMOUNT IN LABEL WITH TOTAL AMOUNT OF EXPENSE
                App.get_running_app().root.get_screen("screen_G").text_input_with_new_final_expense_button.\
                    new_final_expense_form.ids.label_TOTAL_AMOUNT.text = str(calculated_total_amount)











class new_final_expense_POP_UP (Popup):

    def __init__(self, expense_id, **kwargs):
        super(new_final_expense_POP_UP, self).__init__(**kwargs)

        self.expense_id = expense_id



        # STORING TEXT INPUT CLASSES IN SELF.VARIABLE
        self.text_input_MULTIPLY = text_input_screen_G_new_expense_MULTIPLY(expense_id)
        self.text_input_DIVIDE = text_input_screen_G_new_expense_DIVIDE(expense_id)
        self.text_input_AMOUNT = text_input_screen_G_new_expense_AMOUNT(expense_id)
        self.text_input_DESCRIPTION = text_input_screen_G_new_expense_DESCRIPTION(expense_id)


        # ADDING TEXT INPUT TO THE LAYOUT IN THE POP UP SO THEY ARE SHOWING
        self.ids.relative_layout_for_new_expense_form.add_widget(self.text_input_MULTIPLY)
        self.ids.relative_layout_for_new_expense_form.add_widget(self.text_input_DIVIDE)
        self.ids.relative_layout_for_new_expense_form.add_widget(self.text_input_AMOUNT)
        self.ids.relative_layout_for_new_expense_form.add_widget(self.text_input_DESCRIPTION)



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



            # STORING THE EXPENSE INFORMATION IN VARIABLES

            total_amount = list_with_expense_information[4]



        # SHOWING THE EXPENSE INFORMATION IN THE POP UP

        self.ids.label_TOTAL_AMOUNT.text = total_amount








    # --------------------------------------------------------------------------------------------------
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



















    def function_ENTER_EXPENSE(self):



    # ----------------------------
    # ---PREPERATION COMMANDS:----
    # ----------------------------


    #---EXPENSE INFORMATION TO SAVE:

        multiply_value_to_save = self.text_input_MULTIPLY.text
        description_to_save = self.text_input_DESCRIPTION.text
        amount_to_save = self.text_input_AMOUNT.text
        divide_value_to_save = self.text_input_DIVIDE.text

        total_amount_to_save = self.ids.label_TOTAL_AMOUNT.text



    #---LOADING DICTIONARY WITH EXPENSES OF THE BUDGET SHOWING (USING BUDGET ID LOADED JUST BEFORE)

        file_with_expense_information = f"eb_a_created_budget_{self.budget_id}_THE_EXPENSES.json"

        with open(file_with_expense_information, "r") as file:
            dictionary_with_expenses = json.load(file)





    #---CLEARING SCREEN J (AND SCREEN G) SO THE UPDATED LIST OF EXPENSES CAN BE SHOWN





        App.get_running_app().root.get_screen("screen_G").ids.grid_frame_for_all_expenses.clear_widgets()





        # ---------------------------------------------
        # ---SHOWING AND SAVING CHANGES----------------
        # ---------------------------------------------


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





        # ---SAVING CHANGES IN JSON FILES:

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
            json.dump(dictionary_for_json_file, file, indent=2)




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



                    # POSITION OF GRID FRAME FOR NEW (FINALD) EXPENSE BUTTON IN SCREEN G AND J ARE LOWERED SO THERE
                    # IS ROOM FOR EXPENSES:

                    App.get_running_app().root.get_screen("screen_G") \
                        .pos_hint_y_of_grid_for_new_final_expense_button -= .0005









                    # EXPENSES ARE ADDED TO THE GRID FRAME FOR EXPENSES IN SCREEN J - THAT IS: EXPENSES ARE SHOWN
                    # IN SCREEN J
                    # AND:
                    # EXPENSE ID ARE PASSED AS key_with_expense_information TO THE final_expense CLASS, SO THAT
                    # THE EDIT BUTTON CAN OPEN A POP WITH CORRECT EXPENSE INFORMATION AND SAVE THE CHANGES IN CORRECT
                    # FILES

                    self.final_expenses = final_expenses(key_with_expense_information, value_for_multiply_text_input,
                                        text_for_description,
                                        value_for_amount, value_for_divide,
                                        value_for_total_amount)

                    App.get_running_app().root.get_screen("screen_G").ids.grid_frame_for_all_expenses.add_widget(self.final_expenses)



        # ---CLOSING POP UP WITH EXPENSE
        self.dismiss()























    def function_CLOSE_edit_expense_pop_up(self):



    #---DELETING THE EXPENSE THAT WAS CREATED WHEN THE "NEW EXPENSE" BUTTON WAS PRESSED



        # LOADING ID OF CURRENT BUDGET SHOWING TO FIND THE FILE WITH THE EXPENSES IN THE BUDGET SHOWING

        file_with_id_of_current_budget_showing = f"eb_CURRENT_BUDGET_showing.json"

        with open(file_with_id_of_current_budget_showing, "r") as file:
            current_budget_showing = json.load(file)




        # LOADING FILE WITH EXPENSES (LAST INSERTED EXPENSE WAS THE EXPENSE CREATED WHEN "NEW EXPENSE" BUTTON
        # WAS PRESSED. THE EXPENSE INFORMATION WAS: 1 - Description - 0 - 1 - 0)

        file_with_expenses = f"eb_a_created_budget_{current_budget_showing}_THE_EXPENSES.json"

        with open(file_with_expenses, "r") as file:
            dictionary_with_expenses = json.load(file)



            # DELETING LAST INSERTED ITEM

            dictionary_with_expenses.popitem()




            # LOWERING/REPOSITIONING THE POS_HINT_Y OF GRID FRAME FOR NEW EXPENSE BUTTON (IT WAS RAISED WHEN
            # "NEW EXPENSE" BUTTON WAS PRESSED - IT WAS PREPARATION FOR THE BUTTON TO BE LOWERED TO CORRECT
            # POSITION IF ALL EXPENSES WITH THE NEW EXPENSE WHERE TO BE ADDED TO THE GRID FRAME FOR ALL EXPENSES,
            # THAT IS: IF THE "ENTER EXPENSE" BUTTON WAS TO BE PRESSED)

            for key in dictionary_with_expenses:

                if key == "0":

                    pass


                else:

                    # REPOSITIONING GRID FRAME WITH "NEW EXPENSE" BUTTON:

                    App.get_running_app().root.get_screen("screen_G"). \
                        pos_hint_y_of_grid_for_new_final_expense_button -= .0005



        # DUMPING DICTIONARY WITHOUT THE EXPENSE CREATED WHEN "NEW EXPENSE" BUTTON WAS PRESSED

            dictionary_with_latest_expense_deleted = dictionary_with_expenses

        with open(file_with_expenses, "w") as file:
            json.dump(dictionary_with_latest_expense_deleted, file, indent=2)



        # CLOSING POP UP WITH NEW EXPENSE FORM

        self.dismiss()





















class NEW_final_EXPENSE_button(RelativeLayout):




    def function_NEW_final_EXPENSE_POP_UP_form(self):

        file_with_id_of_current_budget_showing = f"eb_CURRENT_BUDGET_showing.json"

        with open(file_with_id_of_current_budget_showing, "r") as file:
            current_budget_showing = json.load(file)




        list_for_expense_ids_to_count = []


        file_with_expenses = f"eb_a_created_budget_{current_budget_showing}_THE_EXPENSES.json"

        with open(file_with_expenses, "r") as file:
            dictionary_with_expenses = json.load(file)


            for key in dictionary_with_expenses:

                if key == "0":

                    expense_id_for_list_with_ids_to_count = int(key)

                    list_for_expense_ids_to_count.append(expense_id_for_list_with_ids_to_count)



                else:

                    expense_id_for_list_with_ids_to_count = int(key)

                    list_for_expense_ids_to_count.append(expense_id_for_list_with_ids_to_count)



                    # PREPARING POSITION OF GRID FRAME WITH NEW FINAL EXPENSE BUTTON:

                    App.get_running_app().root.get_screen("screen_G").\
                        pos_hint_y_of_grid_for_new_final_expense_button += .0005







        list_for_expense_ids_to_count.sort()
        list_for_expense_ids_to_count.reverse()

        expense_id_of_expense_with_highest_id_value = list_for_expense_ids_to_count[0]

        expense_id_for_new_expense = str(expense_id_of_expense_with_highest_id_value + 1)





        # EXPENSE INFORMATION (VALUES AND DESCRIPTION) OF NEW FINAL EXPENSE TO SAVE IN JSON FILE WITH EXPENSES OF BUDGET

        multiply_value = "1"
        description = "Description"
        amount = "0"
        divide_value = "1"
        total_amount = "0"

        values_for_new_expense = [multiply_value, description, amount, divide_value, total_amount]


        # KEY (EXPENSE ID) AND EXPENSE INFORMATION FOR DICTIONARY WITH EXPENSES

        key_and_expense_information_for_dictionary_with_expenses = {expense_id_for_new_expense: values_for_new_expense}



        with open(file_with_expenses, "r") as file:
            dictionary_with_expenses_before_new_expense = json.load(file)

            dictionary_with_expenses_before_new_expense.update(key_and_expense_information_for_dictionary_with_expenses)

            dictionary_with_new_expense_added = dictionary_with_expenses_before_new_expense


        with open(file_with_expenses, "w") as file:
            json.dump(dictionary_with_new_expense_added, file, indent= 2)




        self.new_final_expense_form = new_final_expense_POP_UP(expense_id_for_new_expense)

        self.new_final_expense_form.open()



        pass












