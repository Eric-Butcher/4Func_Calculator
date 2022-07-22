from tkinter import *
from time import sleep

root = Tk() # Start
root.resizable(False,False) # window cannot be resized
root.title("4Func Calc") # title of the windows

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
        self.tb_format = "" # can either be: "", "single", or "double"
                            # "" means the tb is displaying nothing
                            # "single" means the tb is displaying one number and the operation: 9 +, 8 =, etc.
                            # "double" means the tb is displaying two numbers, an operation, and equals: 1 + 1 =
        self.tb_l_num = None # number to the left in the top box, only number if only one is shown
        self.tb_r_num = None # number to the right of the top box, if there are two numbers shown
        self.current_operation = None # what operation is being performed in the tb
        self.bb_value = 0 # what the bb is equal to, or None if waiting for input even if there is a string there
    def reset_variables(self):
        self.tb_format = "" 
        self.tb_l_num = None 
        self.tb_r_num = None 
        self.current_operation = None 
        self.bb_value = 0 


# create the object
info = calculationInfo()

## helper functions

# update the text being shown in the top box
def update_tb_text(string):
    top_box.config(text=string)

# update the text being shown in the bottom box
def update_bb_text(string):
    bottom_box.config(text=string)

# updates the format of the tb text
def format_tb_text(format, operation):
    if (format == "single"):
        new_string = str(info.tb_l_num) + " " + operation
        update_tb_text(new_string)
        info.tb_format = "single"
        info.current_operation = operation
    elif (format == "double"):
        new_string = str(info.tb_l_num) + " " + operation + " " + str(info.tb_r_num) + " ="
        update_tb_text(new_string)
        info.tb_format = "double"
        info.current_operation = operation
    else:
        print("format_tb_text ERROR")

# returns num as int if can be int, elsewise as a float
def format_num(num):
    num = float(num)
    if num.is_integer():
        return int(num)
    else:
        return num



# calculates
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

# changes buttons other than clear on/off
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

def clicked_num(num):
    if (info.tb_format == "double"):
        clicked_clear()
        info.bb_value = num
        update_bb_text(str(num))
    elif (info.bb_value == None or info.bb_value == 0): 
        info.bb_value = num
        update_bb_text(str(num))
    else:
        new_value = bottom_box["text"] + str(num)
        new_value = float(new_value)
        new_value = format_num(new_value)
        update_bb_text(str(new_value))
        info.bb_value = new_value



def clicked_operation(operation):
    if (info.tb_format == ""):
        info.tb_l_num = info.bb_value
        info.bb_value = None
        format = "single"
        format_tb_text(format, operation)
    elif (info.tb_format == "single" and info.bb_value == None):
        format = "single"
        format_tb_text(format, operation)
    elif (info.tb_format == "single" and info.bb_value != None):
        solution = calculate(info.current_operation, info.tb_l_num, info.bb_value)
        info.tb_l_num = solution
        format = "single"
        format_tb_text(format, operation)

        info.bb_value = None
        update_bb_text(str(solution))
    elif (info.tb_format == "double"):
        info.tb_l_num = info.bb_value
        info.bb_value = None
        format_tb_text("single", operation)

def clicked_equals():
    if (info.tb_format == ""):
        info.tb_l_num = info.bb_value
        info.bb_value = None
        format = "single"
        format_tb_text(format, "=")
    elif (info.tb_format == "single" and info.current_operation == "="):
        pass
    elif (info.tb_format == "single"):
        info.tb_r_num = float(bottom_box["text"])
        info.tb_r_num = format_num(info.tb_r_num)
        format_tb_text("double", info.current_operation)
        solution = calculate(info.current_operation, info.tb_l_num, info.tb_r_num)
        solution = format_num(solution)
        update_bb_text(str(solution))
        info.bb_value = solution
    elif (info.tb_format == "double"):
        info.tb_l_num = info.bb_value
        format_tb_text("double", info.current_operation)
        solution = calculate(info.current_operation, info.tb_l_num, info.tb_r_num)
        solution = format_num(solution)
        update_bb_text(str(solution))
        info.bb_value = solution
       

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