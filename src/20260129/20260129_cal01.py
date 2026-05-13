#!/usr/bin/env python3

from tkinter import *
from math import *

def calculate(event):
    label.configure(text = "결과: {:.2f} ".format(eval(entry.get())))

root = Tk()
root.geometry("250x100")

Label(root, text="수식 입력:").pack()

entry = Entry(root)
entry.bind("<Return>", calculate)
entry.pack()


label = Label(root, text ="결과:")
label.pack()

root.mainloop()