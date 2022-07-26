import tkinter as tk

root = tk.Tk()  # Start
root.resizable(False, False)  # window cannot be resized
root.title("4Func Calc")  # title of the windows

# easy values
BASE_PADX = 20
BASE_PADY = 20
BASE_STICKY = "nsew"
BASE_FUNCTION_BG = "grey"
BASE_FUNCTION_RELIEF = "groove"
BASE_NUMBER_RELIEF = "raised"
BASE_NUMBER_FONT = ("Segoe UI", 9, "normal")

## create the two main frames for this application

# frame for theboxes showing numbers
frame_boxes = tk.Frame(root)
frame_boxes.grid(sticky="ew")

# frames for the clickable keys
frame_keypad = tk.Frame(root)
frame_keypad.grid(sticky="nsew")

## create the display boxes

# create the display box for showing information above the entry
top_box = tk.Label(
    frame_boxes,
    fg="blue",
    bg="grey",
    relief="ridge",
    font=BASE_NUMBER_FONT,
    anchor="e",
    text="",
)
top_box.pack(side="top", fill="x")

# create and place the entry box
bottom_box = tk.Label(
    frame_boxes,
    fg="blue",
    bg="grey",
    relief="ridge",
    font=("Segoe UI", 14, "normal"),
    anchor="e",
    text="0",
)  # entry box
bottom_box.pack(side="bottom", fill="x")  # placement of the column

## create the clickable buttons

# create number buttons
button_0 = tk.Button(
    frame_keypad,
    text="0",
    padx=BASE_PADX,
    pady=BASE_PADY,
    relief=BASE_NUMBER_RELIEF,
    font=BASE_NUMBER_FONT,
    command=lambda: clicked_num(0),
)
button_1 = tk.Button(
    frame_keypad,
    text="1",
    padx=BASE_PADX,
    pady=BASE_PADY,
    relief=BASE_NUMBER_RELIEF,
    font=BASE_NUMBER_FONT,
    command=lambda: clicked_num(1),
)
button_2 = tk.Button(
    frame_keypad,
    text="2",
    padx=BASE_PADX,
    pady=BASE_PADY,
    relief=BASE_NUMBER_RELIEF,
    font=BASE_NUMBER_FONT,
    command=lambda: clicked_num(2),
)
button_3 = tk.Button(
    frame_keypad,
    text="3",
    padx=BASE_PADX,
    pady=BASE_PADY,
    relief=BASE_NUMBER_RELIEF,
    font=BASE_NUMBER_FONT,
    command=lambda: clicked_num(3),
)
button_4 = tk.Button(
    frame_keypad,
    text="4",
    padx=BASE_PADX,
    pady=BASE_PADY,
    relief=BASE_NUMBER_RELIEF,
    font=BASE_NUMBER_FONT,
    command=lambda: clicked_num(4),
)
button_5 = tk.Button(
    frame_keypad,
    text="5",
    padx=BASE_PADX,
    pady=BASE_PADY,
    relief=BASE_NUMBER_RELIEF,
    font=BASE_NUMBER_FONT,
    command=lambda: clicked_num(5),
)
button_6 = tk.Button(
    frame_keypad,
    text="6",
    padx=BASE_PADX,
    pady=BASE_PADY,
    relief=BASE_NUMBER_RELIEF,
    font=BASE_NUMBER_FONT,
    command=lambda: clicked_num(6),
)
button_7 = tk.Button(
    frame_keypad,
    text="7",
    padx=BASE_PADX,
    pady=BASE_PADY,
    relief=BASE_NUMBER_RELIEF,
    font=BASE_NUMBER_FONT,
    command=lambda: clicked_num(7),
)
button_8 = tk.Button(
    frame_keypad,
    text="8",
    padx=BASE_PADX,
    pady=BASE_PADY,
    relief=BASE_NUMBER_RELIEF,
    font=BASE_NUMBER_FONT,
    command=lambda: clicked_num(8),
)
button_9 = tk.Button(
    frame_keypad,
    text="9",
    padx=BASE_PADX,
    pady=BASE_PADY,
    relief=BASE_NUMBER_RELIEF,
    font=BASE_NUMBER_FONT,
    command=lambda: clicked_num(9),
)

# create operation buttons
button_add = tk.Button(
    frame_keypad,
    text="+",
    padx=BASE_PADX,
    pady=BASE_PADY,
    bg=BASE_FUNCTION_BG,
    relief=BASE_FUNCTION_RELIEF,
    font=BASE_NUMBER_FONT,
    command=lambda: clicked_operation("+"),
)
button_subtract = tk.Button(
    frame_keypad,
    text="-",
    padx=BASE_PADX,
    pady=BASE_PADY,
    bg=BASE_FUNCTION_BG,
    relief=BASE_FUNCTION_RELIEF,
    font=BASE_NUMBER_FONT,
    command=lambda: clicked_operation("-"),
)
button_multiply = tk.Button(
    frame_keypad,
    text="×",
    padx=BASE_PADX,
    pady=BASE_PADY,
    bg=BASE_FUNCTION_BG,
    relief=BASE_FUNCTION_RELIEF,
    font=BASE_NUMBER_FONT,
    command=lambda: clicked_operation("×"),
)
button_divide = tk.Button(
    frame_keypad,
    text="÷",
    padx=BASE_PADX,
    pady=BASE_PADY,
    bg=BASE_FUNCTION_BG,
    relief=BASE_FUNCTION_RELIEF,
    font=BASE_NUMBER_FONT,
    command=lambda: clicked_operation("÷"),
)
button_equals = tk.Button(
    frame_keypad,
    text="=",
    padx=BASE_PADX,
    pady=BASE_PADY,
    bg=BASE_FUNCTION_BG,
    fg="white",
    relief="ridge",
    font=BASE_NUMBER_FONT,
    command=lambda: clicked_equals(),
)
button_clear = tk.Button(
    frame_keypad,
    text="C",
    padx=BASE_PADX,
    pady=BASE_PADY,
    bg=BASE_FUNCTION_BG,
    fg="white",
    relief="ridge",
    font=BASE_NUMBER_FONT,
    command=lambda: clicked_clear(),
)

# grid the buttons (written in top-down order as appears in program)
button_7.grid(row=0, column=0, sticky=BASE_STICKY)
button_8.grid(row=0, column=1, sticky=BASE_STICKY)
button_9.grid(row=0, column=2, sticky=BASE_STICKY)
button_divide.grid(row=0, column=3, sticky=BASE_STICKY)

button_4.grid(row=1, column=0, sticky=BASE_STICKY)
button_5.grid(row=1, column=1, sticky=BASE_STICKY)
button_6.grid(row=1, column=2, sticky=BASE_STICKY)
button_multiply.grid(row=1, column=3, sticky=BASE_STICKY)

button_1.grid(row=2, column=0, sticky=BASE_STICKY)
button_2.grid(row=2, column=1, sticky=BASE_STICKY)
button_3.grid(row=2, column=2, sticky=BASE_STICKY)
button_subtract.grid(row=2, column=3, sticky=BASE_STICKY)

button_0.grid(row=3, column=0, sticky=BASE_STICKY)
button_clear.grid(row=3, column=1, sticky=BASE_STICKY)
button_equals.grid(row=3, column=2, sticky=BASE_STICKY)
button_add.grid(row=3, column=3, sticky=BASE_STICKY)

## create a class that will be used to create a single object that will store the necessary info to operate the applications functinos

# create the class
class CalculationInfo:
    def __init__(self):  # initialize a new object
        self.tb_format = ""  # can either be: "", "single", or "double"
        # "" means the tb is displaying nothing
        # "single" means the tb is displaying one number and the operation: 9 +, 8 =, etc.
        # "double" means the tb is displaying two numbers, an operation, and equals: 1 + 1 =
        self.tb_left_num = (
            None  # number to the left in the top box, only number if only one is shown
        )
        self.tb_right_num = (
            None  # number to the right of the top box, if there are two numbers shown
        )
        self.current_operation = None  # what operation is being performed in the tb
        self.bb_value = 0  # what the bb is equal to, or None if waiting for input even if there is a string there

    def reset_variables(self):
        self.tb_format = ""
        self.tb_left_num = None
        self.tb_right_num = None
        self.current_operation = None
        self.bb_value = 0


# create the object
info = CalculationInfo()

## helper functions

# update the text being shown in the top box
def update_tb_text(string):
    top_box.config(text=string)


# update the text being shown in the bottom box
def update_bb_text(string):
    bottom_box.config(text=string)


# updates the format of the tb text
def format_tb_text(format, operation):
    if format == "single":
        new_string = str(info.tb_left_num) + " " + operation
        update_tb_text(new_string)
        info.tb_format = "single"
        info.current_operation = operation
    elif format == "double":
        new_string = (
            str(info.tb_left_num) + " " + operation + " " + str(info.tb_right_num) + " ="
        )
        update_tb_text(new_string)
        info.tb_format = "double"
        info.current_operation = operation
    else:
        print("format_tb_text ERROR")


# returns num as int if can be int, elsewise as a float
def format_num(num):
    if num == "UNDEFINED" or num == "OVERFLOW":
        pass
    else:
        num = float(num)
        if num.is_integer():
            return int(num)
        else:
            return num


# checks if the calculation is too big for this calculator's UI to handle
def check_too_long(num):
    numstring = str(num)
    if len(numstring) >= 22:
        return True
    else:
        return False


# calculates
# if the operation performes a number that is too large than it
# returns OVERFLOW which will brick the calculator with that error
# else it will return the solution
def calculate(operation, first_term, second_term):
    if operation == "+":
        the_sum = first_term + second_term
        if check_too_long(the_sum):
            return "OVERFLOW"
        else:
            return the_sum
    elif operation == "-":
        the_sum = first_term - second_term
        if check_too_long(the_sum):
            return "OVERFLOW"
        else:
            return the_sum
    elif operation == "×":
        the_product = first_term * second_term
        if check_too_long(the_product):
            return "OVERFLOW"
        else:
            return the_product
    elif operation == "÷":
        # check for divide by zero
        if second_term == 0:
            return "UNDEFINED"
        else:
            the_quotient = first_term / second_term
            if check_too_long(the_quotient):
                return "OVERFLOW"
            else:
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


# when any of the number buttons are clicked
def clicked_num(num):
    # if the top box is already displaying a full calculation
    # example: 9 + 9 =
    # then clicking a number button will clear the top box and write that
    # new number to the bottom box
    if info.tb_format == "double":
        clicked_clear()
        info.bb_value = num
        update_bb_text(str(num))
    # anytime that clicking a number button will replace what is
    # currently being shown in the bottom box
    # example would be at start (or after clear) when the bottom box
    # displays 0, or after the user has pressed 3 and x, top box will
    # be showing 3 x, but the bottom box will still be showing 3.
    # this allows the user to simply press the new number and have that
    # 3 be replaced
    elif info.bb_value == None or info.bb_value == 0:
        info.bb_value = num
        update_bb_text(str(num))
    # will not place more numbers into the input if the number is getting
    # too long for this calculator to handle from a UI and accuracy perspective
    elif (len(bottom_box["text"])) >= 11:
        pass
    # when numbers are being added to the numberstring input
    # example: user already has 34 in bottom box, clicks 9,
    # bottom box now shows 349
    else:
        new_value = bottom_box["text"] + str(num)
        new_value = float(new_value)
        new_value = format_num(new_value)
        update_bb_text(str(new_value))
        info.bb_value = new_value


def clicked_operation(operation):

    # when nothing is being displayed in the top box,
    # take the number in the bottom box and make it the
    # left number in the top box with the operation chosen
    # example: user pressed 5 +, top box now shows 5 +
    if info.tb_format == "":
        info.tb_left_num = info.bb_value
        info.bb_value = None
        format = "single"
        format_tb_text(format, operation)

    # take the number in the bottom box and put in a single formatted top box
    # with the current operation when the box is showing 0 =, and user has
    # put a number into bottom box
    elif info.tb_format == "single" and info.current_operation == "=":
        info.tb_left_num = format_num(bottom_box["text"])
        format_tb_text("single", operation)


    # if the top box is currently showing something like 5 +
    # and the user pressed an operation without hitting a number key to input a number,
    # the operation will change
    # example: starts at 5 +, user presses x, now 5 x
    elif info.tb_format == "single" and info.bb_value == None:
        format = "single"
        format_tb_text(format, operation)

    # if the top box is currently showing something like 5 + and the user
    # pressed a number key to input a value, and they press an operation key,
    # perform that operation and return the result to the top box as the left number
    # example: 5 + in top box, user pressed 3 so bottom box displays 3. After hitting the
    # plus sign again the top box will display 8 + and 8 in the bottom box
    elif info.tb_format == "single" and info.bb_value != None:
        solution = calculate(info.current_operation, info.tb_left_num, info.bb_value)
        if is_not_solution(solution):
            cannot_calculate(solution)
        else:
            info.tb_left_num = solution
            format = "single"
            format_tb_text(format, operation)

            info.bb_value = None
            update_bb_text(str(solution))

    # if the top box is currently displaying something like 5 + 3 =
    # and the user presses an operation (let's say +), format the top
    # box as 8 +
    elif info.tb_format == "double":
        info.tb_left_num = info.bb_value
        info.bb_value = None
        format_tb_text("single", operation)


def clicked_equals():

    # if there is nothing in the top box and the
    # user presses =, take the value in the bottom box
    # and put it as the top left number in the top box
    # with the equal sign
    if info.tb_format == "":
        info.tb_left_num = info.bb_value
        info.bb_value = None
        format = "single"
        format_tb_text(format, "=")

    # if the top box is already displaying something like 5 =
    # and the user presses equals again, do nothing
    elif info.tb_format == "single" and info.current_operation == "=":
        pass

    # if the top box is displaying something like 5 +,
    # perform that calculation with the number in the
    # bottom box and change the top box to show the previous
    # number in the bottom box and change the bottom box number to the result
    elif info.tb_format == "single":
        info.tb_right_num = float(bottom_box["text"])
        info.tb_right_num = format_num(info.tb_right_num)
        format_tb_text("double", info.current_operation)
        solution = calculate(info.current_operation, info.tb_left_num, info.tb_right_num)
        if is_not_solution(solution):
            cannot_calculate(solution)
        else:
            solution = format_num(solution)
            update_bb_text(str(solution))
            info.bb_value = solution

    # if the top box is already showing something like 5 + 5 =,
    # peform the operation and make the result the top left number in the
    # top box
    elif info.tb_format == "double":
        info.tb_left_num = info.bb_value
        format_tb_text("double", info.current_operation)
        solution = calculate(info.current_operation, info.tb_left_num, info.tb_right_num)
        if is_not_solution(solution):
            cannot_calculate(solution)
        else:
            solution = format_num(solution)
            update_bb_text(str(solution))
            info.bb_value = solution


# clears calculator to start state
def clicked_clear():
    update_tb_text("")
    update_bb_text("0")
    info.reset_variables()

    # reset from an undefined/overflow answer
    set_button_state("normal")


# checks to see if the solution is
# a valid number solution
def is_not_solution(solution):
    not_correct = ["UNDEFINED", "OVERFLOW"]
    if solution in not_correct:
        return True
    else:
        return False


# function that disables calculator in case
# of an OVERFLOW or UNDEFINED
def cannot_calculate(message):
    update_tb_text("")
    update_bb_text(str(message))

    # grey out  and deactivate all the buttons except clear
    set_button_state("disabled")


root.mainloop()  # End
