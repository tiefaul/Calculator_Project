#!Python3
import tkinter as tk

# Main application window
root = tk.Tk() # initializes the main window
root.title("Tyler's Calculator")

# Create display widget
display = tk.Entry(root, width=45, borderwidth=5) # entry widget is used to create a single-line text box
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button click functionality
def button_click(number):
    current = display.get() # Grabs the current display
    display.delete(0, tk.END)  
    display.insert(0, current + str(number))

# Back space function
def button_back():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

# Define how to clear the display
def button_clear():
    display.delete(0, tk.END)

# Define how to evaluate the expression in the display
def button_equal():
    try:
        result = str(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create the buttons
button_1 = tk.Button(root, text="1", padx=30, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=30, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=30, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=30, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=30, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=30, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=30, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=30, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=30, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=30, pady=20, command=lambda: button_click(0))
button_multiply = tk.Button(root, text="*", padx=30, pady=20, command=lambda: button_click("*"))
button_period = tk.Button(root, text=".", padx=30, pady=20, command=lambda: button_click("."))
button_add = tk.Button(root, text="+", padx=30, pady=20, command=lambda: button_click("+"))
button_subtract = tk.Button(root, text="-", padx=30, pady=20, command=lambda: button_click("-"))
button_delete = tk.Button(root, text="C", padx=30, pady=20, command=button_clear)
button_total = tk.Button(root, text="=", padx=30, pady=20, command=button_equal)
button_back = tk.Button(root, text="back", width=1, padx=30, pady=20, command=button_back)

# Place buttons on the grid

# Bottom Row
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_add.grid(row=3, column=3)

# Middle Row
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

# Top Row
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_multiply.grid(row=1, column=3)

button_0.grid(row=4, column=1)
button_delete.grid(row=4, column=0)
button_period.grid(row=4, column=2)
button_total.grid(row=4, column=3)

button_back.grid(row=5, column=0)

root.mainloop()