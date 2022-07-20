from tkinter import *

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

# create the two main frames for this application
frame_boxes = Frame(root)
frame_boxes.grid(sticky="ew")

frame_keypad = Frame(root)
frame_keypad.grid(sticky="nsew")

# create and place the entry box
#b: entry_box = Label(frame_boxes, width=20, height=1, borderwidth=5, fg="blue", bg="grey", relief="ridge", font = ("Segoe UI", 14, "normal"), anchor="e", text="entry") # entry box

entry_box = Label(frame_boxes, fg="blue", bg="grey", relief="ridge", font = ("Segoe UI", 14, "normal"), anchor="e", text="0") # entry box
entry_box.pack(side="bottom", fill="x") # placement of the column

# create the display box for showing information above the entry 
# b: display_box = Label(frame_boxes, width=32, borderwidth=5, fg="blue", bg="grey", relief="ridge", font=base_number_font, anchor="e", text="Hello World!")
# b: display_box.grid(row=0, column=0, padx=10, pady=0)

display_box = Label(frame_boxes, fg="blue", bg="grey", relief="ridge", font=base_number_font, anchor="e", text="")
display_box.pack(side="top", fill="x")

# button functions

def clicked(value):
    current = entry_box["text"]
    if(current == "0"):
        update_entry_box(value)
    else:
        updated = current + value
        update_entry_box(updated)

def calculate():
    update_entry_box("Calculated!")

def update_entry_box(info):
    entry_box.config(text=info)

def update_display_box(info):
    display_box.config(text=info)

def clear_boxes():
    update_entry_box("0")
    update_display_box("")








# create buttons

button_0 = Button(frame_keypad, text="0", padx=base_padx, pady=base_pady, relief = base_number_relief, font=base_number_font, command=lambda: clicked("0"))
button_1 = Button(frame_keypad, text="1", padx=base_padx, pady=base_pady, relief = base_number_relief, font=base_number_font, command=lambda: clicked("1"))
button_2 = Button(frame_keypad, text="2", padx=base_padx, pady=base_pady, relief = base_number_relief, font=base_number_font, command=lambda: clicked("2"))
button_3 = Button(frame_keypad, text="3", padx=base_padx, pady=base_pady, relief = base_number_relief, font=base_number_font, command=lambda: clicked("3"))
button_4 = Button(frame_keypad, text="4", padx=base_padx, pady=base_pady, relief = base_number_relief, font=base_number_font, command=lambda: clicked("4"))
button_5 = Button(frame_keypad, text="5", padx=base_padx, pady=base_pady, relief = base_number_relief, font=base_number_font, command=lambda: clicked("5"))
button_6 = Button(frame_keypad, text="6", padx=base_padx, pady=base_pady, relief = base_number_relief, font=base_number_font, command=lambda: clicked("6"))
button_7 = Button(frame_keypad, text="7", padx=base_padx, pady=base_pady, relief = base_number_relief, font=base_number_font, command=lambda: clicked("7"))
button_8 = Button(frame_keypad, text="8", padx=base_padx, pady=base_pady, relief = base_number_relief, font=base_number_font, command=lambda: clicked("8"))
button_9 = Button(frame_keypad, text="9", padx=base_padx, pady=base_pady, relief = base_number_relief, font=base_number_font, command=lambda: clicked("9"))

button_add = Button(frame_keypad, text="+", padx=base_padx, pady=base_pady,bg=base_function_bg, relief = base_function_relief, font=base_number_font, command=lambda: clicked("+"))
button_subtract = Button(frame_keypad, text="-", padx=base_padx, pady=base_pady, bg=base_function_bg, relief = base_function_relief, font=base_number_font, command=lambda: clicked("-"))
button_multiply = Button(frame_keypad, text="×", padx=base_padx, pady=base_pady, bg=base_function_bg, relief = base_function_relief, font=base_number_font, command=lambda: clicked("×"))
button_divide = Button(frame_keypad, text="÷", padx=base_padx, pady=base_pady, bg=base_function_bg, relief = base_function_relief, font=base_number_font, command=lambda: clicked("÷"))
button_equals = Button(frame_keypad, text="=", padx=base_padx, pady=base_pady, bg=base_function_bg, fg="white", relief = "ridge", font=base_number_font, command=calculate)
button_clear = Button(frame_keypad, text="C", padx=base_padx, pady=base_pady, bg=base_function_bg, fg="white", relief = "ridge", font=base_number_font, command=clear_boxes)

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






root.mainloop() # End