import tkinter
from tkinter import *
from functools import partial

win = Tk()
win.geometry("250x200")

l = Label(win,text="Enter Number One")
l2 = Label(win,text="Enter Number Two")
lab= Label(win)

l.grid(row=1,column=2)
l2.grid(row=3,column=2)
lab.grid(row=7,column=2)


x1 = StringVar()
x2 =StringVar()

def sum(lab,x1,x2):
    n1 = (x1.get())
    n2 = (x2.get())
    sum = int(n1) + int(n2)
    lab.config(text="Sum Is = %d"%sum)
    return



num1 = Entry(win,textvariable=x1)
num2 = Entry(win,textvariable=x2)

num1.grid(row=1,column=3)
num2.grid(row=3,column=3)

sum=partial(sum,lab,x1,x2)
button=Button(win,text="calculate",command=sum)

button.grid(row=4,column=2)
win.mainloop()

