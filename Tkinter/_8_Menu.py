# Step 1 : import tkinter
from tkinter import *


# step 2 : GUI interection
window = Tk()


# step 3 : Adding inputs

menu = Menu(window)
file = Menu(menu, tearoff=0)
edit = Menu(menu, tearoff=0)

file.add_command(label="New")
file.add_command(label="Open")
file.add_separator()
file.add_command(label="Save")
file.add_command(label="Save As")

edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_separator()
edit.add_command(label="Paste")
edit.add_command(label="Paste Special")
edit.add_separator()
edit.add_command(label="Find")
edit.add_command(label="Replace")
edit.add_command(label="Goto")

file.add_separator()
file.add_command(label="Exit", command = window.quit) # 

menu.add_cascade(label="File",menu=file)
window.config(menu=menu)
menu.add_cascade(label="Edit",menu = edit)
window.config(menu=menu)


# Step 4:Main loop
window.mainloop()