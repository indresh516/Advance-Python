#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk

#Create an instance of tkinter frame
win = Tk()
#Set the geometry of tkinter frame

win.geometry("750x550")

#Create a canvas
canvas= Canvas(win, width= 600, height= 400)
canvas.pack()

#Load an image in the script
img= Image.open("download.png")
image= img.resize((400,400))
photo= ImageTk.PhotoImage(image)
#Add image to the Canvas Items
canvas.create_image(10,10,anchor=NW,image=photo)

win.mainloop()