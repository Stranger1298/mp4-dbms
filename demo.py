from tkinter import *
from tkinter import ttk
import random
import time

root = Tk()
root.geometry("800x600+100+50")
root.resizable(0, 0)
root.title("Restaurant Management System")

# Color palette
background_color = "#f5f5f5"
header_color = "#003366"
button_color = "#ff4d4d"
button_hover_color = "#cc0000"
button_text_color = "#000000"
text_color = "#333333"
entry_bg_color = "#ffffff"
entry_border_color = "#cccccc"

# Style configuration
style = ttk.Style()
style.configure("TFrame", background=background_color)
style.configure("TLabel", background=background_color, foreground=text_color, font=('aria', 14, 'bold'))
style.configure("TEntry", fieldbackground=entry_bg_color, font=('aria', 14, 'bold'), padding=6, bordercolor=entry_border_color)
style.configure("TButton", background=button_color, foreground=button_text_color, font=('aria', 14, 'bold'), padding=8, borderwidth=0)
style.map("TButton",
          background=[("active", button_hover_color)],
          foreground=[("active", button_text_color)])

# Function to create a rounded button
def create_rounded_button(master, text, command, **kwargs):
    btn = ttk.Button(master, text=text, command=command, **kwargs)
    btn.configure(style="TButton")
    btn['style'] = 'TButton'
    return btn

# Function to create a rounded entry with border
def create_rounded_entry(master, textvariable, **kwargs):
    frame = Frame(master, background=entry_border_color)
    frame.grid_propagate(False)
    entry = ttk.Entry(frame, textvariable=textvariable, **kwargs)
    entry.grid(sticky='nsew')
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)
    return frame

# Header frame (Title Bar)
header_frame = ttk.Frame(root, width=800, height=100, relief=SUNKEN)
header_frame.pack(side=TOP, fill=X)

# Centered frame for main content
content_frame = ttk.Frame(root, width=800, height=500, relief=SUNKEN)
content_frame.pack(expand=True, padx=20, pady=20)

#------------------TIME--------------
localtime = time.asctime(time.localtime(time.time()))

#-----------------INFO TOP------------
lblinfo = ttk.Label(header_frame, text="Restaurant Management System", font=('aria', 25, 'bold'), foreground="white", background=header_color, padding=10)
lblinfo.pack(side=TOP, fill=X)

lbltime = ttk.Label(header_frame, text=localtime, font=('aria', 15), foreground="white", background=header_color, padding=5)
lbltime.pack(side=TOP, fill=X)

#---------------Calculator------------------
x = 1
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
    x += 1

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

def price():
    print("Price button clicked")

#---------------------------------------------------------------------------------------
j = StringVar()
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

lblreference = ttk.Label(content_frame, text="Order No.", foreground=text_color, padding=10)
lblreference.grid(row=0, column=0, sticky=W)
txtreference = create_rounded_entry(content_frame, textvariable=j)
txtreference.grid(row=0, column=1, padx=10, pady=5)

lblfries = ttk.Label(content_frame, text="Fries", foreground=text_color, padding=10)
lblfries.grid(row=1, column=0, sticky=W)
txtfries = create_rounded_entry(content_frame, textvariable=Fries)
txtfries.grid(row=1, column=1, padx=10, pady=5)

lblLargefries = ttk.Label(content_frame, text="Meals", foreground=text_color, padding=10)
lblLargefries.grid(row=2, column=0, sticky=W)
txtLargefries = create_rounded_entry(content_frame, textvariable=Meals)
txtLargefries.grid(row=2, column=1, padx=10, pady=5)

lblburger = ttk.Label(content_frame, text="Burger", foreground=text_color, padding=10)
lblburger.grid(row=3, column=0, sticky=W)
txtburger = create_rounded_entry(content_frame, textvariable=Burger)
txtburger.grid(row=3, column=1, padx=10, pady=5)

lblFilet = ttk.Label(content_frame, text="Pizza", foreground=text_color, padding=10)
lblFilet.grid(row=4, column=0, sticky=W)
txtFilet = create_rounded_entry(content_frame, textvariable=Pizza)
txtFilet.grid(row=4, column=1, padx=10, pady=5)

lblCheese_burger = ttk.Label(content_frame, text="Cheese burger", foreground=text_color, padding=10)
lblCheese_burger.grid(row=5, column=0, sticky=W)
txtCheese_burger = create_rounded_entry(content_frame, textvariable=Cheese_burger)
txtCheese_burger.grid(row=5, column=1, padx=10, pady=5)

lblDrinks = ttk.Label(content_frame, text="Drinks", foreground=text_color, padding=10)
lblDrinks.grid(row=0, column=2, sticky=W)
txtDrinks = create_rounded_entry(content_frame, textvariable=Drinks)
txtDrinks.grid(row=0, column=3, padx=10, pady=5)

lblcost = ttk.Label(content_frame, text="Cost", foreground=text_color, padding=10)
lblcost.grid(row=1, column=2, sticky=W)
txtcost = create_rounded_entry(content_frame, textvariable=cost)
txtcost.grid(row=1, column=3, padx=10, pady=5)

lblService_Charge = ttk.Label(content_frame, text="Service Charge", foreground=text_color, padding=10)
lblService_Charge.grid(row=2, column=2, sticky=W)
txtService_Charge = create_rounded_entry(content_frame, textvariable=Service_Charge)
txtService_Charge.grid(row=2, column=3, padx=10, pady=5)

lblTax = ttk.Label(content_frame, text="Tax", foreground=text_color, padding=10)
lblTax.grid(row=3, column=2, sticky=W)
txtTax = create_rounded_entry(content_frame, textvariable=Tax)
txtTax.grid(row=3, column=3, padx=10, pady=5)

lblSubtotal = ttk.Label(content_frame, text="Subtotal", foreground=text_color, padding=10)
lblSubtotal.grid(row=4, column=2, sticky=W)
txtSubtotal = create_rounded_entry(content_frame, textvariable=Subtotal)
txtSubtotal.grid(row=4, column=3, padx=10, pady=5)

lblTotal = ttk.Label(content_frame, text="Total", foreground=text_color, padding=10)
lblTotal.grid(row=5, column=2, sticky=W)
txtTotal = create_rounded_entry(content_frame, textvariable=Total)
txtTotal.grid(row=5, column=3, padx=10, pady=5)

btnTotal = create_rounded_button(content_frame, text="TOTAL", command=Ref)
btnTotal.grid(row=6, column=0, padx=10, pady=10)

btnreset = create_rounded_button(content_frame, text="RESET", command=reset)
btnreset.grid(row=6, column=1, padx=10, pady=10)

btnexit = create_rounded_button(content_frame, text="EXIT", command=qexit)
btnexit.grid(row=6, column=2, padx=10, pady=10)

btnShowOrders = create_rounded_button(content_frame, text="SHOW ORDERS", command=show_orders)
btnShowOrders.grid(row=7, column=0, columnspan=3, padx=10, pady=10, sticky=W+E)

btnprice = create_rounded_button(content_frame, text="PRICE", command=price)
btnprice.grid(row=6, column=3, padx=10, pady=10)

root.mainloop()
