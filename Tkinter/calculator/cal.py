# Step 1 : Import
from tkinter import *
# Step 2: GUI Interaction
window = Tk()
window.geometry("500x500")
# Step 3 : Adding Inputs
# Entry Box
e = Entry(window,width=46,borderwidth=5)
e.place(x = 0,y=0)

# Functions
def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))

def add():
    n1 = e.get()
    global math
    math = "Addition"
    global i
    i = int(n1)
    e.delete(0,END)

def sub():
    n1 = e.get()
    global math
    math = "Subtraction"
    global i
    i = int(n1)
    e.delete(0,END)

def mult():
    n1 = e.get()
    global math
    math = "Multiplication"
    global i
    i = int(n1)
    e.delete(0,END)

def div():
    n1 = e.get()
    global math
    math = "Division"
    global i
    i = int(n1)
    e.delete(0,END)

def equal():
    n2 = e.get()
    e.delete(0,END)
    if math == "Addition":
        e.insert(0,i+int(n2))
    elif math =="Subtraction":
        e.insert(0,i-int(n2))
    elif math == "Division":
        e.insert(0,i/int(n2))
    elif math == "Multiplication":
        e.insert(0,i*int(n2))

def clear():
    e.delete(0,END)

# buttons
b=Button(window,text='1',width=12, command=lambda:click(1))
b.place(x = 10,y=60)

b=Button(window,text='2',width=12, command=lambda:click(2))
b.place(x = 100,y=60)

b=Button(window,text='3',width=12, command=lambda:click(3))
b.place(x = 190,y=60)
    
b=Button(window,text='C',width=12, command=clear)
b.place(x=280,y=60)

b=Button(window,text='4',width=12, command=lambda:click(4))
b.place(x = 10,y=100)

b=Button(window,text='5',width=12, command=lambda:click(5))
b.place(x = 100,y=100)

b=Button(window,text='6',width=12, command=lambda:click(6))
b.place(x = 190,y=100)

b=Button(window,text='/',width=12, command=div)
b.place(x=280,y=100)

b=Button(window,text='7',width=12, command=lambda:click(7))
b.place(x = 10,y=140)

b=Button(window,text='8',width=12, command=lambda:click(8))
b.place(x = 100,y=140)

b=Button(window,text='9',width=12, command=lambda:click(9))
b.place(x = 190,y=140)

b=Button(window,text='-',width=12, command=sub)
b.place(x = 190,y=180)

b=Button(window,text='0',width=12, command=lambda:click(0))
b.place(x = 10,y=180)

b=Button(window,text='+',width=12, command=add)
b.place(x=100,y=180)

b=Button(window,text='*',width=12, command=mult)
b.place(x=280,y=140)

b=Button(window,text='=',width=12, command=equal)
b.place(x=280,y=180)


# Step 4 : Main
mainloop()
