# Step 1 : import tkinter
from tkinter import *
import tkinter.messagebox

# step 2 : GUI interection
window = Tk()
window.geometry("500x500")


# step 3 : Adding input
message = Message(window,text="python", relief=RAISED)
message.pack()

# passing variable
var = StringVar()
message = Message(window, textvariable=var, relief=RAISED, padx=20, pady=20)
var.set("Welcome")
message.pack()

#creating a button and adding it to the window
'''var = StringVar()
ent_var= StringVar()
def insert():
    result = ent_var.get()
    var.set(result)


message = Message(window, textvariable=var, relief=RAISED,padx=50,pady=50)
entry = Entry(window, textvariable=ent_var)
button = Button(window, text="OK", command=insert)
message.pack()
entry.pack()
button.pack()'''


# Step 4:Main loop
window.mainloop()