from tkinter import *

root = Tk()
root.geometry("500x500")
v = IntVar()
Radiobutton(root, text='Male', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='Female', variable=v, value=2).pack(anchor=W)
mainloop()
