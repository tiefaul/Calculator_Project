#!Python3

import tkinter as tk
from tkinter import ttk

# Main application window
root = tk.Tk() # initializes the main window
root.title("Tyler's Calculator")
# root.resizable(False, False) # NOTE: Comment out if you don't want the window to be resizable

# Create display widget
textbox = ttk.Entry(root, width=45) # entry widget is used to create a single-line text box
textbox.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Theme
root.tk.call("source", "azure.tcl") # Change "azure.tcl" to "Calculator_Project/azure.tcl" if you have more than one folder opened in VSCode
root.tk.call("set_theme", "dark")

# Change theme button
def change_theme():
    # NOTE: The theme's real name is azure-<mode>
    if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
        # Set light theme
        root.tk.call("set_theme", "light")
    else:
        # Set dark theme
        root.tk.call("set_theme", "dark")

# Define button click functionality
def button_click(number):
    current = textbox.get() # Grabs the current display
    textbox.delete(0, tk.END)  
    textbox.insert(0, current + str(number))

# Back space function
def button_back():
    current = textbox.get()
    textbox.delete(0, tk.END)
    textbox.insert(0, current[:-1])

# Define how to clear the display
def button_clear():
    textbox.delete(0, tk.END)

# Define how to evaluate the expression in the display
def button_equal():
    try:
        result = str(eval(textbox.get()))
        textbox.delete(0, tk.END)
        textbox.insert(0, result)
    except:
        textbox.delete(0, tk.END)
        textbox.insert(0, "Error")

# Create the buttons
button_1 = ttk.Button(root, text="1", command=lambda: button_click(1))
button_2 = ttk.Button(root, text="2", command=lambda: button_click(2))
button_3 = ttk.Button(root, text="3", command=lambda: button_click(3))
button_4 = ttk.Button(root, text="4", command=lambda: button_click(4))
button_5 = ttk.Button(root, text="5", command=lambda: button_click(5))
button_6 = ttk.Button(root, text="6", command=lambda: button_click(6))
button_7 = ttk.Button(root, text="7", command=lambda: button_click(7))
button_8 = ttk.Button(root, text="8", command=lambda: button_click(8))
button_9 = ttk.Button(root, text="9", command=lambda: button_click(9))
button_0 = ttk.Button(root, text="0", command=lambda: button_click(0))
button_multiply = ttk.Button(root, text="*", command=lambda: button_click("*"))
button_period = ttk.Button(root, text=".", command=lambda: button_click("."))
button_add = ttk.Button(root, text="+", command=lambda: button_click("+"))
button_divide = ttk.Button(root, text="/", command=lambda: button_click("/"))
button_subtract = ttk.Button(root, text="-", command=lambda: button_click("-"))
button_delete = ttk.Button(root, text="C", command=button_clear)
button_total = ttk.Button(root, text="=", command=button_equal)
button_remove = ttk.Button(root, text="back", width=1, command=button_back)
button_theme= ttk.Button(root, text="Theme", width=1, command=change_theme)

# Place buttons on the grid

# Bottom Row
button_1.grid(row=3, padx=3, pady=3, column=0, sticky="nsew")
button_2.grid(row=3, padx=3, pady=3, column=1, sticky="nsew")
button_3.grid(row=3, padx=3, pady=3, column=2, sticky="nsew")
button_add.grid(row=3, padx=3, pady=3, column=3, sticky="nsew")

# Middle Row
button_4.grid(row=2, padx=3, pady=3, column=0, sticky="nsew")
button_5.grid(row=2, padx=3, pady=3, column=1, sticky="nsew")
button_6.grid(row=2, padx=3, pady=3, column=2, sticky="nsew")
button_subtract.grid(row=2, padx=3, pady=3, column=3, sticky="nsew")

# Top Row
button_7.grid(row=1, padx=3, pady=3, column=0, sticky="nsew")
button_8.grid(row=1, padx=3, pady=3, column=1, sticky="nsew")
button_9.grid(row=1, padx=3, pady=3, column=2, sticky="nsew")
button_multiply.grid(row=1, padx=3, pady=3, column=3, sticky="nsew")

button_0.grid(row=4,padx=3, pady=3, column=1, sticky="nsew")
button_delete.grid(row=4, padx=3, pady=3, column=0, sticky="nsew")
button_period.grid(row=4, padx=3, pady=3, column=2, sticky="nsew")
button_total.grid(row=5, padx=3, pady=3, column=3, sticky="nsew")

button_remove.grid(row=5, ipadx=32, pady=3, column=0, sticky="nsew")
button_divide.grid(row=4, padx=3, pady=3, column=3, sticky="nsew")
button_theme.grid(row=0,column=5, padx=10, pady=10, ipadx=20, sticky="nsew")

root.mainloop()