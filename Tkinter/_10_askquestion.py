# Step 1 : import tkinter
from tkinter import *
import tkinter.messagebox

# step 2 : GUI interection
window = Tk()


# step 3 : Adding input

#question = tkinter.messagebox.askyesno("Weather","Will it rain")
#if question==True:
#    print("Yes, It will rain take an umbrella")
#else:
#    print("No, It won't rain don't forget your sunscreen")
    
#tkinter.messagebox.askquestion("What is your name?","name")
tkinter.messagebox.askyesnocancel("Married","Enter your choice")
# Step 4:Main loop
window.mainloop()