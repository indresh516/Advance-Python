# tkinter

# Step 1 : import tkinter
from tkinter import *


# step 2 : GUI interection
window = Tk()


# step 3 : Adding inputs
window.title("isit")
window.geometry("500x700")
window.config(bg="SeaShell")
frame1 = Frame(window, bg="blue",width=300, height=300,cursor="spider")
frame2 = Frame(window, bg="green",width=300, height=300, cursor="dotbox")
frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)

# Step 4:Main loop
window.mainloop()