from tkinter import*
import random
import time


root = Tk()
root.title("Restaurant Management System")

Tops = Frame(root,bg="white",width = 1600,height=50)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700)
f2.pack(side=RIGHT)


localtime=time.asctime(time.localtime(time.time()))



itm1 = Label(Tops, font=('Arial Bold',30),text="Restaurant Management System",fg='#4682b4',bd=10).grid(row=0,column=0)
itm2 = Label(Tops, font=('aria',20),text=localtime,fg='#4682b4').grid(row=1,column=0)



def Amt():
    x=random.randint(100,900)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    codr= float(Drinks.get())

    costoffries = cof*25
    costoflargefries = colfries*40
    costofburger = cob*35
    costoffilet = cofi*50
    costofcheeseburger = cochee*50
    costofdrinks = codr*35

    costofmeal = "Rs.",str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
    PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.33)
    Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)/99)
    Service="Rs.",str('%.2f'% Ser_Charge)
    OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="Rs.",str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)


def Exit():
    root.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")

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



order = Label(f1, font=('Arial Bold',17),text="Order No.",fg='#4682b4').grid(row=0,column=1)
entryorder = Entry(f1,font=('Arial Bold',15), textvariable=rand , bd=8,insertwidth=2,bg='#b0e0e6',justify='right').grid(row=0,column=2)

fries = Label(f1, font=('Arial Bold',17),text="Fries Meal",fg='#4682b4').grid(row=1,column=1)
entryfries = Entry(f1,font=('Arial Bold',15), textvariable=Fries , bd=8,insertwidth=2,bg='#b0e0e6',justify='right').grid(row=1,column=2)

lunch = Label(f1, font=('Arial Bold',17),text="Lunch Meal",fg='#4682b4').grid(row=2,column=1)
entrylunch = Entry(f1,font=('Arial Bold',15), textvariable=Largefries , bd=8,insertwidth=2,bg='#b0e0e6',justify='right').grid(row=2,column=2)


burger = Label(f1, font=('Arial Bold',17),text="Burger Meal",fg='#4682b4').grid(row=3,column=1)
entryburger = Entry(f1,font=('Arial Bold',15), textvariable=Burger , bd=8,insertwidth=2,bg='#b0e0e6',justify='right').grid(row=3,column=2)

pizza = Label(f1, font=('Arial Bold',17),text="Pizza Meal",fg='#4682b4').grid(row=4,column=1)
entrypizza = Entry(f1,font=('Arial Bold',15), textvariable=Filet , bd=8,insertwidth=2,bg='#b0e0e6',justify='right').grid(row=4,column=2)

Cheeseburger = Label(f1, font=('Arial Bold',17),text="Cheese burger",fg='#4682b4').grid(row=5,column=1)
entryCheese_burger = Entry(f1,font=('Arial Bold',15), textvariable=Cheese_burger , bd=8,insertwidth=2,bg='#b0e0e6',justify='right').grid(row=5,column=2)


drinks = Label(f1, font=('Arial Bold',17),text="Drinks",fg='#4682b4').grid(row=0,column=3)
entrydrinks = Entry(f1,font=('Arial Bold',15), textvariable=Drinks , bd=8,insertwidth=2,bg='#b0e0e6',justify='right').grid(row=0,column=4)

Cost = Label(f1, font=('Arial Bold',17),text="Cost",fg='#4682b4').grid(row=1,column=3)
entrycost = Entry(f1,font=('Arial Bold',15), textvariable=cost , bd=8,insertwidth=2,bg='#b0e0e6',justify='right').grid(row=1,column=4)

Service_charge = Label(f1, font=('Arial Bold',17),text="Service Charge",fg='#4682b4').grid(row=2,column=3)
entryService_Charge = Entry(f1,font=('Arial Bold',15), textvariable=Service_Charge , bd=8,insertwidth=2,bg='#b0e0e6',justify='right').grid(row=2,column=4)

tax = Label(f1, font=('Arial Bold',17),text="Tax",fg='#4682b4').grid(row=3,column=3)
entrytax = Entry(f1,font=('Arial Bold',15), textvariable=Tax , bd=8,insertwidth=2,bg='#b0e0e6',justify='right').grid(row=3,column=4)

subtotal = Label(f1, font=('Arial Bold',17),text="Subtotal",fg='#4682b4').grid(row=4,column=3)
entrysubtotal = Entry(f1,font=('Arial Bold',15), textvariable=Subtotal , bd=8,insertwidth=2,bg='#b0e0e6',justify='right').grid(row=4,column=4)

Totalamt = Label(f1, font=('Arial Bold',17),text="Total",fg='#4682b4').grid(row=5,column=3)
entryTotal = Entry(f1,font=('Arial Bold',15), textvariable=Total , bd=8,insertwidth=2,bg='#b0e0e6',justify='right').grid(row=5,column=4)




lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=6,columnspan=3)

total=Button(f1,fg='#070707',font=('Arial Bold',16),width=10,padx=14,pady=7, bd=8, text="TOTAL", bg='#b0e0e6',command=Amt).grid(row=7, column=2)

reset=Button(f1,fg='#070707',font=('Arial Bold',16),width=10,padx=14,pady=7, bd=8, text="RESET", bg='#b0e0e6',command=Reset).grid(row=7, column=3)

exit=Button(f1,fg='#070707',font=('Arial Bold',16),width=10,padx=14,pady=7, bd=8, text="EXIT", bg='#b0e0e6',command=Exit).grid(row=7, column=4)


def Item_cost():
    r = Tk()

    r.title("Price of Items")
    itm = Label(r, font=('Arial Bold',16), text="ITEMS", fg='#070707').grid(row=0, column=0)
    itm = Label(r, font=('Arial Bold',16), text="COST", fg='#070707').grid(row=0, column=5)
    itm = Label(r, font=('Arial Bold',14), text="Fries Meal", fg='#4682b4').grid(row=1, column=0)
    itm = Label(r, font=('Arial Bold',14), text="30", fg='#4682b4').grid(row=1, column=5)
    itm = Label(r, font=('Arial Bold',14), text="Lunch Meal", fg='#4682b4').grid(row=2, column=0)
    itm = Label(r, font=('Arial Bold',14), text="50", fg='#4682b4').grid(row=2, column=5)
    itm = Label(r, font=('Arial Bold',14), text="Burger Meal", fg='#4682b4').grid(row=3, column=0)
    itm = Label(r, font=('Arial Bold',14), text="25", fg='#4682b4').grid(row=3, column=5)
    itm = Label(r, font=('Arial Bold',14), text="Pizza Meal", fg='#4682b4').grid(row=4, column=0)
    itm = Label(r, font=('Arial Bold',14), text="80", fg='#4682b4').grid(row=4, column=5)
    itm = Label(r, font=('Arial Bold',14), text="Cheese Burger", fg='#4682b4').grid(row=5, column=0)
    itm = Label(r, font=('Arial Bold',14), text="35", fg='#4682b4').grid(row=5, column=5)
    itm = Label(r, font=('Arial Bold',14), text="Drinks", fg='#4682b4').grid(row=6, column=0)
    itm = Label(r, font=('Arial Bold',14), text="25", fg='#4682b4').grid(row=6, column=5)
    r.mainloop()

price=Button(f1,fg='#070707',font=('Arial Bold',15),width=10,padx=14,pady=7,bd=8, text="PRICE", bg='#b0e0e6',command=Item_cost).grid(row=7, column=0)


root.mainloop()