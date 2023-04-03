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
# Systematiser ordningen af klasser i filer

from screen_D import text_input_GIVE_BUDGET_NAME
from text_input_screen_E_DISPOSABLE_AMOUNT import text_input_DISPOSABLE_AMOUNT

from screen_E import Screen_E


### """ ###
#
# Systematiser ordningen og navngivningen af klasser i filer

from relativeLayout_screen_F_EXPENSE_FORMS import expense_forms
from relativeLayout_screen_G_final_EXPENSE_FORMS import final_expenses
from relativeLayout_eb_list_of_BUDGETS import eb_budgets



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




#-------------------------------------------------SCREEN F----------------------------------------------------


class Screen_F (Screen):

                                                                                    ############ SCREEN F ############

#---SIZE_HINT_Y OF EXPENSES MAIN GRID FRAME (IT INCREASES EVERY TIME THE USER ADD AN EXPENSE FORM TO THE SCREEN)--------


### """ ###
#
# Systematiser navngivningen af variable
    size_hint_y_of_expenses_main_grid_frame = NumericProperty(1)



#---"TOP" SIZE_HINT OF GRID FRAME FOR NEW EXPENSE BUTTON----------------------------------------

    top_size_hint_grid_frame_for_NEW_EXPENSE_button = NumericProperty(.9985)


#---"TOP" SIZE_HINT OF GRID FRAME FOR THE RESULTS (OF CALCULATIONS OF TOTAL OF ALL EXPENSES, REMAINING AMOUNT AND START AMOUNT)------

    top_size_hint_grid_frame_for_THE_RESULTS = NumericProperty(.9975)





    def __init__(self, **kwargs):
        super(Screen_F, self).__init__(**kwargs)



    #---STORING TEXT INPUT WITH DISPOSABLE AMOUNT IN SELF.VARIABLE

        self.text_input_DISPOSABLE_AMOUNT = text_input_DISPOSABLE_AMOUNT()



    #---WHEN APP IS OPENED: LAST ENTERED BUDGET NAME APPEAR IN TOP OF SCREEN-----------

        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer
        file_with_budget_name = "eb_BUDGET_NAME_for_the_budget_about_TO_BE_CREATED.json"

        with open(file_with_budget_name, "r") as file:
            budget_name = json.load(file)

        self.ids.budget_name_in_top.text = budget_name





                                                                                    ############ SCREEN F ############

    #-------WHEN APP IS OPENED: LAST CALCULATED TOTAL OF ALL EXPENSES SHOWS---------

        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer
        file_with_last_calculated_total_of_all_expenses = "eb_TOTAL_OF_ALL_EXPENSES.json"

        with open(file_with_last_calculated_total_of_all_expenses, "r") as file:
            last_calculated_total_of_all_expenses = json.load(file)


        self.ids.label_TOTAL_OF_ALL_EXPENSES.text = last_calculated_total_of_all_expenses




    #-------WHEN APP IS OPENED: LAST CALCULATED REMAINING AMOUNT SHOWS---------

        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer

        file_with_last_calculated_remaining_amount = "eb_REMAINING_AMOUNT.json"

        with open(file_with_last_calculated_remaining_amount, "r") as file:
            last_calculated_remaining_amount = json.load(file)

        self.ids.label_REMAINING_AMOUNT.text = last_calculated_remaining_amount




    #-------WHEN APP IS OPENED: LAST ENTERED START DISPOSABLE AMOUNT SHOWS---------

        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer

        file_with_last_entered_disposable_amount = "eb_DISPOSABLE_AMOUNT.json"

        with open(file_with_last_entered_disposable_amount, "r") as file:
            last_entered_disposable_amount = json.load(file)

        self.ids.label_START_DISPOSABLE_AMOUNT.text = last_entered_disposable_amount





    #--------------------------------------------------------------------------------------------------
    #-------------------------------------------EXPENSE FORMS------------------------------------------
    #--------------------------------------------------------------------------------------------------

    #---WHEN APP IS OPENED: (CORRECT NUMBER OF) EXPENSE FORMS IS SHOWNED IN SCREEN F---------



        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer
        filename_of_number_of_expense_forms = f"eb_LIST_of_current_EXPENSE_FORMS_count.json"

        with open(filename_of_number_of_expense_forms, "r") as fileobject:
            all_expense_forms_to_show_in_screen_F = json.load(fileobject)


            all_expense_forms_to_show_in_screen_F.sort()



        for expense_form in all_expense_forms_to_show_in_screen_F:

            if expense_form < 1:
                pass

                                                                                    ############ SCREEN F ############
            else:

                id_of_expense = expense_form


            #---EXPANDING SIZE OF SCREEN TO SCROLL----------------------------------------

                self.size_hint_y_of_expenses_main_grid_frame += .6




            #---LOWERING THE NEW EXPENSE BUTTON (MAKING ROOM FOR THE EXPENSE FORM)---------

                self.top_size_hint_grid_frame_for_NEW_EXPENSE_button -= .0025



            #---LOWERING THE LABELS WITH THE RESULTS OF CALCULATIONS OF TOTAL OF ALL
            #---EXPENSES, REMAINING AMOUNT AND START AMOUNT (MAKING ROOM FOR THE EXPENSE
            #---FORM)-----------------------------------------------------------------------

                self.top_size_hint_grid_frame_for_THE_RESULTS -= .0025




            #---CREATING JSON STORING FILES FOR ALL THE INDIVIDUAL EXPENSE FORMS (IF THESE FILES DON'T EXISTS ALREADY)



                if self.does_the_json_file_exists(f"expense_{id_of_expense}_text_input_AMOUNT.json"):
                    pass


                else:


        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer

                    default_value_for_text_input_amount = "0"


                    file_for_storing_amount_value = f"expense_{id_of_expense}_text_input_AMOUNT.json"

                    with open(file_for_storing_amount_value, "w") as file:
                        json.dump(default_value_for_text_input_amount, file)


                                                                                    ############ SCREEN F ############

                if self.does_the_json_file_exists(f"expense_{id_of_expense}_text_input_DESCRIPTION.json"):
                    pass

                else:

                    ### """ ###
                    #
                    # Lav/brug en funktion til at læse/dumpe i json.filer
                    default_text_in_description_text_input = "Description"


                    file_for_storing_description = f"expense_{id_of_expense}_text_input_DESCRIPTION.json"

                    with open(file_for_storing_description, "w") as filobject:
                        json.dump(default_text_in_description_text_input, filobject)





                if self.does_the_json_file_exists(f"expense_{id_of_expense}_state_DISABLED_OR_NOT.json"):
                    pass

                else:

                    ### """ ###
                    #
                    # Lav/brug en funktion til at læse/dumpe i json.filer
                    default_state_of_expense = "False"


                    file_with_state_of_expense = f"expense_{id_of_expense}_state_DISABLED_OR_NOT.json"

                    with open(file_with_state_of_expense, "w") as filobject:
                        json.dump(default_state_of_expense, filobject)







                if self.does_the_json_file_exists(f"expense_{id_of_expense}_text_input_DIVIDE.json"):
                    pass

                else:

                    ### """ ###
                    #
                    # Lav/brug en funktion til at læse/dumpe i json.filer
                    default_value_in_divide_text_input = "1"


                    file_for_storing_value_of_divide_text_input = \
                        f"expense_{id_of_expense}_text_input_DIVIDE.json"

                    with open(file_for_storing_value_of_divide_text_input, "w") as filobject:
                        json.dump(default_value_in_divide_text_input, filobject)





                if self.does_the_json_file_exists(f"expense_{id_of_expense}_text_input_MULTIPLY.json"):
                    pass


                else:

                    ### """ ###
                    #
                    # Lav/brug en funktion til at læse/dumpe i json.filer
                    default_value_in_multiply_text_input = "1"


                    file_for_storing_value_of_multiply_text_input= f"expense_{id_of_expense}_text_input_MULTIPLY.json"


                    with open(file_for_storing_value_of_multiply_text_input, "w") as filobject:
                        json.dump(default_value_in_multiply_text_input, filobject)








                if self.does_the_json_file_exists(f"expense_{id_of_expense}_button_text_ENTER_EXPENSE_or_EDIT_EXPENSE.json"):
                    pass


                else:

                    ### """ ###
                    #
                    # Lav/brug en funktion til at læse/dumpe i json.filer
                    default_text_on_enter_or_edit_button = "Enter expense"


                    file_for_storing_text_on_enter_or_edit_button = \
                        f"expense_{id_of_expense}_button_text_ENTER_EXPENSE_or_EDIT_EXPENSE.json"

                    with open(file_for_storing_text_on_enter_or_edit_button, "w") as filobject:
                        json.dump(default_text_on_enter_or_edit_button, filobject)









                if self.does_the_json_file_exists(
                        f"expense_{id_of_expense}_label_TOTAL_AMOUNT.json"):
                    pass


                else:

                    ### """ ###
                    #
                    # Lav/brug en funktion til at læse/dumpe i json.filer

                    default_value_in_total_amount_text_input = "0"


                    file_for_storing_value_of_total_amount = \
                        f"expense_{id_of_expense}_label_TOTAL_AMOUNT.json"

                    with open(file_for_storing_value_of_total_amount, "w") as filobject:
                        json.dump(default_value_in_total_amount_text_input, filobject)




            #---ADDING THE EXPENSE FORMS TO SCREEN F-----------------------------------

                self.ids.grid_frame_for_expense_forms.add_widget(expense_forms(id_of_expense))









    def does_the_json_file_exists(self, fileAndPath):
        return os.path.exists(fileAndPath)







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




#-------SAVING SCREEN_F AS LAST ENTERED SCREEN SO IF APP IS CLOSED WHILE SCREEN_F IS SHOWED,
# SCREEN_F WILL SHOW NEXT TIME APP IS OPENED--------

    def screen_F_in_last_entered_screen_json_file (self):

        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer

        screen_name_to_dump = "screen_F"

        filename = "the_LAST_ENTERED_screen.json"

        with open(filename, "w") as fileobject:
            json.dump(screen_name_to_dump, fileobject)




# -------SAVING SCREEN_A AS LAST ENTERED SCREEN SO IF APP IS CLOSED WHILE SCREEN_A IS SHOWED,
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


    def saving_TOTAL_OF_ALL_EXPENSES(self):

        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer

        total_to_save = self.ids.label_TOTAL_OF_ALL_EXPENSES.text

        file_with_last_calculated_total_of_all_expenses = "eb_TOTAL_OF_ALL_EXPENSES.json"

        with open(file_with_last_calculated_total_of_all_expenses, "w") as file:
            json.dump(total_to_save, file)



#--------------------------SAVING LAST CALCULATED REMAINING AMOUNT------------------------------

    def saving_REMAINING_AMOUNT(self):

        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer
        remaining_amount_to_save = self.ids.label_REMAINING_AMOUNT.text

        file_with_last_calculated_remaining_amount = "eb_REMAINING_AMOUNT.json"

        with open(file_with_last_calculated_remaining_amount, "w") as file:
            json.dump(remaining_amount_to_save, file)


#---------------------------SAVING LAST ENTERED DISPOSABLE AMOUNT-------------------------------

    def saving_DISPOSABLE_AMOUNT(self):

        ### """ ###
        #
        # Lav/brug en funktion til at læse/dumpe i json.filer

        disposable_amount_to_save = self.ids.label_START_DISPOSABLE_AMOUNT.text

        file_with_last_entered_disposable_amount = "eb_DISPOSABLE_AMOUNT.json"

        with open(file_with_last_entered_disposable_amount, "w") as file:
            json.dump(disposable_amount_to_save, file)










#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
#-------------------------FUNCTIONALITY OF WIDGET IN SCREEN F------------------------
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------





    def function_of_NEW_EXPENSE_button(self):



    #---THE COUNTER: COUNTING ALL EXPENSE FORMS (THE COUNT STARTS AT 3 BECAUSE SCREEN F SHOWS 3 EXPENSE FORMS AS DEFAULT)----

    ### """ ###
    #
    # Lav/brug en funktion til at læse/dumpe i json.filer
        file_with_number_of_expense_forms = f"eb_EXPENSE_FORMS_count.json"

        with open(file_with_number_of_expense_forms, "r") as file:
            number_of_expense_forms = json.load(file)

            count_of_expense_forms = number_of_expense_forms + 1

        with open(file_with_number_of_expense_forms, "w") as file:
            json.dump(count_of_expense_forms, file)




    #---ADDING EXPENSE ID TO THE LIST OF ALL EXPENSE FORMS WHICH CONSISTS OF THE IDS OF THE EXPENSES (GIVEN BY THE COUNTER)---

    ### """ ###
    #
    # Lav/brug en funktion til at læse/dumpe i json.filer

        file_with_list_of_expense_forms = f"eb_LIST_of_current_EXPENSE_FORMS_count.json"

        with open(file_with_list_of_expense_forms, "r") as file:
            list_of_expense_forms = json.load(file)

            id_of_expense = count_of_expense_forms

            list_of_expense_forms.append(id_of_expense)



        with open(file_with_list_of_expense_forms, "w") as file:
            json.dump(list_of_expense_forms, file)









    #---CREATING JSON STORING FILES FOR ALL THE INDIVIDUAL EXPENSE FORMS (IF THESE FILES DON'T EXISTS ALREADY)



        if self.does_the_json_file_exists(f"expense_{id_of_expense}_text_input_AMOUNT.json"):
            pass


        else:

            ### """ ###
            #
            # Lav/brug en funktion til at læse/dumpe i json.filer
            default_value_for_text_input_amount = "0"


            file_for_storing_amount_value = f"expense_{id_of_expense}_text_input_AMOUNT.json"

            with open(file_for_storing_amount_value, "w") as file:
                json.dump(default_value_for_text_input_amount, file)






        if self.does_the_json_file_exists(f"expense_{id_of_expense}_text_input_DESCRIPTION.json"):
            pass

        else:

            ### """ ###
            #
            # Lav/brug en funktion til at læse/dumpe i json.filer
            default_text_in_description_text_input = "Description"


            file_for_storing_description = f"expense_{id_of_expense}_text_input_DESCRIPTION.json"

            with open(file_for_storing_description, "w") as filobject:
                json.dump(default_text_in_description_text_input, filobject)





        if self.does_the_json_file_exists(f"expense_{id_of_expense}_state_DISABLED_OR_NOT.json"):
            pass

        else:

            ### """ ###
            #
            # Lav/brug en funktion til at læse/dumpe i json.filer
            default_state_of_expense = "False"


            file_with_state_of_expense = f"expense_{id_of_expense}_state_DISABLED_OR_NOT.json"

            with open(file_with_state_of_expense, "w") as filobject:
                json.dump(default_state_of_expense, filobject)







        if self.does_the_json_file_exists(f"expense_{id_of_expense}_text_input_DIVIDE.json"):
            pass

        else:

            ### """ ###
            #
            # Lav/brug en funktion til at læse/dumpe i json.filer

            default_value_in_divide_text_input = "1"


            file_for_storing_value_of_divide_text_input = \
                f"expense_{id_of_expense}_text_input_DIVIDE.json"

            with open(file_for_storing_value_of_divide_text_input, "w") as filobject:
                json.dump(default_value_in_divide_text_input, filobject)





        if self.does_the_json_file_exists(f"expense_{id_of_expense}_text_input_MULTIPLY.json"):
            pass


        else:

            ### """ ###
            #
            # Lav/brug en funktion til at læse/dumpe i json.filer
            default_value_in_multiply_text_input = "1"


            file_for_storing_value_of_multiply_text_input= f"expense_{id_of_expense}_text_input_MULTIPLY.json"


            with open(file_for_storing_value_of_multiply_text_input, "w") as filobject:
                json.dump(default_value_in_multiply_text_input, filobject)








        if self.does_the_json_file_exists(f"expense_{id_of_expense}_button_text_ENTER_EXPENSE_or_EDIT_EXPENSE.json"):
            pass


        else:

            ### """ ###
            #
            # Lav/brug en funktion til at læse/dumpe i json.filer
            default_text_on_enter_or_edit_button = "Enter expense"


            file_for_storing_text_on_enter_or_edit_button = \
                f"expense_{id_of_expense}_button_text_ENTER_EXPENSE_or_EDIT_EXPENSE.json"

            with open(file_for_storing_text_on_enter_or_edit_button, "w") as filobject:
                json.dump(default_text_on_enter_or_edit_button, filobject)









        if self.does_the_json_file_exists(
                f"expense_{id_of_expense}_label_TOTAL_AMOUNT.json"):
            pass


        else:

            ### """ ###
            #
            # Lav/brug en funktion til at læse/dumpe i json.filer
            default_value_in_total_amount_text_input = "0"


            file_for_storing_value_of_total_amount = \
                f"expense_{id_of_expense}_label_TOTAL_AMOUNT.json"

            with open(file_for_storing_value_of_total_amount, "w") as filobject:
                json.dump(default_value_in_total_amount_text_input, filobject)




    #---BEFORE ADDING NEW EXPENSE FORM: EXPANDING SIZE OF SCREEN TO SCROLL----------------------------------------

        self.size_hint_y_of_expenses_main_grid_frame += .6




    #---BEFORE ADDING NEW EXPENSE FORM: LOWERING THE NEW EXPENSE BUTTON (MAKING ROOM FOR THE EXPENSE FORM)---------

        self.top_size_hint_grid_frame_for_NEW_EXPENSE_button -= .0025


    #---BEFORE ADDING NEW EXPENSE FORM: LOWERING THE LABELS WITH THE RESULTS OF
    #---CALCULATIONS OF TOTAL OF ALL EXPENSES, REMAINING AMOUNT AND START AMOUNT
    #---(MAKING ROOM FOR THE EXPENSE FORM)-----------------------------------------------------------------------

        self.top_size_hint_grid_frame_for_THE_RESULTS -= .0025




    #---ADDING NEW EXPENSE FORM TO SCREEN F----------------------------------
        self.ids.grid_frame_for_expense_forms.add_widget(expense_forms(id_of_expense))

























#-------------------------------------------------------------------------------------------------
#---FUNCTION OF CREATE BUDGET BUTTON: ------------------------------------------------------------


    def function_CREATE_BUDGET_button(self):




    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #-------------------------------SAVING BUDGET (AND CREATING FILES FOR FUTURE SAVING)-------------------------------
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -




    #---ADDING BUDGET TO THE COUNT IF BUDGETS AND THEREBY CREATING BUDGETS ID FOR CREATED BUDGET: -----------

    ### """ ###
    #
    # Lav/brug en funktion til at læse/dumpe i json.filer

        file_with_count_of_budget_ids = f"eb_COUNTING_ids_of_BUDGETS.json"

        with open(file_with_count_of_budget_ids, "r") as file:
            number_of_budget_ids = json.load(file)

            number_of_budget_ids += 1

        with open(file_with_count_of_budget_ids, "w") as file:
            json.dump(number_of_budget_ids, file)


        budget_id = str(
            number_of_budget_ids)





    #---SAVING BUDGET ID IN JSON FILE WITH LIST OF BUDGET IDS: ------------------------------------

    ### """ ###
    #
    # Lav/brug en funktion til at læse/dumpe i json.filer
        file_with_list_of_budget_ids = f"eb_LIST_of_BUDGET_IDS.json"

        with open(file_with_list_of_budget_ids, "r") as file:
            list_of_budgets = json.load(file)

            list_of_budgets.append(number_of_budget_ids)

        with open(file_with_list_of_budget_ids, "w") as file:
            json.dump(list_of_budgets, file)





    #---SAVING BUDGET ID OF THE BUDGET SHOWING IN SCREEN G
    #---WHEN APP IS OPENED AFTER APP WAS CLOSED WHILE SCREEN G WAS SHOWING: ------------------------

    ### """ ###
    #
    # Lav/brug en funktion til at læse/dumpe i json.filer
    # Det er Screen_J og ikke Screen_I

        file_with_budget_id_of_current_showing_budget_in_screen_G_or_screen_I = f"eb_CURRENT_BUDGET_showing.json"

        with open(file_with_budget_id_of_current_showing_budget_in_screen_G_or_screen_I, "w") as file:
            json.dump(number_of_budget_ids, file)







    #---SAVING BUDGET NAME IN JSON FILE: -------------------------------------

        # LOADING BUDGET NAME FROM JSON FILE WITH BUDGET NAME OF BUDGET ABOUT TO BE CREATED:

    ### """ ###
    #
    # Lav/brug en funktion til at læse/dumpe i json.filer

        file_with_budget_name = f"eb_BUDGET_NAME_for_the_budget_about_TO_BE_CREATED.json"

        with open(file_with_budget_name, "r") as file:
            budget_name_to_save = json.load(file)



        # SAVING LOADED BUDGET NAME IN (CREATED) JSON FILE

    ### """ ###
    #
    # Lav/brug en funktion til at læse/dumpe i json.filer

        file_for_saving_budget_name_for_this_budget = f"eb_a_created_budget_{budget_id}_BUDGET_NAME.json"

        with open(file_for_saving_budget_name_for_this_budget, "w") as file:
            json.dump(budget_name_to_save, file)







    #---SAVING EXPENSES IN JSON FILE: ----------------------------------------


        # LOADING EXPENSES FROM JSON FILE WITH EXPENSES OF BUDGET ABOUT TO BE CREATED

    ### """ ###
    #
    # Lav/brug en funktion til at læse/dumpe i json.filer
        file_with_saved_expenses = "eb_EXPENSES_of_the_budget_about_TO_BE_CREATED.json"

        with open(file_with_saved_expenses, "r") as file:
            dictionary_of_data_in_file = json.load(file)

        data_to_save_in_file_with_expenses_of_created_budget = dictionary_of_data_in_file




        # SAVING LOADED EXPENSES IN (CREATED) JSON FILE

    ### """ ###
    #
    # Lav/brug en funktion til at læse/dumpe i json.filer
        file_to_save_the_expenses_of_this_budget = f"eb_a_created_budget_{budget_id}_THE_EXPENSES.json"

        with open(file_to_save_the_expenses_of_this_budget, "w") as file:
            json.dump(data_to_save_in_file_with_expenses_of_created_budget, file, indent=2)






   # SAVING START DISPOSABLE AMOUNT IN (CREATED) JSON FILE: ----------------------------------------

    ### """ ###
    #
    # Lav/brug en funktion til at læse/dumpe i json.filer
        file_with_start_disposable_amount = "eb_DISPOSABLE_AMOUNT.json"

        with open(file_with_start_disposable_amount, "r") as file:
            the_start_disposable_amount = json.load(file)

        data_to_save_in_file_with_start_disposable_amount_of_created_budget = the_start_disposable_amount

    ### """ ###
    #
    # Lav/brug en funktion til at læse/dumpe i json.filer
        file_to_save_the_start_disposable_amount_of_this_budget = f"eb_a_created_budget_{budget_id}_DISPOSABLE_AMOUNT.json"

        with open(file_to_save_the_start_disposable_amount_of_this_budget, "w") as file:
            json.dump(data_to_save_in_file_with_start_disposable_amount_of_created_budget, file)





    #---SAVING TOTAL OF ALL EXPENSES IN (CREATED) JSON FILE: ----------------------------------------

    ### """ ###
    #
    # Lav/brug en funktion til at læse/dumpe i json.filer

        file_with_total_of_all_expenses = "eb_TOTAL_OF_ALL_EXPENSES.json"

        with open(file_with_total_of_all_expenses, "r") as file:
            the_total_of_all_expenses = json.load(file)

        data_to_save_in_file_with_total_of_all_expenses_of_created_budget = the_total_of_all_expenses



    ### """ ###
    #
    # Lav/brug en funktion til at læse/dumpe i json.filer

        file_to_save_the_total_of_all_expenses_of_this_budget = f"eb_a_created_budget_{budget_id}_TOTAL_OF_ALL_EXPENSES.json"

        with open(file_to_save_the_total_of_all_expenses_of_this_budget, "w") as file:
            json.dump(data_to_save_in_file_with_total_of_all_expenses_of_created_budget, file)





    #---SAVING REMAINING AMOUNT IN (CREATED) JSON FILE: ----------------------------------------

    ### """ ###
    #
    # Lav/brug en funktion til at læse/dumpe i json.filer

        file_with_remaining_amount = "eb_REMAINING_AMOUNT.json"

        with open(file_with_remaining_amount, "r") as file:
            the_remaining_amount = json.load(file)

        data_to_save_in_file_with_remaining_amount_of_created_budget = the_remaining_amount


        file_to_save_the_remaining_amount_of_this_budget = f"eb_a_created_budget_{budget_id}_REMAINING_AMOUNT.json"

        with open(file_to_save_the_remaining_amount_of_this_budget, "w") as file:
            json.dump(data_to_save_in_file_with_remaining_amount_of_created_budget, file)







    #---CREATING JSON FILE FOR SAVING TOTAL OF PAID EXPENSES: ----------------------------------------

    ### """ ###
    #
    # Lav/brug en funktion til at læse/dumpe i json.filer

        data_to_save_in_file_with_total_paid_expenses = "0"

        file_to_save_the_total_of_paid_expenses_of_this_budget = f"eb_a_created_budget_{budget_id}_TOTAL_OF_PAID_EXPENSES.json"

        with open(file_to_save_the_total_of_paid_expenses_of_this_budget, "w") as file:
            json.dump(data_to_save_in_file_with_total_paid_expenses, file)






    #---CREATING JSON FILE FOR SAVING TOTAL OF PAID EXPENSES: ----------------------------------------

    ### """ ###
    #
    # Lav/brug en funktion til at læse/dumpe i json.filer
        data_to_save_in_file_with_current_disposable_amount_expenses = the_start_disposable_amount

        file_to_save_the_current_disposable_amount_of_this_budget = \
            f"eb_a_created_budget_{budget_id}_CURRENT_DISPOSABLE_AMOUNT.json"

        with open(file_to_save_the_current_disposable_amount_of_this_budget, "w") as file:
            json.dump(data_to_save_in_file_with_current_disposable_amount_expenses, file)












    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # -------------------------------------------------SCREEN I--------------------------------------------------------
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -




        widget_frame_for_budget = eb_budgets(budget_id)

        App.get_running_app().root.get_screen("screen_I").\
            ids.grid_frame_for_all_eb_budgets.add_widget(widget_frame_for_budget)









    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # -------------------------------------------------SCREEN G--------------------------------------------------------
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

########## # # #################### # # # # # # # # # # ##  ## # # # # # #  ##################################

    #---SHOWING BUDGET NAME IN SCREEN G:

        #text_input_with_budget_name = text_input_GIVE_BUDGET_NAME()

        budget_name_for_created_budget = App.get_running_app().root.get_screen("screen_D").ids.text_input_GIVE_BUDGET_NAME.text

        #budget_name_for_created_budget = text_input_with_budget_name.text

        #App.get_running_app().root.get_screen("screen_G").ids.budget_name_in_top.text = budget_name_for_created_budget

        App.get_running_app().root.get_screen("screen_G").ids.budget_name_in_top.text = budget_name_to_save




############### # # # # # # # # #  # # # #  # # #  # # ######################## # # # #    ### # # # # # #



    #---SHOWING TOTAL OF ALL EXPENSES IN SCREEN G: ----------------------------

        total_of_all_expenses = self.ids.label_TOTAL_OF_ALL_EXPENSES.text

        App.get_running_app().root.get_screen("screen_G").ids.label_TOTAL_OF_ALL_EXPENSES.text = total_of_all_expenses



    #---SHOWING REMAINING AMOUNT IN SCREEN G: ----------------------------------------

        remaining_amount = self.ids.label_REMAINING_AMOUNT.text

        App.get_running_app().root.get_screen(
            "screen_G").ids.label_REMAINING_AMOUNT.text = remaining_amount




    #---SHOWING START DISPOSABLE AMOUNT IN SCREEN G: ------------------------------------

        start_disposable_amount = self.ids.label_START_DISPOSABLE_AMOUNT.text

        App.get_running_app().root.get_screen(
            "screen_G").text_input_with_start_disposable_amount.text = start_disposable_amount



    #---SHOWING TOTAL OF PAID EXPENSES IN SCREEN G: -------------------------------------

        total_of_paid_expenses = "0"

        App.get_running_app().root.get_screen(
            "screen_G").ids.label_TOTAL_OF_PAID_EXPENSES.text = total_of_paid_expenses




    #---SHOWING CURRENT DISPOSABLE AMOUNT IN SCREEN G: ------------------------------------

        current_disposable_amount = self.ids.label_START_DISPOSABLE_AMOUNT.text

        App.get_running_app().root.get_screen(
            "screen_G").ids.label_CURRENT_DISPOSABLE_AMOUNT.text = current_disposable_amount







    #---CLEARING (THE WIDGETS WITH THE) PREVIOUSLY ADDED EXPENSES (FROM PREVIOUS BUDGET)
    #---IN SCREEN G BEFORE ADDING EXPENSES OF CURRENT BUDGET:


        App.get_running_app().root.get_screen("screen_G"). \
        ids.grid_frame_for_all_expenses.clear_widgets()

        App.get_running_app().root.get_screen("screen_G").pos_hint_y_of_grid_for_new_final_expense_button = .994








    #---SHOWING EXPENSES IN SCREEN G: -------------------------------------



    ### """ ###
    #
    # Lav/brug en funktion til at læse/dumpe i json.filer
        file_with_ids_of_entered_expense = "eb_IDS_of_ENTERED_EXPENSES_in_budget_about_TO_BE_CREATED.json"

        with open(file_with_ids_of_entered_expense, "r") as file:
            list_of_ids = json.load(file)


        #---SORTING LIST OF EXPENSE-IDS SO EXPENSES ARE SHOWN IN THE ORDER THEY
        #---WERE SHOWN IN SCREEN F WHERE EXPENSES ARE ENTERED

            list_of_ids.sort()


        #---LOADING EXPENSE INFORMATION (MULTIPLY VALUE, DESCRIPTION, AMOUNT ETC) FROM FILES CREATED FOR THIS BUDGET

            for expense_id in list_of_ids:

                if expense_id == 0:
                    pass

                else:

                    ### """ ###
                    #
                    # Lav/brug en funktion til at læse/dumpe i json.filer

                    file_with_value_in_multiply_text_input = f"expense_{expense_id}_text_input_MULTIPLY.json"

                    with open(file_with_value_in_multiply_text_input, "r") as file:
                        multiply_value = json.load(file)





                    file_with_value_in_divide_text_input = f"expense_{expense_id}_text_input_DIVIDE.json"

                    with open(file_with_value_in_divide_text_input, "r") as file:
                        divide_value = json.load(file)




                    file_with_text_in_description_text_input = f"expense_{expense_id}_text_input_DESCRIPTION.json"

                    with open(file_with_text_in_description_text_input, "r") as file:
                        description = json.load(file)




                    file_with_text_in_amount_text_input = f"expense_{expense_id}_text_input_AMOUNT.json"

                    with open(file_with_text_in_amount_text_input, "r") as file:
                        amount = json.load(file)




                    file_with_total_of_expense_label = f"expense_{expense_id}_label_TOTAL_AMOUNT.json"

                    with open(file_with_total_of_expense_label, "r") as file:
                        total_of_expense = json.load(file)





                #---ID OF EXPENSE:

                    id_of_expense = str(expense_id)


                #---DISPLAYING EXPENSES IN SCREEN G: ----------------------------------------



                ### """ ###
                #
                # Systematiser navngivnelsen af objecter fra klasser du har kreeret


                    widget_for_displaying_expense_from_CLASS_relativeLayout = final_expenses(id_of_expense, multiply_value, description, amount, divide_value,
                                                                    total_of_expense)



                    App.get_running_app().root.get_screen(
                        "screen_G").pos_hint_y_of_grid_for_new_final_expense_button -= .0005


                    App.get_running_app().root.get_screen("screen_G"). \
                        ids.grid_frame_for_all_expenses.add_widget(widget_for_displaying_expense_from_CLASS_relativeLayout)



















    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #-------------------------------------------------RESETTING-------------------------------------------------------
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -








########### DU ER NÅET HERTIL ###################################################################################


### """ ###
#
# Lav/brug en funktion til at læse/dumpe/resette indhold i json.filer


    #---RESETTING REST OF eb_JSON FILES:

        file_with_budget_name_of_the_budget_about_to_be_created = \
            f"eb_BUDGET_NAME_for_the_budget_about_TO_BE_CREATED.json"

        text_for_budget_name_file = "Enter budget name"

        with open(file_with_budget_name_of_the_budget_about_to_be_created, "w") as file:
            json.dump(text_for_budget_name_file, file)






        file_with_dictionary_with_expenses_of_the_budget_about_to_be_created = \
            f"eb_EXPENSES_of_the_budget_about_TO_BE_CREATED.json"


        dictionary_for_file = {"0": ["No expenses"]}

        with open(file_with_dictionary_with_expenses_of_the_budget_about_to_be_created, "w") as file:
            json.dump(dictionary_for_file, file)






        file_with_ids_of_entered_expenses = \
            f"eb_IDS_of_ENTERED_EXPENSES_in_budget_about_TO_BE_CREATED.json"

        list_of_ids_of_entered_expenses = [0]

        with open(file_with_ids_of_entered_expenses, "w") as file:
            json.dump(list_of_ids_of_entered_expenses, file)






        file_with_disposable_amount = f"eb_DISPOSABLE_AMOUNT.json"

        amount_for_file = "0"

        with open(file_with_disposable_amount, "w") as file:
            json.dump(amount_for_file, file)




        file_with_remaining_amount = f"eb_REMAINING_AMOUNT.json"

        remaining_amount_for_file = "0"

        with open(file_with_remaining_amount, "w") as file:
            json.dump(remaining_amount_for_file, file)





        file_with_total_of_all_expenses = f"eb_TOTAL_OF_ALL_EXPENSES.json"

        total_of_all_expenses_for_file = "0"

        with open(file_with_total_of_all_expenses, "w") as file:
            json.dump(total_of_all_expenses_for_file, file)






    #---REMOVING eb_JSON FILES - AND RESETTING size_hints OF MAIN GRID FRAME, GRID FRAME FOR NEW EXPENSE BUTTON
    #---AND GRID FRAME FOR THE RESULTS IN SCREEN F:

        file_with_list_of_expense_forms = f"eb_LIST_of_current_EXPENSE_FORMS_count.json"

        with open(file_with_list_of_expense_forms, "r") as file:
            list_of_expense_forms = json.load(file)


            for expense_id in list_of_expense_forms:


            #---REMOVING EVERY FILE WITH EXPENSE INFORMATION (MULTIPLY-VALUE, DESCRIPTION, ETC.)

                os.remove(f"expense_{expense_id}_label_TOTAL_AMOUNT.json")
                os.remove(f"expense_{expense_id}_text_input_AMOUNT.json")
                os.remove(f"expense_{expense_id}_text_input_DESCRIPTION.json")
                os.remove(f"expense_{expense_id}_text_input_DIVIDE.json")
                os.remove(f"expense_{expense_id}_text_input_MULTIPLY.json")

                os.remove(f"expense_{expense_id}_state_DISABLED_OR_NOT.json")
                os.remove(f"expense_{expense_id}_button_text_ENTER_EXPENSE_or_EDIT_EXPENSE.json")


            #---RESETTING THE SIZE OF SCREEN TO SCROLL----------------------------------------

                self.size_hint_y_of_expenses_main_grid_frame -= .6




            #---RESETTING THE POSITION OF THE NEW EXPENSE BUTTON (MAKING ROOM FOR THE EXPENSE FORM)---------

                self.top_size_hint_grid_frame_for_NEW_EXPENSE_button += .0025




            #---RESETTING THE POSITION OF THE LABELS WITH THE RESULTS OF CALCULATIONS OF TOTAL OF ALL
            #---EXPENSES, REMAINING AMOUNT AND START AMOUNT (MAKING ROOM FOR THE EXPENSE
            #---FORM)-----------------------------------------------------------------------

                self.top_size_hint_grid_frame_for_THE_RESULTS += .0025



    #---RESETTING WHAT IS SHOWN IN SCREEN D, E AND F:


    #---SCREEN D---

        App.get_running_app().root.get_screen("screen_D").ids.text_input_GIVE_BUDGET_NAME.text = "Enter budget name"



    #---SCREEN E---


        App.get_running_app().root.get_screen("screen_E").text_input_with_disposable_amount.text = "0"




    #---SCREEN F---

        

        self.ids.label_TOTAL_OF_ALL_EXPENSES.text = "0"

        self.ids.label_REMAINING_AMOUNT.text = "0"

        self.ids.label_START_DISPOSABLE_AMOUNT.text = "0"




    #---RESETTING THE COUNTER: COUNTING ALL EXPENSE FORMS (THE COUNT STARTS AT 3 BECAUSE SCREEN F SHOWS 3 EXPENSE FORMS AS DEFAULT)----

    ### """ ###
    #
    # Lav/brug en funktion til at læse/dumpe i json.filer
        file_with_number_of_expense_forms = f"eb_EXPENSE_FORMS_count.json"

        number_of_expense_forms = 3

        with open(file_with_number_of_expense_forms, "w") as file:
            json.dump(number_of_expense_forms, file)




    #---RESETTING THE LIST OF ALL EXPENSE FORMS WHICH CONSISTS OF THE IDS OF THE EXPENSES:

        file_with_list_of_expense_forms = f"eb_LIST_of_current_EXPENSE_FORMS_count.json"

        list_of_expense_ids = [1, 2, 3]

        with open(file_with_list_of_expense_forms, "w") as file:
            json.dump(list_of_expense_ids, file)



    #---CLEARING WIDGETS FROM GRID FRAME FOR EXPENSE FORMS - THAT IS: EVERY EXPENSE FORM IS REMOVED FROM SCREEN F:

        self.ids.grid_frame_for_expense_forms.clear_widgets()




    #---RESETTING NUMBER OF EXPENSE FORMS SHOWN IN SCREEN F (TO THE DEFAULT: 3):

    ### """ ###
    #
    # Lav/brug en funktion til at læse/dumpe i json.filer
        with open(file_with_list_of_expense_forms, "r") as file:
            list_of_expense_forms = json.load(file)

        for expense_form in list_of_expense_forms:

            id_of_expense = expense_form



        #---EXPANDING SIZE OF SCREEN TO SCROLL----------------------------------------

            self.size_hint_y_of_expenses_main_grid_frame += .6



        #---LOWERING THE NEW EXPENSE BUTTON (MAKING ROOM FOR THE EXPENSE FORM)---------

            self.top_size_hint_grid_frame_for_NEW_EXPENSE_button -= .0025




        #---LOWERING THE LABELS WITH THE RESULTS OF CALCULATIONS OF TOTAL OF ALL
        #---EXPENSES, REMAINING AMOUNT AND START AMOUNT (MAKING ROOM FOR THE EXPENSE
        #---FORM)-----------------------------------------------------------------------

            self.top_size_hint_grid_frame_for_THE_RESULTS -= .0025





        #---CREATING JSON STORING FILES FOR ALL THE INDIVIDUAL, RESETTED EXPENSE FORMS (IF THESE FILES DON'T EXISTS ALREADY)

            if self.does_the_json_file_exists(f"expense_{id_of_expense}_text_input_AMOUNT.json"):
                pass


            else:

                ### """ ###
                #
                # Lav/brug en funktion til at læse/dumpe i json.filer



                default_value_for_text_input_amount = "0"

                file_for_storing_amount_value = f"expense_{id_of_expense}_text_input_AMOUNT.json"

                with open(file_for_storing_amount_value, "w") as file:
                    json.dump(default_value_for_text_input_amount, file)




            if self.does_the_json_file_exists(f"expense_{id_of_expense}_text_input_DESCRIPTION.json"):
                pass

            else:

                default_text_in_description_text_input = "Description"

                file_for_storing_description = f"expense_{id_of_expense}_text_input_DESCRIPTION.json"

                with open(file_for_storing_description, "w") as filobject:
                    json.dump(default_text_in_description_text_input, filobject)





            if self.does_the_json_file_exists(f"expense_{id_of_expense}_state_DISABLED_OR_NOT.json"):
                pass

            else:

                default_state_of_expense = "False"

                file_with_state_of_expense = f"expense_{id_of_expense}_state_DISABLED_OR_NOT.json"

                with open(file_with_state_of_expense, "w") as filobject:
                    json.dump(default_state_of_expense, filobject)





            if self.does_the_json_file_exists(f"expense_{id_of_expense}_text_input_DIVIDE.json"):
                pass

            else:

                default_value_in_divide_text_input = "1"

                file_for_storing_value_of_divide_text_input = \
                    f"expense_{id_of_expense}_text_input_DIVIDE.json"

                with open(file_for_storing_value_of_divide_text_input, "w") as filobject:
                    json.dump(default_value_in_divide_text_input, filobject)





            if self.does_the_json_file_exists(f"expense_{id_of_expense}_text_input_MULTIPLY.json"):
                pass


            else:

                default_value_in_multiply_text_input = "1"

                file_for_storing_value_of_multiply_text_input = f"expense_{id_of_expense}_text_input_MULTIPLY.json"

                with open(file_for_storing_value_of_multiply_text_input, "w") as filobject:
                    json.dump(default_value_in_multiply_text_input, filobject)





            if self.does_the_json_file_exists(
                    f"expense_{id_of_expense}_button_text_ENTER_EXPENSE_or_EDIT_EXPENSE.json"):
                pass


            else:

                default_text_on_enter_or_edit_button = "Enter expense"

                file_for_storing_text_on_enter_or_edit_button = \
                    f"expense_{id_of_expense}_button_text_ENTER_EXPENSE_or_EDIT_EXPENSE.json"

                with open(file_for_storing_text_on_enter_or_edit_button, "w") as filobject:
                    json.dump(default_text_on_enter_or_edit_button, filobject)






            if self.does_the_json_file_exists(
                    f"expense_{id_of_expense}_label_TOTAL_AMOUNT.json"):
                pass


            else:

                default_value_in_total_amount_text_input = "0"

                file_for_storing_value_of_total_amount = \
                    f"expense_{id_of_expense}_label_TOTAL_AMOUNT.json"

                with open(file_for_storing_value_of_total_amount, "w") as filobject:
                    json.dump(default_value_in_total_amount_text_input, filobject)





            self.ids.grid_frame_for_expense_forms.add_widget(expense_forms(id_of_expense))






    pass






