# Step 1 : import tkinter
from tkinter import *
import tkinter.messagebox

# step 2 : GUI interection
window = Tk()


# step 3 : Adding inputs
lst = []
if len(lst)==0:
    msg = "List is empty"
elif len(lst)>10:
    msg = "List is full"
else:
    msg = "Everything is fine"
# tkinter.messagebox.showinfo("info",msg)
# tkinter.messagebox.showerror("info","Running out of time")
tkinter.messagebox.showwarning("info","Running out of time")


# Step 4:Main loop
window.mainloop()