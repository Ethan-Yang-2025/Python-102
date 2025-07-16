#### Rectangle Calculator by Pollakrid ####

import tkinter
from tkinter import ttk

#### UI ####
# Main window
app = tkinter.Tk()
app.title("Rectangle Calculator")
app.geometry("300x500")
app.resizable(False, False)
app.configure(bg="black")

# Title
title = tkinter.Label(app, text="Rectangle\nCalculator", font=("Lucida Console", 24, "bold"), bg="black", 
                      fg="white")
title.pack(pady=20)

# Unit selection
unit_label = tkinter.Label(app, text="Unit:", font=("Lucida Console", 14), bg="black", fg="white")
unit_label.pack(anchor="w", padx=20)

unit_var = tkinter.StringVar()
unitlist = ["___", "meters", "feet", "inches", "centimeters"]
unit_dropdown = ttk.Combobox(app, textvariable=unit_var, values=unitlist, width=26)
unit_dropdown.pack(pady=5)

# Width entry
width_label = tkinter.Label(app, text="Width:", font=("Lucida Console", 14), bg="black", fg="white")
width_label.pack(anchor="w", padx=20, pady=(20,5))
width_entry = tkinter.Entry(app, width=30)
width_entry.pack()

# Length entry
length_label = tkinter.Label(app, text="Length:", font=("Lucida Console", 14), bg="black", fg="white")
length_label.pack(anchor="w", padx=20, pady=(20,5))
length_entry = tkinter.Entry(app, width=30)
length_entry.pack()

# Reset button
def reset_app():
    unit_var.set("")
    width_entry.delete(0, tkinter.END) # Clear width entry (0 = first character, tkinter.END = last character)
    length_entry.delete(0, tkinter.END) # Clear length entry (0 = first character, tkinter.END = last character)
    result_label.config(text=f"Result:\n0 sq.{unit_var.get() or '___'}")
    result_frame.pack(side="bottom", fill ="x")
    error_frame.pack_forget() # Hide error frame

reset_btn = tkinter.Button(app, text="Reset", font=("Lucida Console", 12), width=20, command=reset_app)
reset_btn.pack(pady=35)

# Result frame
result_frame = tkinter.Frame(app, bg="#90EE90", width=300, height=100)
result_frame.pack(side="bottom", fill ="x")

result_label = tkinter.Label(result_frame, text="Result:\n0 sq.___", font=("Lucida Console", 14), 
                             bg="#90EE90")
result_label.pack(pady=20)

# Error frame (initially hidden)
error_frame = tkinter.Frame(app, bg="#ff4444", width=300, height=100)

error_label = tkinter.Label(error_frame, text="Error:\nPress Reset", font=("Lucida Console", 14), 
                            bg="#ff4444")
error_label.pack(pady=20)

#### Backend ####
# Function for calculating area and updating the UI
def calculate(event=None): # When called by event binding, Tkinter passes an event object
    width = float(width_entry.get() or 0)  # Get width, default to 0 if empty
    length = float(length_entry.get() or 0) # Get length, default to 0 if empty
    unit = unit_var.get() or "___"
    area = width * length

    if width >= 0 and length >= 0:
        result_label.config(text=f"Result:\n{area} sq.{unit}")
        result_frame.pack(side="bottom", fill ="x")
        error_frame.pack_forget()

    else:
        result_frame.pack_forget()
        error_frame.pack(side="bottom", fill ="x")

# Bind calculate function to entry widgets
width_entry.bind('<KeyRelease>', calculate)
length_entry.bind('<KeyRelease>', calculate)
unit_dropdown.bind('<<ComboboxSelected>>', calculate)

# Run the app
app.mainloop()