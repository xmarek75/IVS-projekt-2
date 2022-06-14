#!/usr/bin/env python3
###################################################################
# Project name: Gazorpazorp calculator
# File: gui.py
# Last change: 28.4.2021
# Authors: Stepan Bilek, Vilem Gottwald, Pavel Marek
# Description: Gui for calculator
###################################################################

##
# @file gui.py
#
# @brief GUI for calculator, uses functions from LibProcExpr.py and LibMath.py
#
# @author Stepan Bilek, Vilem Gottwald, Pavel Marek
#


import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import font as tkFont
import LibProcExpr as pe


# colors initialization
button_color = "#424242"
hbgc = "#303030"          #highlight background color
active_color = "#323232"  #under cursor color

padx_size = 26
pady_size = 8

#initializing root calculator window
root = tk.Tk()
root.title("Gazorpazorpcalc")
root.configure(bg = hbgc)
root.resizable(0, 0)

# getting path to calculator logo
path = os.path.realpath(__file__).rsplit('/', 1)
logo_location = path[0] + "/logo.png"

# fonts initialization
button_font = tkFont.Font(family = 'Helvetica', size = 22, weight = 'bold')
help_font = tkFont.Font(family = 'Helvetica', size = 15)
help_text_f = tkFont.Font(family = 'Helvetica', size = 15)

# adding logo
image = Image.open(logo_location)
image = image.resize((110, 110))
photo = ImageTk.PhotoImage(image)

logo = tk.Label(root, image = photo, borderwidth = 0)
logo.image = photo
logo.grid(row = 1, column = 0, rowspan = 2)


# label to display calculator history
ans_str = tk.StringVar()
history = tk.Label(root, textvariable=ans_str, anchor=tk.W, justify = tk.LEFT, width = 26, bg = hbgc, bd = 0, highlightbackground = hbgc, font = ('Helvetica', 20))

##
# @brief Validates input that should be written into the calculator.
#
# @param action Action that should be performed (insertion | deletion).
# @param char Character that should be added or deleted.
#
# @return True if action is valid otherwise False.
#
def validCheck(action, char):
    if action == '0':
        return True
    global ans_displayed
    allowed = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "/", "*", "-", "+", "^", "%", "!", "√"]
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]


    for i in char:
        if i not in allowed:
            return False

    if i in nums and ans_displayed:
        entry.delete(0, tk.END)
        entry.insert(tk.END, char)
        entry.after_idle(lambda: entry.configure(validate="key"))
    ans_displayed = False
    return True


# Entry screen to display current input
VC = root.register(validCheck)
entry = tk.Entry(root, justify = tk.RIGHT, validate='key', validatecommand=(VC, '%d', '%S'), width = 15, bg = "#404040", bd = 0, highlightbackground = hbgc, font = ('Helvetica', 35))
entry.focus_set()


## displayed answer indicator, if True inserting nuber into calculator entry first deletes its content
ans_displayed = False
## global variable for storing the latest result (ans button inserts its content into entry)
glob_result = ""


##
# @brief Adds number into the  calculator entry field.
# This function is called whenever number or decimal point button is pressed.
# if current content of entry is a result of calclation, the result is first deleted
#
# @param new character that will be inserted into the entry field
#
def b_num(new):
    global ans_displayed
    if ans_displayed == True:
       b_clear_empty()

    current = entry.get()
    entry.delete(0, tk.END)

    formula = str(current) + str(new)
    entry.insert(0, formula)

    ans_displayed = False
    entry.xview_moveto(1)
    return

##
# @brief Adds operator into the calculator entry field.
# This function is called whenever operator button is pressed.
# If current content of entry is a result of previous calculation, entry is first erased.
#
# @param new character that will be inserted into the entry field
#
def b_operator(new):

    global ans_displayed
    current = entry.get()
    entry.delete(0, tk.END)
    formula = str(current) + str(new)
    entry.insert(0, formula)
    ans_displayed = False
    entry.xview_moveto(1)
    return

##
# @brief Evaluates the content of entry field and replaces it with result.
# If the input is invalid prints error message into the entry field.
# Does nothing when entry field is empty.
#
# @param event Parameter that is required for keybinds, default value is None.
#
def b_equal(event=None):
    global ans_displayed
    global glob_result

    expr = entry.get()
    if len(expr) == 0:
        return
    err = False

    try:
        result = pe.solve_expr(expr)
    except ValueError:
        err = True
        result = str("Value Error")
    except ZeroDivisionError:
        err = True
        result = str("Zero division Error")
    except IndexError:
        err = True
        result = str("Value Error")

    if err:
       entry.configure(validate="none")
    else:
         glob_result = result


    ans_str.set(str(expr) + " = ")
    entry.delete(0, tk.END)
    entry.insert(0, str(result))
    if err:
        entry.configure(validate="key")
    ans_displayed = True
    return

# binding corresponding keys to equals button
root.bind('<Return>', b_equal)
root.bind('<KP_Enter>', b_equal)

##
# @brief Deletes last character of the entry.
# This function is called whenever DEL button is pressed.
#
# @param event Parameter that is required for keybinds, default value is None.
#
def b_delete(event=None):
    global ans_displayed
    if ans_displayed:
        b_clear_empty()
        return

    index = len(entry.get()) - 1
    entry.delete(index, tk.END)
    return

##
# @brief Erases entry and history.
# This function is called whenever AC button is pressed.
#
# @param event Parameter that is required for keybinds, default value is None.
#
def b_clear_empty(event=None):
    entry.delete(0, tk.END)
    ans_str.set("")
    return

# binding corresponding keys to AC button
root.bind('e',b_clear_empty)

##
# @brief Opens toplevel window with help.
# This function is called whenever Help button is pressed
#
def show_help():
    Help = tk.Toplevel(root)
    Help.title("Help")
    Help.configure(bg = button_color)
    Help.geometry("800x650")
    Help.resizable(0,0)
    Help.focus_set()

    help_text = """
Equations are entered in standart mathematical form.
For example to add 1 and 2 enter:  1+2
To solve, click on the = button or hit enter on your keyboard.

Calculations are performed in standart mathematical order:
    1. factorial (!)
    2. root (√), power (^)
    3. multiplication (*), division (/), modulo (% | button MOD)
    4. addition (+), substraction (-)

Supported input format based on operand type:
    - binary (+, -, * , /, ^, √, %) insert as - number operator number (e.g., 5+3)
    - unary (!) insert as - number operator (e.g., 5!)
        square root (√) is also supported as √x

Buttons with special function:
    - ANS\t - inserts the answer of the last calculation into the input field
    - MOD\t - inserts modulo operator % into the input field
    - AC\t - deletes the whole input field
    - DEL\t - deletes last character from the input field

Keyboard can aslo be used for input, special buttons key equivalents are:
    <button>         <key>
      ANS\t\ta\t (answer)
      AC\t\te\t  (erase)
      DEL\t       <Backspace>
      MOD\t\t%
      √\t\tr\t (root)
      =\t       <Enter> or <Return>
    """
    tk.Message(Help, text=help_text,font=help_text_f, fg="#c7c7c7", bg=button_color, justify=tk.LEFT).pack()
    return

##
# @brief Auxiliary function for ANS key binding.
# Calls function that inserts answer into entry field.
#
# @param event Parameter that is required for keybinds, default value is None.
#
def keyb_ans(event=None):
    b_num(glob_result)
    return

# binding corresponding keys to ANS button
root.bind('a',keyb_ans)

##
# @brief Auxiliary function for square root character key binding.
# Inserts √ character into entry field.
#
# @param event Parameter that is required for keybinds, default value is None.
#
def keyb_root(event=None):
    b_num("√")
    return

# binding corresponding keys to square root button
root.bind('r',keyb_root)

# creating help button in the top bar
button_help = tk.Button(root, text = "Help", font = help_font, bd = 0, activebackground = active_color, highlightbackground = hbgc, bg = hbgc, padx = padx_size, pady = pady_size, height = 1, width = 2,  command = lambda: show_help())

# number buttons
button_1 = tk.Button(root, text = "1", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(1))
button_2 = tk.Button(root, text = "2", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(2))
button_3 = tk.Button(root, text = "3", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(3))
button_4 = tk.Button(root, text = "4", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(4))
button_5 = tk.Button(root, text = "5", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(5))
button_6 = tk.Button(root, text = "6", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(6))
button_7 = tk.Button(root, text = "7", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(7))
button_8 = tk.Button(root, text = "8", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(8))
button_9 = tk.Button(root, text = "9", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(9))
button_0 = tk.Button(root, text = "0", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = 70, pady = 8, height = 2, width = 8, command = lambda: b_num(0))
button_point = tk.Button(root, text = ".", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num("."))

# operators buttons
button_plus = tk.Button(root, text = "+", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_operator("+"))
button_minus = tk.Button(root, text = "-", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_operator("-"))
button_times = tk.Button(root, text = "*", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_operator("*"))
button_divide = tk.Button(root, text= "/", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_operator("/"))
button_equal = tk.Button(root, text = "=", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_equal())
button_power = tk.Button(root, text = "^", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_operator("^"))
button_root = tk.Button(root, text = "√", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num("√")) #b_num because of ans_displayed state
button_ans = tk.Button(root, text = "ANS", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(glob_result))
button_del = tk.Button(root, text = "DEL", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_delete())
button_ac = tk.Button(root, text = "AC", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_clear_empty())
button_mod = tk.Button(root, text = "MOD", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_operator("%"))
button_fact = tk.Button(root, text = "!", font = button_font, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_operator("!"))

# griding elements to the root window
button_help.grid(row = 0, column = 0, sticky = tk.W)

history.grid(row = 1, column = 1, columnspan = 5, sticky = tk.S)

entry.grid(row = 2, column = 1, columnspan = 5, sticky = tk.N)

button_ans.grid(row = 3, column = 0)
button_mod.grid(row = 3, column = 1)
button_ac.grid(row = 3, column = 2)
button_del.grid(row = 3, column = 3)

button_power.grid(row = 4, column = 0)
button_root.grid(row = 4, column = 1)
button_fact.grid(row = 4, column = 2)
button_divide.grid(row = 4, column = 3)

button_7.grid(row = 5, column = 0)
button_8.grid(row = 5, column = 1)
button_9.grid(row = 5, column = 2)
button_times.grid(row = 5, column = 3)

button_4.grid(row = 6, column = 0)
button_5.grid(row = 6, column = 1)
button_6.grid(row = 6, column = 2)
button_minus.grid(row = 6, column = 3)

button_1.grid(row = 7, column = 0)
button_2.grid(row = 7, column = 1)
button_3.grid(row = 7, column = 2)
button_plus.grid(row = 7, column = 3)

button_0.grid(row = 8, column = 0, columnspan = 2)
button_point.grid(row = 8, column = 2)
button_equal.grid(row = 8, column = 3)

root.mainloop()





