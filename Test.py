import tkinter as tk

# Main application window
root = tk.Tk() # initializes the main window
root.title("Tyler's Calculator")

# Create display widget
display = tk.Entry(root, width=45, borderwidth=5) # entry widget is used to create a single-line text box
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

display.get()

root.mainloop()