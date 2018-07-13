'''from tkinter import *
window = Tk()
window.title("Welcome to LikeGeeks app")

window.geometry('350x200')
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=1, row=0)
window.mainloop()

import tkinter as tk

root = tk.Tk()

T1 = tk.Text(root)
T1.tag_configure("center", justify='center')
T1.insert("1.0", "text")
T1.tag_add("center", "1.0", "end")
T1.pack()

root.mainloop()

from tkinter import *
master = Tk()
Label(master, text='First Name').grid(row=3)
Label(master, text='Last Name').grid(row=4)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=3, column=1)
e2.grid(row=4, column=1)
mainloop()'''


from tkinter import *

top = Tk()
L1 = Label(top, text="User Name".).grid(row=1)
#L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
e1 = Entry(top)
#E1.pack(side = RIGHT)
e1.grid(row=1, column=1)

top.mainloop()