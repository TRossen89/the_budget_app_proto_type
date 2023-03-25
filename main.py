#from kivy.uix.tabbedpanel import TabbedPanel


from screen_A import *
from screen_B import *
from screen_C import *
from screen_D import *
from screen_E import *
from screen_F import *
from screen_G import *
from screen_H import *
from screen_I import *
from screen_J import *



# working window size
Window.size = (360, 600)
#Window.size = (660, 900)






class Screen_K(Screen):
    pass

class Screen_L(Screen):
    pass



class Screen_M(Screen):
    pass



class Screen_N(Screen):
    pass

class Screen_O(Screen):
    pass

class Screen_P(Screen):
    pass









Builder.load_file('kv_files/loaded_kv_file.kv')





class MyBudget_protoType (App):


    def build (self):


    #--------ADDING SCREENS TO APP---------------

        myScreenManager = ScreenManager()

        myScreenManager.add_widget(Screen_A(name="screen_A"))

        myScreenManager.add_widget(Screen_B(name="screen_B"))

        myScreenManager.add_widget(Screen_C(name="screen_C"))
        myScreenManager.add_widget(Screen_D(name="screen_D"))
        myScreenManager.add_widget(Screen_E(name="screen_E"))
        myScreenManager.add_widget(Screen_F(name="screen_F"))
        myScreenManager.add_widget(Screen_G(name="screen_G"))

        myScreenManager.add_widget(Screen_H(name="screen_H"))
        myScreenManager.add_widget(Screen_I(name="screen_I"))
        myScreenManager.add_widget(Screen_J(name="screen_J"))




        myScreenManager.add_widget(Screen_K(name="screen_K"))
        myScreenManager.add_widget(Screen_L(name="screen_L"))
        myScreenManager.add_widget(Screen_M(name="screen_M"))
        myScreenManager.add_widget(Screen_N(name="screen_N"))
        myScreenManager.add_widget(Screen_O(name="screen_O"))
        myScreenManager.add_widget(Screen_P(name="screen_P"))


    #------MAKING THE TRANSITION BETWEEN SCREENS INSTANTANEUOSLY (THAT IS WITH NO SLIDE OR OTHER TRANSITION EFFECT)-----

        myScreenManager.transition = NoTransition()



    #---------MAKING LAST ENTERED SCREEN THE SCREEN SHOWING WHEN OPENING APP NEXT TIME--------

        filename = "the_LAST_ENTERED_screen.json"

        with open(filename, "r") as fileobject:
            the_last_entered_screen = json.load(fileobject)


        myScreenManager.current = the_last_entered_screen




        #  Hvis jeg gerne vil have SlideTransition er der et problem med de dynamisk tilføjede layouts.
        #  Jeg kan ikke bare skrive root.manager.transition.direction = "left/right".
        #  De dynamisk tilføjede layouts har ikke et attribute der hedder "manager"


        #sm.transition = SlideTransition()






        Window.clearcolor = (1, 1, 1, 1)

        return myScreenManager








if __name__ == '__main__':
    MyBudget_protoType().run()

