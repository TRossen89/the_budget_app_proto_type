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




class text_input_DISPOSABLE_AMOUNT(TextInput):


    max_characters = NumericProperty(12)


    def __init__(self, **kwargs):
        super(text_input_DISPOSABLE_AMOUNT, self).__init__(**kwargs)


#-------WHEN APP IS OPENED: LAST ENTERED DISPOSABLE AMOUNT SHOWS------------

        file_with_disposable_amount = "eb_DISPOSABLE_AMOUNT.json"

        with open(file_with_disposable_amount, "r") as file:
            last_entered_disposable_amount = json.load(file)

        self.text = last_entered_disposable_amount




    def insert_text(self, substring, from_undo=False):
        if len(self.text) >= self.max_characters and self.max_characters > 0:
            substring = ""
        TextInput.insert_text(self, substring, from_undo)



#---IF NOTHING IS WRITTEN IN DISPOSABLE AMOUNT TEXT INPUT THE TEXT IN IN THE TEXT INPUT CHANGES TO A '0'

    def on_text_if_nothing_then_0_in_text_input(self):
        text_in_text_input = self.text

        if text_in_text_input == "":
            self.text = "0"



#----------SAVING LAST ENTERED DISPOSABLE AMOUNT IN JSON------------------

    def saving_DISPOSABLE_AMOUNT_in_json(self):

        amount_to_save = self.text

        file_with_disposable_amount = "eb_DISPOSABLE_AMOUNT.json"

        with open(file_with_disposable_amount, "w") as file:
            json.dump(amount_to_save, file)


    pass