# tkinter

# Step 1 : import tkinter
from tkinter import *


# step 2 : GUI interection
window = Tk()


# step 3 : Adding inputs
window.title("Data Science") # for add title
window.geometry("376x700")   # for add default size of window

def logentry():
    print("logged in Successfully....")


button = Button(window, text="Login", width=12, bg="red",fg="white", font=("bold",12), activebackground="#00BFFF",activeforeground="black", command=logentry)
button.pack()




# Step 4:Main loop
window.mainloop()