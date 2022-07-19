from tkinter import *

root = Tk() # Start
root.title("4Func Calculator")

# create and place the entry box
entry_box = Entry(root, width=35, borderwidth=5, fg="blue", bg="grey") # entry box
entry_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10) # placement of the column

# button functions

def output(value):
    print(value)

# easy values
base_padx = 20
base_pady = 20
base_sticky = "nsew"
base_function_bg = "grey"

# create buttons

button_0 = Button(root, text="0", padx=base_padx, pady=base_pady, command=lambda: output(0))
button_1 = Button(root, text="1", padx=base_padx, pady=base_pady, command=lambda: output(1))
button_2 = Button(root, text="2", padx=base_padx, pady=base_pady, command=lambda: output(2))
button_3 = Button(root, text="3", padx=base_padx, pady=base_pady, command=lambda: output(3))
button_4 = Button(root, text="4", padx=base_padx, pady=base_pady, command=lambda: output(4))
button_5 = Button(root, text="5", padx=base_padx, pady=base_pady, command=lambda: output(5))
button_6 = Button(root, text="6", padx=base_padx, pady=base_pady, command=lambda: output(6))
button_7 = Button(root, text="7", padx=base_padx, pady=base_pady, command=lambda: output(7))
button_8 = Button(root, text="8", padx=base_padx, pady=base_pady, command=lambda: output(8))
button_9 = Button(root, text="9", padx=base_padx, pady=base_pady, command=lambda: output(9))

button_add = Button(root, text="+", padx=base_padx, pady=base_pady,bg=base_function_bg, command=lambda: output("+"))
button_subtract = Button(root, text="-", padx=base_padx, pady=base_pady, bg=base_function_bg, command=lambda: output("-"))
button_multiply = Button(root, text="×", padx=base_padx, pady=base_pady, bg=base_function_bg, command=lambda: output("×"))
button_divide = Button(root, text="÷", padx=base_padx, pady=base_pady, bg=base_function_bg, command=lambda: output("÷"))
button_equals = Button(root, text="=", padx=base_padx, pady=base_pady, bg=base_function_bg, fg="white", command=lambda: output("="))
button_clear = Button(root, text="C", padx=base_padx, pady=base_pady, bg=base_function_bg, fg="white", command=lambda: output("Cleared"))

# grid the buttons (written in top-down order as appears in program)

button_7.grid(row=1, column=0, sticky=base_sticky)
button_8.grid(row=1, column=1, sticky=base_sticky)
button_9.grid(row=1, column=2, sticky=base_sticky)
button_divide.grid(row=1, column=3, sticky=base_sticky)

button_4.grid(row=2, column=0, sticky=base_sticky)
button_5.grid(row=2, column=1, sticky=base_sticky)
button_6.grid(row=2, column=2, sticky=base_sticky)
button_multiply.grid(row=2, column=3, sticky=base_sticky)

button_1.grid(row=3, column=0, sticky=base_sticky)
button_2.grid(row=3, column=1, sticky=base_sticky)
button_3.grid(row=3, column=2, sticky=base_sticky)
button_subtract.grid(row=3, column=3, sticky=base_sticky)

button_0.grid(row=4, column=0, sticky=base_sticky)
button_clear.grid(row=4, column=1, sticky=base_sticky)
button_equals.grid(row=4, column=2, sticky=base_sticky)
button_add.grid(row=4, column=3, sticky=base_sticky)






root.mainloop() # End