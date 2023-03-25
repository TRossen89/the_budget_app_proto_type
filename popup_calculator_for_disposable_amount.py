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













#----------CLASS WITH THE POPUP CALCULATOR FOR DISPOSABLE AMOUNT-------------------------


class popup_calculator_for_disposable_amount (Popup):


# _____________________SIZE_HINT_Y_MAIN_GRID________________________________________________________________________

    size_hint_y_main_grid = NumericProperty(4)



# ___________________________TOP_HINTS______________________________________________________________________________


    top_hint_add_calc_btn = NumericProperty(.98)


    top_hint_total_txt_input = NumericProperty(.97)

    top_hint_view_calculations = NumericProperty(.96)





    def add_calculator(self):

        new_calculator_layout = new_calculator()

        self.size_hint_y_main_grid += .416666667

        self.top_hint_add_calc_btn -= .01

        self.top_hint_total_txt_input -= .01
        self.top_hint_view_calculations -= .01

        self.ids.grid_with_calculator.add_widget(new_calculator_layout)



#-----------------ARROWS UP AND DOWN---------------------------

    def function_of_arrow_up_multiply(self):


        initial_number_to_multiply_with = float(self.ids.multiply.text)

        initial_number_to_multiply_with += 1


        self.ids.multiply.text = str(initial_number_to_multiply_with)



    def function_of_arrow_down_multiply(self):

        initial_number_to_multiply_with = float(self.ids.multiply.text)

        initial_number_to_multiply_with -= 1

        self.ids.multiply.text = str(initial_number_to_multiply_with)



    def function_of_arrow_up_divide (self):


        initial_number_to_divide_with = float(self.ids.divide.text)

        initial_number_to_divide_with += 1

        self.ids.divide.text = str(initial_number_to_divide_with)



    def function_of_arrow_down_divide(self):


        initial_number_to_divide_with = float(self.ids.divide.text)

        initial_number_to_divide_with -= 1

        self.ids.divide.text = str(initial_number_to_divide_with)

    pass



#-----------------= FUNCTION----------------------


    def equals_to (self):


        multiplied_with = float(self.ids.multiply.text)
        divided_with = float(self.ids.divide.text)

        initial_amount = float(self.ids.amount.text)

        calculated_amount = multiplied_with * initial_amount / divided_with

        self.ids.amount.text = str(calculated_amount)



# _____________________________ADD TO TOTAL________________________________________________

# ________________ORIGINAL_ADD_TO_TOTAL________________________________________________

    def add_to_total(self):


        multiplied_with = float(self.ids.multiply.text)
        divided_with = float(self.ids.divide.text)

        initial_amount = float(self.ids.amount.text)

        calculated_amount = multiplied_with * initial_amount / divided_with

        amount_to_add = calculated_amount



        initial_total = float(self.ids.total_to_disposable_amount.text)


        total_when_amount_added = initial_total + amount_to_add

        self.ids.total_to_disposable_amount.text = str(total_when_amount_added)



        #description = self.ids.description.text

        #description_of_amount_added_to_total = Label(text=f"{description} \n "
         #                                                 f"+ Added: {str(gange_med)} * {str(initial_amount)} "
          #                                                f"/ {str(divideret_med)} = "
           #                                               f"{str(calculated_amount)} ", halign='center', font_size=12,
            #                                         color=(0, 0, 0, 1), )

        #self.ids.data_view_grid.add_widget(description_of_amount_added_to_total)
        #self.size_hint_y_main_grid += .2

        #self.ids.gange_en.text = str(1)
        #self.ids.divideret_en.text = str(1)



# _______________________SUBTRACT FROM TOTAL________________________________________________

    def subtract_from_total(self):


        multiplied_with = float(self.ids.multiply.text)
        divided_with = float(self.ids.divide.text)

        initial_amount = float(self.ids.amount.text)

        calculated_amount = multiplied_with * initial_amount / divided_with



        amount_to_subtract = calculated_amount

        initial_total = float(self.ids.total_to_disposable_amount.text)

        total_when_amount_added = initial_total - amount_to_subtract

        self.ids.total_to_disposable_amount.text = str(total_when_amount_added)



        #description = self.ids.description.text

        #description_of_amount_added_to_total = Label(text=f"{description} \n "
         #                                                 f"- Subtracted: {str(gange_med)} * {str(initial_amount)} "
          #                                                f"/ {str(divideret_med)} = "
           #                                               f"{str(calculated_amount)} ", halign='center', font_size=12,
            #                                         color=(0, 0, 0, 1), )

        #self.ids.data_view_grid.add_widget(description_of_amount_added_to_total)
        #self.size_hint_y_main_grid += .2





#__________________ADD the calculated amount TO DISPOSABLE AMOUNT_______________________________________________

    def enter_as_disp_amount (self):

        App.get_running_app().root.get_screen("screen_E").ids.text_input_DISPOSABLE_AMOUNT.text = \
            App.get_running_app().root.get_screen("screen_E").calculator.\
                ids.total_to_disposable_amount.text



        self.dismiss()



    def add_calc_amount_to_disp_amount (self):


        Initial_amount_in_disp_amount_txt_inp = \
            float(App.get_running_app().root.get_screen("screen_E").ids.text_input_DISPOSABLE_AMOUNT.text)

        Amount_calculated = float(App.get_running_app().root.get_screen("screen_E").calculator.ids.\
                total_to_disposable_amount.text)


        Amount_in_disp_amount_txtinp_when_calc_amount_added = Initial_amount_in_disp_amount_txt_inp + Amount_calculated

        App.get_running_app().root.get_screen("screen_E").ids.text_input_DISPOSABLE_AMOUNT.text = \
            str(Amount_in_disp_amount_txtinp_when_calc_amount_added)




        self.dismiss()




    def close_calc_popup (self):

        self.dismiss()









# -----------CALCULATOR THE USER CAN ADD IN 'POPUP CALCULATOR FOR DISPOSABLE AMOUNT'------------


class new_calculator(RelativeLayout):


# ------FUNCTIONS OF THE ARROWS POINTING UP AND DOWN-----------

# -----------------ARROWS UP AND DOWN---------------------------

    def function_of_arrow_up_multiply(self):
        initial_number_to_multiply_with = float(self.ids.new_calculator_multiply.text)

        initial_number_to_multiply_with += 1

        self.ids.new_calculator_multiply.text = str(initial_number_to_multiply_with)



    def function_of_arrow_down_multiply(self):
        initial_number_to_multiply_with = float(self.ids.new_calculator_multiply.text)

        initial_number_to_multiply_with -= 1

        self.ids.new_calculator_multiply.text = str(initial_number_to_multiply_with)


    def function_of_arrow_up_divide(self):
        initial_number_to_divide_with = float(self.ids.new_calculator_divide.text)

        initial_number_to_divide_with += 1

        self.ids.new_calculator_divide.text = str(initial_number_to_divide_with)


    def function_of_arrow_down_divide(self):
        initial_number_to_divide_with = float(self.ids.new_calculator_divide.text)

        initial_number_to_divide_with -= 1

        self.ids.new_calculator_divide.text = str(initial_number_to_divide_with)


    pass




# _______ = FUNCTION ________________________________________________________________

    def new_calculator_equals_to(self):


        multiplied_with = float(self.ids.new_calculator_multiply.text)

        divided_with = float(self.ids.new_calculator_divide.text)

        initial_amount = float(self.ids.new_calculator_amount.text)

        calculated_amount = multiplied_with * initial_amount / divided_with

        self.ids.new_calculator_amount.text = str(calculated_amount)

        self.ids.new_calculator_multiply.text = str(1)
        self.ids.new_calculator_divide.text = str(1)



# --------ADDING CALCULATED AMOUNT TO AMOUNT IN THE TEXT INPUT WITH THE TOTA------------

    def new_calculator_add_to_total(self):
        initial_amount = float(self.ids.new_calculator_amount.text)

        multiplied_with = float(self.ids.new_calculator_multiply.text)

        divided_with = float(self.ids.new_calculator_divide.text)

        calculated_amount = multiplied_with * initial_amount / divided_with

        amount_to_add = calculated_amount

        self.ids.new_calculator_multiply.text = str(1)
        self.ids.new_calculator_divide.text = str(1)

        total_text_input = \
            App.get_running_app().root.get_screen("screen_E").calculator. \
                ids.total_to_disposable_amount.text

        initial_total = float(total_text_input)

        total_when_amount_added = initial_total + amount_to_add

        App.get_running_app().root.get_screen("screen_E").calculator. \
            ids.total_to_disposable_amount.text = str(total_when_amount_added)



# ______DESCRIPTION when ADD____________________________________________________________

#    description = self.ids.new_calculator_description.text

#   description_of_amount_added_to_total = Label(text=f"{description} \n "
#                                                    f"+ Added: {str(gange_med)} * {str(initial_amount)} "
#                                                   f"/ {str(divideret_med)} = "
#                                                  f"{str(calculated_amount)} ", halign='center', font_size=12,
#                                            color=(0, 0, 0, 1))

# App.get_running_app().root.ids.b_c_disp_amount_win.calc_popup.ids.data_view_grid.add_widget(description_of_amount_added_to_total)

# App.get_running_app().root.ids.b_c_disp_amount_win.calc_popup.size_hint_y_main_grid += .2

# ---------------SUBTRACTING CALCULATED AMOUNT FROM AMOUNT IN THE TEXT INPUT WITH THE TOTAL OF CALCULATIONS------------

    def new_calculator_subtract_from_total(self):
        initial_amount = float(self.ids.new_calculator_amount.text)

        multiplied_with = float(self.ids.new_calculator_multiply.text)

        divided_with = float(self.ids.new_calculator_divide.text)

        calculated_amount = multiplied_with * initial_amount / divided_with

        amount_to_subtract = calculated_amount

        self.ids.new_calculator_multiply.text = str(1)
        self.ids.new_calculator_divide.text = str(1)

        total_text_input = \
            App.get_running_app().root.get_screen("screen_E").calculator. \
                ids.total_to_disposable_amount.text

        initial_total = float(total_text_input)

        total_when_amount_subtracted = initial_total - amount_to_subtract

        App.get_running_app().root.get_screen("screen_E").calculator. \
            ids.total_to_disposable_amount.text = str(total_when_amount_subtracted)

# ______DESCRIPTION when ADD____________________________________________________________

#    description = self.ids.custom_description.text

#   description_of_amount_added_to_total = Label(text=f"{description} \n "
#                                                    f"- Subtracted: {str(gange_med)} * {str(initial_amount)} "
#                                                   f"/ {str(divideret_med)} = "
#                                                  f"{str(calculated_amount)} ", halign='center', font_size=12,
#                                            color=(0, 0, 0, 1))

# App.get_running_app().root.ids.b_c_disp_amount_win.calc_popup.ids.data_view_grid.add_widget(
#   description_of_amount_added_to_total)

# App.get_running_app().root.ids.b_c_disp_amount_win.calc_popup.size_hint_y_main_grid += .2

















