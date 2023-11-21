# Step 1 : import tkinter
from tkinter import *
import tkinter.messagebox

# step 2 : GUI interection
window = Tk()
window.geometry("500x500")


# step 3 : Adding input
chbox1 = IntVar()
chbox2 = IntVar()
chbox3 = IntVar()

chbox1 = Checkbutton(window, text="apple",onvalue=1, offvalue=0, height=2, width= 10)
chbox2 = Checkbutton(window, text="Mango",onvalue=1, offvalue=0, height=2, width= 10)
chbox3 = Checkbutton(window, text="Orange",onvalue=1, offvalue=0, height=2, width= 10)

chbox1.pack()
chbox2.pack()
chbox3.pack()


# Step 4:Main loop
window.mainloop()