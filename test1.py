'''import  tkinter as tk
from tkinter import *
r = tk.Tk()
r.title('Restaurant Management System')
#Label(r,text ="Restaurant Management System".center(410)).grid(row =0)
Label = tk.Label(r, text = "Test Label".center(110), font = ('Comic Sans MS',30),
 bg = 'Green', fg = 'blue').grid(row=0)
Labe2 = tk.Label(r, text = "Test".center(110), font = ('Comic Sans MS',30),
 bg = 'Green', fg = 'blue').grid(row=1)'''

from tkinter import *
import tkinter as tk
r = tk.Tk()
tk.Label(r, text="First Name",height=20).grid(row=0)
tk.Label(r, text="Last Name").grid(row=1)
#tk.Label(r, text="First Name").grid(row=2)
#tk.Label(r, text="Last Name").grid(row=3)
e1 = Entry(r)
e2 = Entry(r)
#e3 = Entry(r)
#e4 = Entry(r)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
#e3.grid(row=2, column=1)
#e4.grid(row=3, column=1)
mainloop()






r.mainloop()
'''
from tkinter import *
from subprocess import *

print("Hello world")

def func():
    proc = Popen("Test2.py", stdout=PIPE, shell=True)
    proc = proc.communicate()
    output.insert(END, proc)

Master = Tk()
Check = Button(Master, text="Display output", command=func)
Quit = Button(Master, text="Exit", fg="red", command=Master.quit)
output = Text(Master, width=40, height=8)

Check.pack(padx=20, pady=8)
Quit.pack(padx=20, pady=18)
output.pack()

Master.mainloop()'''