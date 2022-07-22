from tkinter import *
from time import sleep

root = Tk() # Start
root.resizable(False,False) # window cannot be resized
root.title("4Func Calc") # title of the window

# easy values
base_padx = 20
base_pady = 20
base_sticky = "nsew"
base_function_bg = "grey"
base_function_relief = "groove"
base_number_relief = "raised"
base_number_font = ("Segoe UI", 9, "normal")

## create the two main frames for this application

# frame for theboxes showing numbers 
frame_boxes = Frame(root)
frame_boxes.grid(sticky="ew")

# frames for the clickable keys
frame_keypad = Frame(root)
frame_keypad.grid(sticky="nsew")

## create the display boxes

# create the display box for showing information above the entry 
top_box = Label(frame_boxes, fg="blue", bg="grey", relief="ridge", font=base_number_font, anchor="e", text="")
top_box.pack(side="top", fill="x")

# create and place the entry box
bottom_box = Label(frame_boxes, fg="blue", bg="grey", relief="ridge", font = ("Segoe UI", 14, "normal"), anchor="e", text="0") # entry box
bottom_box.pack(side="bottom", fill="x") # placement of the column

## create the clickable buttons

# create number buttons
button_0 = Button(frame_keypad, text="0", padx=base_padx, pady=base_pady, relief = base_number_relief, font=base_number_font, command=lambda: clicked_num(0))
button_1 = Button(frame_keypad, text="1", padx=base_padx, pady=base_pady, relief = base_number_relief, font=base_number_font, command=lambda: clicked_num(1))
button_2 = Button(frame_keypad, text="2", padx=base_padx, pady=base_pady, relief = base_number_relief, font=base_number_font, command=lambda: clicked_num(2))
button_3 = Button(frame_keypad, text="3", padx=base_padx, pady=base_pady, relief = base_number_relief, font=base_number_font, command=lambda: clicked_num(3))
button_4 = Button(frame_keypad, text="4", padx=base_padx, pady=base_pady, relief = base_number_relief, font=base_number_font, command=lambda: clicked_num(4))
button_5 = Button(frame_keypad, text="5", padx=base_padx, pady=base_pady, relief = base_number_relief, font=base_number_font, command=lambda: clicked_num(5))
button_6 = Button(frame_keypad, text="6", padx=base_padx, pady=base_pady, relief = base_number_relief, font=base_number_font, command=lambda: clicked_num(6))
button_7 = Button(frame_keypad, text="7", padx=base_padx, pady=base_pady, relief = base_number_relief, font=base_number_font, command=lambda: clicked_num(7))
button_8 = Button(frame_keypad, text="8", padx=base_padx, pady=base_pady, relief = base_number_relief, font=base_number_font, command=lambda: clicked_num(8))
button_9 = Button(frame_keypad, text="9", padx=base_padx, pady=base_pady, relief = base_number_relief, font=base_number_font, command=lambda: clicked_num(9))

# create operation buttons
button_add = Button(frame_keypad, text="+", padx=base_padx, pady=base_pady,bg=base_function_bg, relief = base_function_relief, font=base_number_font, command=lambda: clicked_operation("+"))
button_subtract = Button(frame_keypad, text="-", padx=base_padx, pady=base_pady, bg=base_function_bg, relief = base_function_relief, font=base_number_font, command=lambda: clicked_operation("-"))
button_multiply = Button(frame_keypad, text="×", padx=base_padx, pady=base_pady, bg=base_function_bg, relief = base_function_relief, font=base_number_font, command=lambda: clicked_operation("×"))
button_divide = Button(frame_keypad, text="÷", padx=base_padx, pady=base_pady, bg=base_function_bg, relief = base_function_relief, font=base_number_font, command=lambda: clicked_operation("÷"))
button_equals = Button(frame_keypad, text="=", padx=base_padx, pady=base_pady, bg=base_function_bg, fg="white", relief = "ridge", font=base_number_font, command=lambda: clicked_equals())
button_clear = Button(frame_keypad, text="C", padx=base_padx, pady=base_pady, bg=base_function_bg, fg="white", relief = "ridge", font=base_number_font, command=lambda: clicked_clear())

# grid the buttons (written in top-down order as appears in program)
button_7.grid(row=0, column=0, sticky=base_sticky)
button_8.grid(row=0, column=1, sticky=base_sticky)
button_9.grid(row=0, column=2, sticky=base_sticky)
button_divide.grid(row=0, column=3, sticky=base_sticky)

button_4.grid(row=1, column=0, sticky=base_sticky)
button_5.grid(row=1, column=1, sticky=base_sticky)
button_6.grid(row=1, column=2, sticky=base_sticky)
button_multiply.grid(row=1, column=3, sticky=base_sticky)

button_1.grid(row=2, column=0, sticky=base_sticky)
button_2.grid(row=2, column=1, sticky=base_sticky)
button_3.grid(row=2, column=2, sticky=base_sticky)
button_subtract.grid(row=2, column=3, sticky=base_sticky)

button_0.grid(row=3, column=0, sticky=base_sticky)
button_clear.grid(row=3, column=1, sticky=base_sticky)
button_equals.grid(row=3, column=2, sticky=base_sticky)
button_add.grid(row=3, column=3, sticky=base_sticky)

## create a class that will be used to create a single object that will store the necessary info to operate the applications functinos

# create the class
class calculationInfo():
    def __init__(self): # initialize a new object
        self.tb_display_string = "" # the program starts with nothing being displayed here
        self.bb_display_string = "0" # the program starts with 0 in the bb
        self.bb_number = None
        self.tb_left_number = None
        self.tb_right_number = None
        self.current_operation = None
    def reset_variables(self):
        self.tb_display_string = "" 
        self.bb_display_string = "0" 
        self.bb_number = 0
        self.tb_left_number = None
        self.tb_right_number = None
        self.current_operation = ""
    def update_displaying_strings(self): # set the display strings in the function to what is currently being displayed
        self.tb_display_string = top_box["text"]
        self.bb_display_string = bottom_box["text"]

# create the object
info = calculationInfo()

## functinos

# helper functions
def update_tb_text(string):
    top_box.config(text=string)
def update_bb_text(string):
    bottom_box.config(text=string)

def format_tb(num, operation):
    string = str(num) + " " + operation
    update_tb_text(string)
    info.tb_display_string = string
    info.current_operation = operation
    info.tb_left_number = num

def calculate(operation, first_term, second_term):
    if (operation == "+"):
        the_sum = first_term + second_term
        return the_sum
    elif (operation == "-"):
        the_sum = first_term - second_term
        return the_sum
    elif (operation == "×"):
        the_product = first_term * second_term
        return the_product
    elif (operation == "÷"):
        if(second_term == 0):
            return "UNDEFINED"
        else:
            the_quotient = first_term / second_term
            return the_quotient
    else:
        print("Error")

def set_button_state(current_state):
    button_0.config(state=current_state)
    button_1.config(state=current_state)
    button_2.config(state=current_state)
    button_3.config(state=current_state)
    button_4.config(state=current_state)
    button_5.config(state=current_state)
    button_6.config(state=current_state)
    button_7.config(state=current_state)
    button_8.config(state=current_state)
    button_9.config(state=current_state)
    button_add.config(state=current_state)
    button_subtract.config(state=current_state)
    button_multiply.config(state=current_state)
    button_divide.config(state=current_state)
    button_equals.config(state=current_state)



# button click functions

def clicked_num(num): # what to do when a number is pressed

    # None: for when bb is displaying a numberstring but allows user to input a new value to replace the old one sitting there
    # 0: For when the bb is displaying and equals to 0, so we don't have numbers onscreen starting with zero: 067, 000, 098.0
    if (info.bb_number == None or info.bb_number == 0): 
        info.bb_number = num # sets the bb_number to the input
        update_bb_text(str(num)) # updates the bb text to display that singular digit
    else:
        # update the bb text
        # example: if 987 what previously in box and the user typed 1, the box would now display 9871
        to_display = (bottom_box["text"]) + (str(num)) # concantation of what is curerntly onscreen and number just pressed
        update_bb_text(to_display) # updates the text so that the num the user just pressed appears after
        info.bb_number = float(to_display) # updates the bb_number variable

# what happens when a user clicks an operation  (+, -, ×, ÷)
def clicked_operation(operation):
    # if there is nothing right now in the tb
    # change the tb box to show the bb-number and the plus sign
    if (info.tb_display_string == ""):
        format_tb(info.bb_number, operation)
        info.tb_left_number = info.bb_number
        info.bb_number = None
    elif ("=" in info.tb_display_string):
        format_tb(info.tb_left_number, operation)
        info.tb_left_number = info.bb_number
        info.bb_number = None
    else:
        # this steps allows the user to change their operation
        # ensures user cannot press a number once and then get a calculation
        if (info.bb_number == None):
            format_tb(info.tb_left_number, operation)
        else:
            # allows user to calculate the expressions without hitting =
            # as long as they have input two numbers
            first_term = info.tb_left_number
            second_term = info.bb_number
            solution = calculate(operation, first_term, second_term)
            if (solution == "UNDEFINED"):
                undefined()
            else:
                format_tb(solution, operation)
                update_bb_text(str(solution))
                info.bb_number = None

# clears calculator to start state
def clicked_clear():
    update_tb_text("")
    update_bb_text("0")
    info.reset_variables()

    # reset from an undefined answer
    set_button_state("normal")

def undefined():
    update_tb_text("")
    update_bb_text("UNDEFINED")
    
    # grey out all the buttons except clear
    set_button_state("disabled")
    

root.mainloop() # End