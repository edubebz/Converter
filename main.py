## Converts units of centimeters to inches with a basic GUI
from tkinter import *
from tkinter import ttk

# Calculating the result
def calculate(*args):
    try:
        value = float(centimeters.get())
        print(value)
        inches.set(round(value / 2.54, 2))
    except ValueError:
        pass

### Creating the program window
# Initializes the window, gives it a name
root = Tk()
root.title("Centimeters to Inches")

## Creating a frame widget - this holds the content of the UI.
# Grid works by using column/rows and placing widgets inside those coordinates
mainframe = ttk.Frame(root, borderwidth=1, padding="12 3 12 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Creating the centimeter entry widget (box)
centimeters = StringVar()
centimeters_entry = ttk.Entry(mainframe, width=8, textvariable=centimeters)
centimeters_entry.grid(column=2, row=1, sticky=(W, E))

# Creating the context text
ttk.Label(mainframe, text="centimeters is ").grid(column=3, row=1, sticky=(W, E))

## Creating the other widgets to place the other elements of the window
# Creating the buttons
ttk.Button(mainframe, text="Exit", command=root.destroy).grid(column=4, row=3, sticky=W)
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# Creating the result
inches = StringVar()
ttk.Label(mainframe, textvariable=inches).grid(column=4, row=1)
ttk.Label(mainframe, text="inches.").grid(column=5, row=1, sticky=(W))

# Padding - adding a bit around the widgets to clean up the look
for child in mainframe.winfo_children():
    child.grid_configure(padx=1, pady=5)
centimeters_entry.focus()
root.bind("<Return>", calculate)

# Opens the window
root.mainloop()

#create a dropdown for different conversions