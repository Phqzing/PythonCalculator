from tkinter import *


window = Tk()


#Title and other basic stuff
window.title("Calculator")
window.geometry("440x379") # "384x396"
window.resizable(0, 0)


def click(item):
    global equation
    equation = equation + str(item)
    display.set(equation)

def clear_screen():
    global equation
    equation = ""
    display.set("")\

def display_answer():
    global equation
    answer = str(eval(equation))
    display.set(answer)
    equation = ""

equation = ""


# Display
display = StringVar()

display_frame = Frame(window, width = 422, height = 50, bd = 0)
display_frame.pack(side = TOP)

input = Entry(display_frame, font = ("Times New Roman", 18, "bold"), textvariable = display, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
input.grid(row = 0, column = 0)
input.pack(ipady = 10)


# Buttons
button_body_frame = Frame(window, width = 312, height = 272)
button_body_frame.pack()

# First row of buttons
clear_button = Button(button_body_frame, text = "Clear", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda:clear_screen())
clear_button.grid(row = 0, column = 0, padx = 1, pady = 1)

b1_button = Button(button_body_frame, text = "(", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda:click("("))
b1_button.grid(row = 0, column = 1, padx = 1, pady = 1)

b2_button = Button(button_body_frame, text = ")", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda:click(")"))
b2_button.grid(row = 0, column = 2, padx = 1, pady = 1)

divide_button = Button(button_body_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:click("/"))
divide_button.grid(row = 0, column = 3, padx = 1, pady = 1)

# Second row of buttons
seven_button = Button(button_body_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda:click("7"))
seven_button.grid(row = 1, column = 0, padx = 1, pady = 1)

eight_button = Button(button_body_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda:click("8"))
eight_button.grid(row = 1, column = 1, padx = 1, pady = 1)

nine_button = Button(button_body_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda:click("9"))
nine_button.grid(row = 1, column = 2, padx = 1, pady = 1)

multiply_button = Button(button_body_frame, text = "x", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:click("*"))
multiply_button.grid(row = 1, column = 3, padx = 1, pady = 1)

# Third row of buttons
six_button = Button(button_body_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda:click("6"))
six_button.grid(row = 2, column = 0, padx = 1, pady = 1)

five_button = Button(button_body_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda:click("5"))
five_button.grid(row = 2, column = 1, padx = 1, pady = 1)

four_button = Button(button_body_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda:click("4"))
four_button.grid(row = 2, column = 2, padx = 1, pady = 1)

sub_button = Button(button_body_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:click("-"))
sub_button.grid(row = 2, column = 3, padx = 1, pady = 1)

# Fourth row of buttons
three_button = Button(button_body_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda:click("3"))
three_button.grid(row = 3, column = 0, padx = 1, pady = 1)

two_button = Button(button_body_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda:click("2"))
two_button.grid(row = 3, column = 1, padx = 1, pady = 1)

one_button = Button(button_body_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda:click("1"))
one_button.grid(row = 3, column = 2, padx = 1, pady = 1)

add_button = Button(button_body_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:click("+"))
add_button.grid(row = 3, column = 3, padx = 1, pady = 1)

# Fifth row of buttons
zero_button = Button(button_body_frame, text = "0", fg = "black", width = 24, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda:click("0"))
zero_button.grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)

dot_button = Button(button_body_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda:click("."))
dot_button.grid(row = 4, column = 2, padx = 1, pady = 1)

equals_button = Button(button_body_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:display_answer())
equals_button.grid(row = 4, column = 3, padx = 1, pady = 1)



window.mainloop()