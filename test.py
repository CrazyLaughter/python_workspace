#coding=utf-8
print('回df')

from Tkinter import *
root = Tk()
root.title("hello world")
root.geometry('300x200')
l = Label(root, text='好show', bg='green', font=('Arial', 12), width=5, height=2)
l.pack(side=LEFT)#LEFT RIGHT TOP BOTTOM
root.mainloop()