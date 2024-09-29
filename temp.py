from tkinter import *
import random
import time

root = Tk()
root.geometry("1200x600+0+0")
root.resizable(0,0)
root.title("Restaurant Management System")

Tops = Frame(root, bg="white", width=1000, height=60, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=700, height=540, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=540, relief=SUNKEN)
f2.pack(side=RIGHT)

#------------------TIME--------------
localtime = time.asctime(time.localtime(time.time()))

#-----------------INFO TOP------------
lblinfo = Label(Tops, font=('aria', 25, 'bold'), text="Restaurant Management System", fg="light sky blue", bd=10, anchor='w')
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=('aria', 15), text=localtime, fg="azure", anchor=W)
lblinfo.grid(row=1, column=0)

#---------------Calculator------------------
x=1
order_data = []

def Ref():
    global x
    randomRef = str(x)
    j.set(randomRef)

    cof = float(Fries.get() or 0)
    colfries = float(Meals.get() or 0)
    cob = float(Burger.get() or 0)
    cofi = float(Pizza.get() or 0)
    cochee = float(Cheese_burger.get() or 0)
    codr = float(Drinks.get() or 0)


    costoffries = cof * 25
    costofmeals = colfries * 40
    costofburger = cob * 35
    costofpizza = cofi * 30
    costofcheeseburger = cochee * 50
    costofdrinks = codr * 35

    costofmeal = costoffries + costofmeals + costofburger + costofpizza + costofcheeseburger + costofdrinks
    PayTax = costofmeal * 0.33
    Totalcost = costofmeal
    Ser_Charge = costofmeal / 99
    Service = "Rs. " + str('%.2f' % Ser_Charge)
    OverAllCost = "Rs. " + str(PayTax + Totalcost + Ser_Charge)
    PaidTax = "Rs. " + str('%.2f' % PayTax)

    Service_Charge.set(Service)
    cost.set("Rs. " + str('%.2f' % costofmeal))
    Tax.set(PaidTax)
    Subtotal.set("Rs. " + str('%.2f' % costofmeal))
    Total.set(OverAllCost)

    order = {
        "Order No": randomRef,
        "Fries": cof,
        "Meals": colfries,
        "Burger": cob,
        "Pizza": cofi,
        "Cheese Burger": cochee,
        "Drinks": codr,
        "Cost": costofmeal,
        "Service Charge": Ser_Charge,
        "Tax": PayTax,
        "Total": PayTax + Totalcost + Ser_Charge
    }
    order_data.append(order)
    x+=1

def qexit():
    root.destroy()

def reset():
    j.set("")
    Fries.set("")
    Meals.set("")
    Burger.set("")
    Pizza.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")

def show_orders():
    order_window = Toplevel(root)
    order_window.geometry("600x400")
    order_window.title("Order Data")
    Label(order_window, text="Order Data", font=('aria', 14, 'bold')).pack()
    text_widget = Text(order_window, wrap='word')
    text_widget.pack(expand=1, fill='both')

    for order in order_data:
        text_widget.insert(END, f"{order}\n\n")

#---------------------------------------------------------------------------------------
j= StringVar()
Fries = StringVar()
Meals = StringVar()
Burger = StringVar()
Pizza = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()

lblreference = Label(f1, font=('aria', 14, 'bold'), text="Order No.", fg="steel blue", bd=10, anchor='w')
lblreference.grid(row=0, column=0)
txtreference = Entry(f1, font=('ariel', 14, 'bold'), textvariable=j, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtreference.grid(row=0, column=1)

lblfries = Label(f1, font=('aria', 14, 'bold'), text="Fries", fg="steel blue", bd=10, anchor='w')
lblfries.grid(row=1, column=0)
txtfries = Entry(f1, font=('ariel', 14, 'bold'), textvariable=Fries, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtfries.grid(row=1, column=1)

lblLargefries = Label(f1, font=('aria', 14, 'bold'), text="Meals", fg="steel blue", bd=10, anchor='w')
lblLargefries.grid(row=2, column=0)
txtLargefries = Entry(f1, font=('ariel', 14, 'bold'), textvariable=Meals, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtLargefries.grid(row=2, column=1)

lblburger = Label(f1, font=('aria', 14, 'bold'), text="Burger", fg="steel blue", bd=10, anchor='w')
lblburger.grid(row=3, column=0)
txtburger = Entry(f1, font=('ariel', 14, 'bold'), textvariable=Burger, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtburger.grid(row=3, column=1)

lblFilet = Label(f1, font=('aria', 14, 'bold'), text="Pizza", fg="steel blue", bd=10, anchor='w')
lblFilet.grid(row=4, column=0)
txtFilet = Entry(f1, font=('ariel', 14, 'bold'), textvariable=Pizza, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtFilet.grid(row=4, column=1)

lblCheese_burger = Label(f1, font=('aria', 14, 'bold'), text="Cheese burger", fg="steel blue", bd=10, anchor='w')
lblCheese_burger.grid(row=5, column=0)
txtCheese_burger = Entry(f1, font=('ariel', 14, 'bold'), textvariable=Cheese_burger, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtCheese_burger.grid(row=5, column=1)

#--------------------------------------------------------------------------------------
lblDrinks = Label(f1, font=('aria', 14, 'bold'), text="Drinks", fg="steel blue", bd=10, anchor='w')
lblDrinks.grid(row=0, column=2)
txtDrinks = Entry(f1, font=('ariel', 14, 'bold'), textvariable=Drinks, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtDrinks.grid(row=0, column=3)

lblcost = Label(f1, font=('aria', 14, 'bold'), text="Cost", fg="steel blue", bd=10, anchor='w')
lblcost.grid(row=1, column=2)
txtcost = Entry(f1, font=('ariel', 14, 'bold'), textvariable=cost, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtcost.grid(row=1, column=3)

lblService_Charge = Label(f1, font=('aria', 14, 'bold'), text="Service Charge", fg="steel blue", bd=10, anchor='w')
lblService_Charge.grid(row=2, column=2)
txtService_Charge = Entry(f1, font=('ariel', 14, 'bold'), textvariable=Service_Charge, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtService_Charge.grid(row=2, column=3)

lblTax = Label(f1, font=('aria', 14, 'bold'), text="Tax", fg="steel blue", bd=10, anchor='w')
lblTax.grid(row=3, column=2)
txtTax = Entry(f1, font=('ariel', 14, 'bold'), textvariable=Tax, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtTax.grid(row=3, column=3)

lblSubtotal = Label(f1, font=('aria', 14, 'bold'), text="Subtotal", fg="steel blue", bd=10, anchor='w')
lblSubtotal.grid(row=4, column=2)
txtSubtotal = Entry(f1, font=('ariel', 14, 'bold'), textvariable=Subtotal, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtSubtotal.grid(row=4, column=3)

lblTotal = Label(f1, font=('aria', 14, 'bold'), text="Total", fg="steel blue", bd=10, anchor='w')
lblTotal.grid(row=5, column=2)
txtTotal = Entry(f1, font=('ariel', 14, 'bold'), textvariable=Total, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtTotal.grid(row=5, column=3)

#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1, text="---------------------", fg="white")
lblTotal.grid(row=6, columnspan=3)

btnTotal = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 14, 'bold'), width=10, text="TOTAL", bg="powder blue", command=Ref)
btnTotal.grid(row=7, column=1)

btnreset = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 14, 'bold'), width=10, text="RESET", bg="powder blue", command=reset)
btnreset.grid(row=7, column=2)

btnexit = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 14, 'bold'), width=10, text="EXIT", bg="powder blue", command=qexit)
btnexit.grid(row=7, column=3)

btnShowOrders = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 14, 'bold'), width=10, text="SHOW ORDERS", bg="powder blue", command=show_orders)
btnShowOrders.grid(row=8, column=1, columnspan=3, sticky=W+E)

def price():
    roo = Tk()
    roo.geometry("400x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 14, 'bold'), text="ITEM", fg="white", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 14, 'bold'), text="", fg="black", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 14, 'bold'), text="PRICE", fg="white", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 14, 'bold'), text="Fries", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 14, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 14, 'bold'), text="Meals", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 14, 'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 14, 'bold'), text="Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 14, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 14, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 14, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 14, 'bold'), text="Pizza", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 14, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 14, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 14, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()

btnprice = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 14, 'bold'), width=10, text="PRICE", bg="powder blue", command=price)
btnprice.grid(row=7, column=0)

root.mainloop()