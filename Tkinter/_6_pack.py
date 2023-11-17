# tkinter

# Step 1 : import tkinter
from tkinter import *


# step 2 : GUI interection
window = Tk()


# step 3 : Adding inputs
window.title("Data Science") # for add title
window.geometry("376x700")   # for add default size of window

label1 = Label(window, text="Label-1",bg="red",fg="white")
label2 = Label(window, text="Label-2",bg="blue",fg="white")
label3 = Label(window, text="Label-3",bg="green",fg="white")


label1.pack(side=TOP, fill= X, expand=False)
label2.pack(side=LEFT, fill= Y, expand=False)
label3.pack(side=RIGHT, fill= Y, expand=False)



# Step 4:Main loop
window.mainloop()