# Step 1 : import tkinter
from tkinter import *
import tkinter.messagebox

# step 2 : GUI interection
window = Tk()
window.title("isit")
window.geometry("500x700")


# step 3 : Adding input

c = Canvas(window, width=500, height=700)
c.pack()

#c.create_line(0,25,500,25, width=5,fill="red",dash=(3,6))#
#c.create_line(0,500,500,0,width=5,fill="blue",dash=(3,3))

# c.create_rectangle(25,25,475,675, fill="red", outline="blue", width=5)
c.create_arc(25,25,475,675, extent= 180, fill="red")
c.create_image()

# Step 4:Main loop
window.mainloop()