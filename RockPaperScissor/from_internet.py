import tkinter as tk
from tkinter import ttk


# Function to check if the entry is empty
def check_entry():
    if entry.get() == "":
        result_label.config(text="The entry field is empty!")
    else:
        result_label.config(text=f"Entry content: {entry.get()}")


# Create the main window
root = tk.Tk()
root.title("Grid Expand Example")
root.geometry("400x200")  # Set the geometry of the window

# Configure grid to expand widgets
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

# Create an Entry widget
entry = ttk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Create a button to trigger the check
check_button = ttk.Button(root, text="Check Entry", command=check_entry)
check_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Create a label to display the result
result_label = ttk.Label(root, text="")
result_label.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# Run the application
root.mainloop()

################################################################
# Resizing image codes

# from tkinter import *
# from PIL import Image, ImageTk
#
# # from tkinter.ttk import *
#
# # creating tkinter window
# root = Tk()
#
# # Adding widgets to the root window
# Label(root, text='GeeksforGeeks', font=(
#     'Verdana', 15)).pack(side=TOP, pady=10)
#
# # Creating a photoimage object to use image
# image = Image.open(r"images/rock.png")
# image = image.resize((110, 110))
# photo = ImageTk.PhotoImage(image)
#
# # here, image option is used to
# # set image on button
# Button(root, text='Click Me !', image=photo, height=110,
#        width=110).pack(
#     side=TOP)
#
# mainloop()
