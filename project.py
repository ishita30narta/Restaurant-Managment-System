import  tkinter as tk
from tkinter import *
import time
r = tk.Tk()
r.title('Restaurant Management System')

Tops = Frame(r,bg="white",width = 1600,height=50,relief=SUNKEN)
#Tops.pack(side=TOP)

f1 = Frame(r,width = 900,height=700,relief=SUNKEN)
#f1.pack(side=LEFT)

f2 = Frame(r ,width = 400,height=700,relief=SUNKEN)
#f2.pack(side=RIGHT)


localtime=time.asctime(time.localtime(time.time()))
#Label = tk.Label(r, text = "Restaurant Management System".center(105), font = ('Arial Bold',30), fg = '#4264bc').grid(row=0)
#Label2 = tk.Label(r, text = localtime.center(105), font = ('Arial',20), fg = '#4264bc').grid(row=1)
lblinfo = tk.Label(r, font=( 'aria' ,30, 'bold' ),text="Restaurant Management System".center(105),fg="steel blue",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = tk.Label(r, font=( 'aria' ,20, ),text=localtime.center(105),fg="steel blue",anchor=W)
lblinfo.grid(row=1,column=0)




rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()


lblreference = tk.Label(r, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="steel blue",bd=10,anchor='w')
lblreference.grid(row=3,column=0)
txtreference = Entry(r,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtreference.grid(row=3,column=1)

lblfries = tk.Label(r, font=( 'aria' ,16, 'bold' ),text="Fries Meal",fg="steel blue",bd=10,anchor='w')
lblfries.grid(row=4,column=0)
txtfries = Entry(r,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtfries.grid(row=4,column=1)

lblLargefries = tk.Label(r, font=( 'aria' ,16, 'bold' ),text="Lunch Meal",fg="steel blue",bd=10,anchor='w')
lblLargefries.grid(row=5,column=0)
txtLargefries = Entry(r,font=('ariel' ,16,'bold'), textvariable=Largefries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtLargefries.grid(row=5,column=1)


lblburger = tk.Label(r, font=( 'aria' ,16, 'bold' ),text="Burger Meal",fg="steel blue",bd=10,anchor='w')
lblburger.grid(row=6,column=0)
txtburger = Entry(r,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtburger.grid(row=6,column=1)

lblFilet = tk.Label(r, font=( 'aria' ,16, 'bold' ),text="Pizza Meal",fg="steel blue",bd=10,anchor='w')
lblFilet.grid(row=7,column=0)
txtFilet = Entry(r,font=('ariel' ,16,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtFilet.grid(row=7,column=1)

lblCheese_burger = tk.Label(r, font=( 'aria' ,16, 'bold' ),text="Cheese burger",fg="steel blue",bd=10,anchor='w')
lblCheese_burger.grid(row=8,column=0)
txtCheese_burger = Entry(r,font=('ariel' ,16,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtCheese_burger.grid(row=8,column=1)

lblDrinks = tk.Label(r, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="steel blue",bd=10,anchor='w')
lblDrinks.grid(row=3,column=2)
txtDrinks = Entry(r,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtDrinks.grid(row=3,column=3)

lblcost = tk.Label(r, font=( 'aria' ,16, 'bold' ),text="cost",fg="steel blue",bd=10,anchor='w')
lblcost.grid(row=4,column=2)
txtcost = Entry(r,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtcost.grid(row=4,column=3)

lblService_Charge = tk.Label(r, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="steel blue",bd=10,anchor='w')
lblService_Charge.grid(row=5,column=2)
txtService_Charge = Entry(r,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtService_Charge.grid(row=5,column=3)

lblTax = tk.Label(r, font=( 'aria' ,16, 'bold' ),text="Tax",fg="steel blue",bd=10,anchor='w')
lblTax.grid(row=6,column=2)
txtTax = Entry(r,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTax.grid(row=6,column=3)

lblSubtotal = tk.Label(r, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="steel blue",bd=10,anchor='w')
lblSubtotal.grid(row=7,column=2)
txtSubtotal = Entry(r,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtSubtotal.grid(row=7,column=3)

lblTotal = tk.Label(r, font=( 'aria' ,16, 'bold' ),text="Total",fg="steel blue",bd=10,anchor='w')
lblTotal.grid(row=8,column=2)
txtTotal = Entry(r,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTotal.grid(row=8,column=3)


r.mainloop()
