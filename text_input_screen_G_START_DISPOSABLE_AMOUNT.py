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


class text_input_START_DISPOSABLE_AMOUNT(TextInput):


    max_characters = NumericProperty(12)


    def __init__(self, **kwargs):
        super(text_input_START_DISPOSABLE_AMOUNT, self).__init__(**kwargs)





    #---WHEN APP IS OPENED: LAST ENTERED DISPOSABLE AMOUNT SHOWS------------

        file_with_id_of_current_budget_showing_in_screen_G = f"eb_CURRENT_BUDGET_showing.json"

        with open(file_with_id_of_current_budget_showing_in_screen_G, "r") as file:
            current_budget = json.load(file)

        if current_budget == 0:
            pass

        else:

            file_with_start_disposable_amount = f"eb_a_created_budget_{current_budget}_DISPOSABLE_AMOUNT.json"

            with open(file_with_start_disposable_amount, "r") as file:
                disposable_amount = json.load(file)

                self.text = disposable_amount




#---MAKING SURE THERE IS ALWAYS A INT/FLOAT TYPE SIGN IN SALDO TEXT INPUT

    def on_text_if_nothing_then_0_in_SALDO_text_input(self):

        text_in_text_input = self.text

        if text_in_text_input == "":
            self.text = "0"







    def insert_text(self, substring, from_undo=False):
        if len(self.text) >= self.max_characters and self.max_characters > 0:
            substring = ""
        TextInput.insert_text(self, substring, from_undo)






#---IF NOTHING IS WRITTEN IN DISPOSABLE AMOUNT TEXT INPUT THE TEXT IN IN THE TEXT INPUT CHANGES TO A '0'

    def on_text_if_nothing_then_0_in_text_input(self):
        text_in_text_input = self.text

        if text_in_text_input == "":
            self.text = "0"



#---on_text FUNCTION: SAVING LAST ENTERED DISPOSABLE AMOUNT -------------------------------

    def saving_DISPOSABLE_AMOUNT(self):

        file_with_id_of_current_budget_showing_in_screen_G = f"eb_CURRENT_BUDGET_showing.json"

        with open(file_with_id_of_current_budget_showing_in_screen_G, "r") as file:
            current_budget = json.load(file)

        if current_budget == 0:
            pass

        else:

            disposable_amount_to_save = self.text

            file_with_last_entered_disposable_amount = f"eb_a_created_budget_{current_budget}_DISPOSABLE_AMOUNT.json"

            with open(file_with_last_entered_disposable_amount, "w") as file:
                json.dump(disposable_amount_to_save, file)




#---on_text FUNCTION FOR text_input_START_DISPOSABLE_AMOUNT: RECALCULATING REMAINING AMOUNT AND
    # CURRENT DISPOSABLE AMOUNT -------------------------------

    def on_text_calculating_REMAINING_AMOUNT_and_CURRENT_DISPOSABLE_AMOUNT(self):



        file_with_id_of_current_budget_showing_in_screen_G = f"eb_CURRENT_BUDGET_showing.json"

        with open(file_with_id_of_current_budget_showing_in_screen_G, "r") as file:
            current_budget = json.load(file)



        if current_budget == 0:
            pass

        else:

            string_with_start_disposable_amount = self.text



            if string_with_start_disposable_amount == "":

                if App.get_running_app().root == None:
                    pass

                else:


                    self.text = "0"


                    total_of_expected_expenses = App.get_running_app().root.get_screen("screen_G").\
                        ids.label_TOTAL_OF_ALL_EXPENSES.text



                    # IF START DISPOSABLE AMOUNT IS 0 THEN REMAINING AMOUNT MUST BE 0 - TOTAL OF ALL EXPENSES
                    App.get_running_app().root.get_screen("screen_G").ids.label_REMAINING_AMOUNT.text = \
                        f"-{total_of_expected_expenses}"



                    total_of_paid_expenses = App.get_running_app().root.get_screen("screen_G").\
                        ids.label_TOTAL_OF_PAID_EXPENSES.text

                    App.get_running_app().root.get_screen("screen_G").\
                        ids.label_CURRENT_DISPOSABLE_AMOUNT.text = f"-{total_of_paid_expenses}"




            else:

                if App.get_running_app().root == None:
                    pass

                else:

                    start_disposable_amount = float(self.text)


                    label_with_total_of_all_expected_expenses = App.get_running_app().root.get_screen("screen_G").\
                        ids.label_TOTAL_OF_ALL_EXPENSES.text



                    total_of_expected_expenses = float(label_with_total_of_all_expected_expenses)




                    label_with_total_of_paid_expenses = App.get_running_app().root.get_screen("screen_G").\
                        ids.label_TOTAL_OF_PAID_EXPENSES.text

                    total_of_paid_expenses = float(label_with_total_of_paid_expenses)




                    App.get_running_app().root.get_screen("screen_G").\
                        ids.label_REMAINING_AMOUNT.text = str(start_disposable_amount - total_of_expected_expenses)


                    App.get_running_app().root.get_screen("screen_G").\
                        ids.label_CURRENT_DISPOSABLE_AMOUNT.text = str(
                        start_disposable_amount - total_of_paid_expenses)




    pass