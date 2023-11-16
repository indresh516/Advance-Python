# tkinter

# Step 1 : import tkinter
from tkinter import *


# step 2 : GUI interection
window = Tk()


# step 3 : Adding inputs
window.title("isit")
window.geometry("500x700")
window.config(bg="red")
frame1 = Frame(window,width=300, height=300,cursor="dot")
frame2 = Frame(window,width=300, height=300, cursor="dotbox")

button1 = Button(frame1, text="Submit", bg="blue")
button2 = Button(frame2, text="Exit",bg="green")


frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)
button1.pack()
button2.pack()




# Step 4:Main loop
window.mainloop()