# Step 1 : import tkinter
from tkinter import *


# step 2 : GUI interection
window = Tk()


# step 3 : Adding inputs
window.title("isit")
window.geometry("400x300")

label1 = Label(window, text="mail")
label2= Label(window, text="Password")

e1 = Entry(window, width=40,borderwidth=2)
e2 = Entry(window, width=40,borderwidth=2)


label1.grid(row=0,column=1)
label2.grid(row=1,column=1)
e1.grid(row=0, column=2)
e2.grid(row=1, column=2)




# Step 4:Main loop
window.mainloop()