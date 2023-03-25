



# ------- functions limiting number of characters and showing last entered acceptable number ------
# ------- functions undoing last edition in the 4 text inputs -------------------------------------


def button_arrow_undo_UNDO_function(self):
    text_in_text_input_AMOUNT_before_press = self.ids.text_input_AMOUNT.text

    text_in_text_input_DESCRIPTION_before_press = self.ids.text_input_DESCRIPTION.text

    text_in_text_input_MULTIPLY_before_press = self.ids.text_input_MULTIPLY.text

    text_in_text_input_DIVIDE_before_press = self.ids.text_input_DIVIDE.text

    UNDO_is_pressed = "Pressed"

    file_controlling_if_undo_button_has_been_pressed = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_UNDO_pressed_or_not.json"

    with open(file_controlling_if_undo_button_has_been_pressed, "w") as file:
        json.dump(UNDO_is_pressed, file)

    file_with_updating_last_text_input_event = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_AMOUNT_last_event.json"

    with open(file_with_updating_last_text_input_event, "r") as file:
        list_with_events = json.load(file)

    if len(list_with_events) < 1:

        pass




    elif list_with_events[-1] == "text selected AMOUNT":

        number_of_text_selected_amount = list_with_events.count("text selected AMOUNT")

        for number in range(number_of_text_selected_amount):
            list_with_events.remove("text selected AMOUNT")

        with open(file_with_updating_last_text_input_event, "w") as file:
            json.dump(list_with_events, file)

        with open(file_with_updating_last_text_input_event, "r") as file:
            updated_list_with_events = json.load(file)

        if updated_list_with_events[-1] == "on_text MULTIPLY":

            self.ids.text_input_MULTIPLY.do_undo()

            text_in_text_input_MULTIPLY_after_press = self.ids.text_input_MULTIPLY.text

            if text_in_text_input_MULTIPLY_before_press == text_in_text_input_MULTIPLY_after_press:

                UNDO_is_not_pressed = ""

                file_controlling_if_undo_button_has_been_pressed = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_UNDO_pressed_or_not.json"

                with open(file_controlling_if_undo_button_has_been_pressed, "w") as file:
                    json.dump(UNDO_is_not_pressed, file)


            else:

                updated_list_with_events.pop()

                with open(file_with_updating_last_text_input_event, "w") as file:
                    json.dump(updated_list_with_events, file)




        elif updated_list_with_events[-1] == "on_text DIVIDE":

            self.ids.text_input_DIVIDE.do_undo()

            text_in_text_input_DIVIDE_after_press = self.ids.text_input_DIVIDE.text

            if text_in_text_input_DIVIDE_before_press == text_in_text_input_DIVIDE_after_press:

                UNDO_is_not_pressed = ""

                file_controlling_if_undo_button_has_been_pressed = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_UNDO_pressed_or_not.json"

                with open(file_controlling_if_undo_button_has_been_pressed, "w") as file:
                    json.dump(UNDO_is_not_pressed, file)


            else:

                updated_list_with_events.pop()

                with open(file_with_updating_last_text_input_event, "w") as file:
                    json.dump(updated_list_with_events, file)








        elif updated_list_with_events[-1] == "on_text AMOUNT":

            self.ids.text_input_AMOUNT.do_undo()

            text_in_text_input_AMOUNT_after_press = self.ids.text_input_AMOUNT.text

            if text_in_text_input_AMOUNT_before_press == text_in_text_input_AMOUNT_after_press:
                UNDO_is_not_pressed = ""

                file_controlling_if_undo_button_has_been_pressed = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_UNDO_pressed_or_not.json"

                with open(file_controlling_if_undo_button_has_been_pressed, "w") as file:
                    json.dump(UNDO_is_not_pressed, file)

            else:

                updated_list_with_events.pop()

                with open(file_with_updating_last_text_input_event, "w") as file:
                    json.dump(updated_list_with_events, file)







        elif updated_list_with_events[-1] == "on_text DESCRIPTION":

            self.ids.text_input_DESCRIPTION.do_undo()

            text_in_text_input_DESCRIPTION_after_press = self.ids.text_input_DESCRIPTION.text

            if text_in_text_input_DESCRIPTION_before_press == text_in_text_input_DESCRIPTION_after_press:
                UNDO_is_not_pressed = ""

                file_controlling_if_undo_button_has_been_pressed = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_UNDO_pressed_or_not.json"

                with open(file_controlling_if_undo_button_has_been_pressed, "w") as file:
                    json.dump(UNDO_is_not_pressed, file)



            else:

                updated_list_with_events.pop()

                with open(file_with_updating_last_text_input_event, "w") as file:
                    json.dump(updated_list_with_events, file)








    else:

        if list_with_events[-1] == "on_text MULTIPLY":

            self.ids.text_input_MULTIPLY.do_undo()

            text_in_text_input_MULTIPLY_after_press = self.ids.text_input_MULTIPLY.text

            if text_in_text_input_MULTIPLY_before_press == text_in_text_input_MULTIPLY_after_press:

                UNDO_is_not_pressed = ""

                file_controlling_if_undo_button_has_been_pressed = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_UNDO_pressed_or_not.json"

                with open(file_controlling_if_undo_button_has_been_pressed, "w") as file:
                    json.dump(UNDO_is_not_pressed, file)


            else:

                list_with_events.pop()

                with open(file_with_updating_last_text_input_event, "w") as file:
                    json.dump(list_with_events, file)




        elif list_with_events[-1] == "on_text DIVIDE":

            self.ids.text_input_DIVIDE.do_undo()

            text_in_text_input_DIVIDE_after_press = self.ids.text_input_DIVIDE.text

            if text_in_text_input_DIVIDE_before_press == text_in_text_input_DIVIDE_after_press:

                UNDO_is_not_pressed = ""

                file_controlling_if_undo_button_has_been_pressed = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_UNDO_pressed_or_not.json"

                with open(file_controlling_if_undo_button_has_been_pressed, "w") as file:
                    json.dump(UNDO_is_not_pressed, file)


            else:

                list_with_events.pop()

                with open(file_with_updating_last_text_input_event, "w") as file:
                    json.dump(list_with_events, file)





        elif list_with_events[-1] == "on_text AMOUNT":

            self.ids.text_input_AMOUNT.do_undo()

            text_in_text_input_AMOUNT_after_press = self.ids.text_input_AMOUNT.text

            if text_in_text_input_AMOUNT_before_press == text_in_text_input_AMOUNT_after_press:

                UNDO_is_not_pressed = ""

                file_controlling_if_undo_button_has_been_pressed = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_UNDO_pressed_or_not.json"

                with open(file_controlling_if_undo_button_has_been_pressed, "w") as file:
                    json.dump(UNDO_is_not_pressed, file)

            else:

                list_with_events.pop()

                with open(file_with_updating_last_text_input_event, "w") as file:
                    json.dump(list_with_events, file)






        elif list_with_events[-1] == "on_text DESCRIPTION":

            self.ids.text_input_DESCRIPTION.do_undo()

            text_in_text_input_DESCRIPTION_after_press = self.ids.text_input_DESCRIPTION.text

            if text_in_text_input_DESCRIPTION_before_press == text_in_text_input_DESCRIPTION_after_press:

                UNDO_is_not_pressed = ""

                file_controlling_if_undo_button_has_been_pressed = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_UNDO_pressed_or_not.json"

                with open(file_controlling_if_undo_button_has_been_pressed, "w") as file:
                    json.dump(UNDO_is_not_pressed, file)


            else:

                list_with_events.pop()

                with open(file_with_updating_last_text_input_event, "w") as file:
                    json.dump(list_with_events, file)

    # if list_with_events[-1] == "":


def function_limiting_number_of_CHARACTERS_in_text_input_def_MULTIPLY(self):
    file_controlling_if_undo_button_has_been_pressed = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_UNDO_pressed_or_not.json"

    with open(file_controlling_if_undo_button_has_been_pressed, "r") as file:
        is_UNDO_pressed_the_last_event_check = json.load(file)

        if is_UNDO_pressed_the_last_event_check == "Pressed":

            UNDO_not_last_event = ""

            with open(file_controlling_if_undo_button_has_been_pressed, "w") as file:
                json.dump(UNDO_not_last_event, file)



        else:

            is_arrow_pressed = self.list_storing_arrow_press[-1]

            if is_arrow_pressed == "Yes":

                is_arrow_pressed_updated = "No"

                self.list_storing_arrow_press.append(is_arrow_pressed_updated)

                pass

            else:
                last_event = "on_text MULTIPLY"

                file_with_updating_last_text_input_event = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_AMOUNT_last_event.json"

                with open(file_with_updating_last_text_input_event, "r") as file:
                    list_with_events = json.load(file)

                    list_with_events.append(last_event)

                with open(file_with_updating_last_text_input_event, "w") as file:
                    json.dump(list_with_events, file)


def function_limiting_number_of_CHARACTERS_in_text_input_DIVIDE(self):
    file_controlling_if_undo_button_has_been_pressed = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_UNDO_pressed_or_not.json"

    with open(file_controlling_if_undo_button_has_been_pressed, "r") as file:
        is_UNDO_pressed_the_last_event_check = json.load(file)

        if is_UNDO_pressed_the_last_event_check == "Pressed":

            UNDO_not_last_event = ""

            with open(file_controlling_if_undo_button_has_been_pressed, "w") as file:
                json.dump(UNDO_not_last_event, file)










        else:

            last_event = "on_text DIVIDE"

            file_with_updating_last_text_input_event = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_AMOUNT_last_event.json"

            with open(file_with_updating_last_text_input_event, "r") as file:
                list_with_events = json.load(file)

                list_with_events.append(last_event)

            with open(file_with_updating_last_text_input_event, "w") as file:
                json.dump(list_with_events, file)


def text_input_LIMITING_CHARACTERS_in_DESCRIPTION(self):
    file_controlling_if_undo_button_has_been_pressed = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_UNDO_pressed_or_not.json"

    with open(file_controlling_if_undo_button_has_been_pressed, "r") as file:
        is_UNDO_pressed_the_last_event_check = json.load(file)

        if is_UNDO_pressed_the_last_event_check == "Pressed":

            UNDO_not_last_event = ""

            with open(file_controlling_if_undo_button_has_been_pressed, "w") as file:
                json.dump(UNDO_not_last_event, file)







        else:

            last_event = "on_text DESCRIPTION"

            file_with_updating_last_text_input_event = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_AMOUNT_last_event.json"

            with open(file_with_updating_last_text_input_event, "r") as file:
                list_with_events = json.load(file)

                list_with_events.append(last_event)

            with open(file_with_updating_last_text_input_event, "w") as file:
                json.dump(list_with_events, file)


# FUNCTION LIMITING THE NUMBER OF CHARACTERS THE USER CAN WRITE IN THE TEXT INPUT

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!! MANGLER:
# !!!!!!!!!!!!!!!!!!!!!!!!!!!! 1) POP UP WARNING: TOO MANY CHARACTERS: Maximum number 99.999.999.999!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!! 2) FILE FOR CONTROLLING IF TEXT INPUT WAS EMPTY RIGHT BEFORE A NUMBER WITH TOO MANY
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! CHARACTERS WAS COPY PASTED INTO THE TEXT INPUT


def text_input_on_text_SAVE_SELECTED_TEXT_in_AMOUNT(self):
    file_controlling_if_undo_button_has_been_pressed = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_UNDO_pressed_or_not.json"

    with open(file_controlling_if_undo_button_has_been_pressed, "r") as file:
        is_UNDO_pressed_the_last_event_check = json.load(file)

        if is_UNDO_pressed_the_last_event_check == "Pressed":

            is_UNDO_pressed_last_event = "No"

            with open(file_controlling_if_undo_button_has_been_pressed, "w") as file:
                json.dump(is_UNDO_pressed_last_event, file)

            file_with_updating_last_text_input_event = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_AMOUNT_last_event.json"

            with open(file_with_updating_last_text_input_event, "r") as file:
                list_with_events = json.load(file)

                list_with_events.pop()

            with open(file_with_updating_last_text_input_event, "w") as file:
                json.dump(list_with_events, file)



        else:

            last_event = "text selected AMOUNT"

            # self.list_with_events.append(last_event)

            file_with_updating_last_text_input_event = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_AMOUNT_last_event.json"

            with open(file_with_updating_last_text_input_event, "r") as file:
                list_with_events = json.load(file)

                list_with_events.append(last_event)

            with open(file_with_updating_last_text_input_event, "w") as file:
                json.dump(list_with_events, file)

    # text_in_text_input = self.ids.text_input_AMOUNT.text

    text_to_save = self.ids.text_input_AMOUNT.selection_text

    # if text_in_text_input == text_to_save:

    #   pass

    # else:

    file_with_saved_selected_text = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_AMOUNT_saved_selected.json"

    with open(file_with_saved_selected_text, "r") as file:
        list_with_saved_selected_text = json.load(file)

        list_with_saved_selected_text.append(text_to_save)

    with open(file_with_saved_selected_text, "w") as file:
        json.dump(list_with_saved_selected_text, file)


def on_text_testing_what_happens(self):
    text = self.ids.text_input_AMOUNT.text

    print(text)


def function_limiting_number_of_CHARACTERS_in_text_input_AMOUNT(self):
    # First thing that happens when on_text triggers this function, is that the on_text event in AMOUNT is stored in a file
    # tracking the events of the 4 text inputs in the EDIT EXPENSE FORM, but ONLY if the UNDO Button hasn't been
    # pressed right before the on_text event. So before any of the code of any of the other on_text functions this
    # method produces, it is checked whether the UNDO Button has been pressed
    # right before this on_text event in AMOUNT happens. The reason the text in text input only should be saved in a
    # file if the UNDO Button hasn't been pressed right before the on_text event, is that the UNDO Button uses the
    # file tracking events in the 4 text inputs to know which text input to TextInput.undo(). If it weren't checked
    # if the UNDO Button has been pressed right before on_text event, then when the UNDO Button is pressed and an
    # on_text event thereby would happen in this text input AMOUNT (because the UNDO Button undo a edit in the text
    # input - this changes the text in the text input AMOUNT and so an on_text event happens) this on_text event would
    # be stored as the last event in file tracking the events of the 4 text inputs and so if the UNDO Button is pressed
    # again, it would undo text input AMOUNT again even if it was on of the other 3 inputs the second last edition has
    # happened.
    # If the UNDO Button HAS been pressed right before the on_text event, the file tracking if the UNDO Button has been
    # pressed is being updated to "" or "Not Pressed", so that in the next on_text event where the UNDO Button HAS NOT
    # been pressed right before, the on_text event WILL be registered/stored.

    file_controlling_if_undo_button_has_been_pressed = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_UNDO_pressed_or_not.json"

    with open(file_controlling_if_undo_button_has_been_pressed, "r") as file:
        is_UNDO_pressed_the_last_event_check = json.load(file)

        if is_UNDO_pressed_the_last_event_check == "Pressed":

            UNDO_not_last_event = ""

            with open(file_controlling_if_undo_button_has_been_pressed, "w") as file:
                json.dump(UNDO_not_last_event, file)



        else:

            # SAVING EVERY ON_TEXT EVENT IN FILE FOR CHECKING IF ANY TEXT WAS SELECTED TO BE REPLACED BY A NUMBER WITH TOO
            # MANY CHARACTERS

            last_event = "on_text AMOUNT"

            file_with_updating_last_text_input_event = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_AMOUNT_last_event.json"

            with open(file_with_updating_last_text_input_event, "r") as file:
                list_with_events = json.load(file)

                list_with_events.append(last_event)

            with open(file_with_updating_last_text_input_event, "w") as file:
                json.dump(list_with_events, file)

    characters_in_text_input = self.ids.text_input_AMOUNT.text

    file_to_store_text_input_from_amount = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_AMOUNT_limited.json"

    with open(file_to_store_text_input_from_amount, "r") as file:
        list_with_characters = json.load(file)

        list_with_characters.append(characters_in_text_input)

    with open(file_to_store_text_input_from_amount, "w") as file:
        json.dump(list_with_characters, file)

    if len(characters_in_text_input) >= 12:

        file_to_store_text_input_from_amount = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_AMOUNT_limited.json"

        with open(file_to_store_text_input_from_amount, "r") as file:
            list_with_characters = json.load(file)

        text_for_text_input = list_with_characters[-2]

        self.ids.text_input_AMOUNT.text = text_for_text_input

        # Checking if, before the text exceeded max number of characters, there was text in this text input
        # and the whole text/group of numbers was marked/selected and replaced by some copied/cut text.

        # If there was text and it was marked and replaced, then the text_for_text_input would result in ""

        # # (because when the too large
        # # number was pasted into the text input, it first removed the text, which would result in ""
        # # and be stored in the file
        # # recording the text in the text input and then it would paste in the too large number,
        # # which would result in [the too large number] which would be stored in the file recording
        # # the text in the text input. That means that list_with_characters[-2] = "")

        # and the length of the third/3d last bundle of text saved in the file storing the text in the text_input,
        # that is len(list_with_characters[-3], would be more than 1.

        # # (because before the replacement the marked/selected text is stored in the file recording
        # # the text input, that is, it is stored right before the "" and [the too large number]. And if there
        # # were some text to be marked/selected before the replacement, the len of this text is more than 1. If
        # # there was no text in the text input len(list_with_characters[-3] would be "".

        # So only if there was text before the max characters was exceeded and only if all of this text
        # was selected and replaced, would text_for_text_input == "" and len(list_with_characters[-3] >= 1)

        if text_for_text_input == "" and len(list_with_characters[-3]) >= 1:

            with open(file_with_updating_last_text_input_event, "r") as file:
                list_with_event_check = json.load(file)

            if list_with_event_check[-6] == "text selected AMOUNT":
                file_with_saved_selected_text = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_AMOUNT_saved_selected.json"

                with open(file_with_saved_selected_text, "r") as file:
                    list_with_selected_text = json.load(file)

                    self.ids.text_input_AMOUNT.text = list_with_selected_text[-2]

                # Updating the file storing last events, so the last relevant event is stored.
                # When text is marked/selected and

                with open(file_with_updating_last_text_input_event, "r") as file:
                    list_with_events = json.load(file)

                    list_with_events.pop()
                    list_with_events.pop()
                    list_with_events.pop()
                    list_with_events.pop()
                    list_with_events.pop()

                with open(file_with_updating_last_text_input_event, "w") as file:
                    json.dump(list_with_events, file)


###################################

                #file_with_updating_last_text_input_event = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_AMOUNT_last_event.json"

                #with open(file_with_updating_last_text_input_event, "r") as file:
                 #   list_with_events = json.load(file)

#                    list_with_events.pop()

#                with open(file_with_updating_last_text_input_event, "w") as file:
 #                   json.dump(list_with_events, file)


file_with_updating_last_text_input_event = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_AMOUNT_last_event.json"

with open(file_with_updating_last_text_input_event, "r") as file:
    list_with_events = json.load(file)

    list_with_events.pop()

with open(file_with_updating_last_text_input_event, "w") as file:
    json.dump(list_with_events, file)




file_with_updating_last_text_input_event = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_AMOUNT_last_event.json"

with open(file_with_updating_last_text_input_event, "r") as file:
    list_with_events = json.load(file)

    list_with_events.pop()

with open(file_with_updating_last_text_input_event, "w") as file:
    json.dump(list_with_events, file)



file_with_updating_last_text_input_event = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_AMOUNT_last_event.json"

with open(file_with_updating_last_text_input_event, "r") as file:
    list_with_events = json.load(file)

    list_with_events.pop()

with open(file_with_updating_last_text_input_event, "w") as file:
    json.dump(list_with_events, file)

file_with_last_event = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_AMOUNT_last_event.json"

with open(file_with_last_event, "r") as file:
    list_with_events = json.load(file)

    last_event_before_arrow_up_press = list_with_events[-1]

    list_with_events.append(last_event_before_arrow_up_press)

with open(file_with_last_event, "w") as file:
    json.dump(list_with_events, file)





setattr(self, "the_edit_expense_pop_up", edit_expense_POP_UP(self.expense_id))

list_with_characters = characters_in_text_input

file_to_store_text_input_from_amount = f"eb_a_created_budget_{self.budget_id}_expense_{self.expense_id}_MULTIPLY_limited.json"

with open(file_to_store_text_input_from_amount, "w") as file:
    json.dump(list_with_characters, file)

with open(file_to_store_text_input_from_amount, "r") as file:
    list_with_characters = json.load(file)

    list_with_characters.append(characters_in_text_input)

with open(file_to_store_text_input_from_amount, "w") as file:
    json.dump(list_with_characters, file)

text_selected = self.ids.text_input_MULTIPLY.selectio

class text_input_screen_G_edit_expense_MULTIPLY (TextInput):

    text_input_MULTIPLY_value = StringProperty("1")


    def __init__(self, expense_id, **kwargs):
        super(text_input_screen_G_edit_expense_MULTIPLY, self).__init__(**kwargs)


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

            multiply_value = list_with_expense_information[0]



            # SHOWING THE EXPENSE INFORMATION IN THE POP UP

        self.text_input_MULTIPLY_value = multiply_value
            # STORING THE EXPENSE INFORMATION IN VARIABLES











#---IF NOTHING IS WRITTEN IN DISPOSABLE AMOUNT TEXT INPUT THE TEXT IN THE TEXT INPUT CHANGES TO A '0'

    def on_text_if_nothing_then_0_in_MULTIPLY_text_input(self):

        text_in_text_input = self.text

        if text_in_text_input == "":
            self.text = "1"

        if text_in_text_input == "0":
            self.text = "1"




    def function_CALCULATING_TOTAL_AMOUNT_when_on_text_MULTIPLY(self):



    #---CALCULATING TOTAL AMOUNT

        multiply_text_input = self.text


        if multiply_text_input == "":
            pass

        else:


            key_for_correct_expense_form_object = self.expense_id

            # LOADING MULTIPLY VALUE AND MAKING IT A FLOAT
            multiply_value_to_save = float(self.text)

            # LOADING AMOUNT VALUE AND MAKING IT A FLOAT

            amount_to_save = float(App.get_running_app().root.get_screen("screen_G").
                                   dictionary_with_expense_forms[key_for_correct_expense_form_object].
                                   the_edit_expense_pop_up.text_input_screen_G_edit_expense_AMOUNT.text)


            # LOADING DIVIDE VALUE AND MAKING IT A FLOAT
            divide_value_to_save = float(App.get_running_app().root.get_screen("screen_G").
                                   dictionary_with_expense_forms[key_for_correct_expense_form_object].
                                         the_edit_expense_pop_up.text_input_screen_G_edit_expense_DIVIDE.text)

            # CALCULATING TOTAL AMOUNT OF EXPENSE
            calculated_total_amount = multiply_value_to_save * amount_to_save / divide_value_to_save

            App.get_running_app().root.get_screen("screen_G").dictionary_with_expense_forms[key_for_correct_expense_form_object].\
                the_edit_expense_pop_up.ids.label_TOTAL_AMOUNT.text = str(calculated_total_amount)




















class text_input_screen_G_edit_expense_DIVIDE (TextInput):


    text_input_DIVIDE_value = StringProperty("1")

    def __init__(self, expense_id, **kwargs):
        super(text_input_screen_G_edit_expense_DIVIDE, self).__init__(**kwargs)

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

            divide_value = list_with_expense_information[3]




        # SHOWING THE EXPENSE INFORMATION IN THE POP UP


        self.text_input_DIVIDE_value = divide_value



    def on_text_if_nothing_then_0_in_DIVIDE_text_input(self):

        text_in_text_input = self.text

        if text_in_text_input == "":
            self.text = "1"

        if text_in_text_input == "0":
            self.text = "1"


    def function_CALCULATING_TOTAL_AMOUNT_when_on_text_DIVIDE(self):
        # ---CALCULATING TOTAL AMOUNT

        divide_text_input = self.text

        if divide_text_input == "":
            pass

        else:

            key_for_correct_expense_form_object = self.expense_id

            # LOADING MULTIPLY VALUE AND MAKING IT A FLOAT
            multiply_value_to_save = float(App.get_running_app().root.get_screen("screen_G").
                                           dictionary_with_expense_forms[key_for_correct_expense_form_object].
                                           the_edit_expense_pop_up.text_input_screen_G_edit_expense_MULTIPLY.text)

            # LOADING AMOUNT VALUE AND MAKING IT A FLOAT
            amount_to_save = float(App.get_running_app().root.get_screen("screen_G").
                                   dictionary_with_expense_forms[key_for_correct_expense_form_object].
                                   the_edit_expense_pop_up.text_input_screen_G_edit_expense_AMOUNT.text)

            # LOADING DIVIDE VALUE AND MAKING IT A FLOAT
            divide_value_to_save = float(self.text)

            # CALCULATING TOTAL AMOUNT OF EXPENSE
            calculated_total_amount = multiply_value_to_save * amount_to_save / divide_value_to_save

            App.get_running_app().root.get_screen("screen_G").dictionary_with_expense_forms[
                key_for_correct_expense_form_object]. \
                the_edit_expense_pop_up.ids.label_TOTAL_AMOUNT.text = str(calculated_total_amount)






class text_input_screen_G_edit_expense_DESCRIPTION(TextInput):

    def __init__(self, expense_id, **kwargs):
        super(text_input_screen_G_edit_expense_DESCRIPTION, self).__init__(**kwargs)

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




    pass





class text_input_screen_G_edit_expense_AMOUNT(TextInput):



    def __init__(self, expense_id, **kwargs):
        super(text_input_screen_G_edit_expense_AMOUNT, self).__init__(**kwargs)

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



    def on_text_if_nothing_then_0_in_AMOUNT_text_input(self):

        text_in_text_input = self.text

        if text_in_text_input == "":
            self.text = "0"





    #def function_CALCULATING_TOTAL_AMOUNT_when_on_text_AMOUNT(self):





    #---CALCULATING TOTAL AMOUNT

        #amount_text_input = self.text

        #if amount_text_input == "":
         #   pass

        #else:


         #   key_for_correct_expense_form_object = self.expense_id



            # LOADING MULTIPLY VALUE AND MAKING IT A FLOAT
          #  multiply_value_to_save = float(App.get_running_app().root.get_screen("screen_G").dictionary_with_expense_forms[key_for_correct_expense_form_object].the_edit_expense_pop_up.text_input_screen_G_edit_expense_MULTIPLY.text)

            # LOADING AMOUNT VALUE AND MAKING IT A FLOAT
           # amount_to_save = float(self.text)

            # LOADING DIVIDE VALUE AND MAKING IT A FLOAT
            #divide_value_to_save = float(App.get_running_app().root.final_expenses.the_edit_expense_pop_up.text_input_screen_G_edit_expense_DIVIDE.text)

            # CALCULATING TOTAL AMOUNT OF EXPENSE
            #calculated_total_amount = multiply_value_to_save * amount_to_save / divide_value_to_save

            #App.get_running_app().root.get_screen("screen_G").dictionary_with_expense_forms[key_for_correct_expense_form_object].\
             #   the_edit_expense_pop_up.ids.label_TOTAL_AMOUNT.text = str(calculated_total_amount)













    self.text_input_screen_G_edit_expense_MULTIPLY.bind \
                (on_text=self.function_CALCULATING_TOTAL_AMOUNT_when_on_text_MULTIPLY)

    self.text_input_screen_G_edit_expense_DIVIDE.bind(
        on_text=self.function_CALCULATING_TOTAL_AMOUNT_when_on_text_DIVIDE)




    self.text_input_screen_G_edit_expense_AMOUNT.bind(
        on_text=self.function_CALCULATING_TOTAL_AMOUNT_when_on_text_AMOUNT)






file_with_list_of_budgets = f"eb_LIST_of_BUDGET_IDS.json"

        with open(file_with_list_of_budgets, "r") as file:
            list_of_budget_ids = json.load(file)