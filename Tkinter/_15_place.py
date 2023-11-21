# Step 1 : import tkinter
from tkinter import *
import tkinter.messagebox

# step 2 : GUI interection
window = Tk()
window.geometry("500x500")


# step 3 : Adding input
button = Button(window, text="button", width=12)
button.place(x=250,y=25)

# Step 4:Main loop
window.mainloop()