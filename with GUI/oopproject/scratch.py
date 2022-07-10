from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import datetime
import sqlite3
from tkinter import messagebox


#created file
import items

def startup():
    startup = Tk()
    startup.geometry('+0+0')
    startup.title('Jollibae Ordering System')
    startup.iconbitmap('assets/wut2.ico')

    logo = ImageTk.PhotoImage(file="assets/logo.PNG")

    startup_frame = LabelFrame(startup, bg='#272727', borderwidth=0, highlightthickness=0, )
    startup_frame.grid(columnspan=3, sticky=W + E)

    logol = Label(startup_frame, image=logo, borderwidth=0, highlightthickness=0, anchor='center')
    logol.grid(row=0, column=0, padx=20, pady=20)

    title = Label(startup_frame, text="Self-Order Kiosk", bg='#272727', fg='#ffffff', font=('Arial Rounded MT Bold', 60), anchor='center', width=30)
    title.grid(row=1, column=0, sticky=W + E, padx=20, pady=20)

    datet = datetime.datetime.now().strftime("%A %m-%d-20%y, %H:%M:%S")
    datel = Label(startup_frame, text=datet, bg='#272727', fg='#ffffff', font=('Arial Rounded MT Bold', 15))
    datel.grid(row=0, column=0, padx=150, pady=20, sticky=N+E)

    desc = Label(startup_frame, text="Welcome to Jollibae! Please Enter Your Name (Given/ First Name).", padx=40, pady=10, background="#303030", fg='#ffffff', font=('Arial', 12))
    desc.grid(row=2, sticky=W+E)


    def set_cname():
        cname = name_box.get()
        startup.destroy()
        mainmenu(cname)

    name_box = Entry(startup_frame, font=('Arial', 30), width=15)
    name_box.grid(row=3, pady=20)

    enter_name = Button(startup_frame, text="Enter Name", bg='red', fg='#ffffff', font=('Arial Bold', 30), command=set_cname)
    enter_name.grid(row=4, pady=20)

    startup.mainloop()

def mainmenu(customer_name):
    root = Tk()
    root.geometry('+0+0')
    root.title('Jollibae Ordering System')
    root.iconbitmap('assets/wut2.ico')

    #header
    logo = Image.open("assets/logo.PNG")
    logo = logo.resize((120,120),Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(logo)

    header = LabelFrame(root, bg='#272727', borderwidth=0, highlightthickness=0, )
    header.grid(columnspan=3, sticky=W+E)

    logol = Label(header, image=logo, borderwidth=0, highlightthickness=0)
    logol.grid(row =0, column=0, padx=20, pady=20)

    title = Label(header, text="Self-Order Kiosk", bg='#272727', fg='#ffffff', font=('Arial Rounded MT Bold', 60), anchor=E)
    title.grid(row=0, column=1, sticky=W+E)

    datet = datetime.datetime.now().strftime("%A %m-%d-20%y, %H:%M:%S")
    datel = Label(header, text=datet, padx=20, pady=20, bg='#272727', fg='#ffffff', font=('Arial Rounded MT Bold', 15), anchor=S + E)
    datel.grid(row=0, column=2, sticky='nsew')

    desc = Label(header, text="Welcome to Jollibae, " + customer_name + "!  Feel free to explore our Menu!", padx=40, pady=10, background="#303030", fg='#ffffff', font=('Arial', 12), width=161, anchor=W)
    desc.grid(row=2, columnspan=3)

    #frame 1
    frame = LabelFrame(root, pady=20, borderwidth=0, bg='#303030')
    frame.grid(row=1, sticky='nsew')
    fr1w = Label(frame, width=25, bg='#303030')
    fr1w.grid()

    '''def spinboxchange(qtk, price, indx):
        qtc = qtk.get()
    
        if qtc != 0:  # change to delete order
            subprice = int(qtc) * price
            orderl[indx][3] = subprice
            print_order()
            print(orderl)
    
        else:
            orderl.pop(indx)
            print_order()
            print(orderl)
    '''

    def proceed(orderlist, customer_name):
        if orderlist == []:
            messagebox.showerror("Empty order", "Please Order an Item/s first. Thank You.")
        else:
            response= messagebox.askquestion("Proceed to Checkout", "Would you like to proceed to Checkout and finalize order?")
            if response == "yes":
                for orders in orderlist: orders[0] = orders[0].get()
                print(orderlist)
                root.destroy()
                confirm_order(orderlist, customer_name)
            else: pass


    def quantity_change(qtk, price, indx, op):
        qtc = qtk.get()

        if op == '+':
            qtc += 1
            qtk.set(qtc)
        else:
            qtc -= 1
            qtk.set(qtc)

        qtc = qtk.get()
        if qtc != 0:  # change to delete order
            subprice = int(qtc) * price
            orderl[indx][3] = subprice
            print_order()
            print(orderl)

        else:
            orderl.pop(indx)
            print_order()
            print(orderl)

    def print_order():
        global frame3
        frame3.forget()
        frame3 = LabelFrame(root, padx=10, pady=10, borderwidth=0, highlightthickness=0)
        frame3.grid(row=1, column=2, sticky='nsew')

        qtyd = Label(frame3, text='Qty.', bg='#272727', fg='#ffffff', font=('Arial', 15))
        qtyd.grid(row=0,)

        itemd = Label(frame3, text='Item', font=('Arial Bold', 15), width=13)
        itemd.grid(row=0, column=1)

        priced = Label(frame3, text='Price', bg='#272727', fg='#ffffff', font=('Arial', 15), width=9)
        priced.grid(row=0, column=2)

        orderl_items = []

        r = 1
        for order in orderl:
            #qtsp = Spinbox(frame3, from_=0, to=10, font=('Arial Bold', 15), width=1, textvariable=order[0])
            #qtsp.grid(row=r, column=0, pady=5, sticky=W + E)

            qtlab = Label(frame3, textvariable=order[0], font=('Arial Bold', 12), width=4)
            qtlab.grid(row=r, column=0, padx=5, pady=5)

            qtsub = Button(frame3, text='-', font=('Arial Bold', 12), width=1, bg='#58E3E4')
            qtsub.grid(row=r, column=0, sticky=W)

            qtplus = Button(frame3, text='+', font=('Arial Bold', 12), width=1, bg='#58E3E4')
            qtplus.grid(row=r, column=0, sticky=E)

            itp = Label(frame3, text=order[1][:21] + order[1][21:], font=('Arial Bold', 10))
            itp.grid(row=r, column=1, sticky=W + E)

            pstr = "PHP " + str(order[3]) + ".00"
            plp = Label(frame3, text=pstr, font=('Arial Bold', 10))
            plp.grid(row=r, column=2, sticky=W + E)

            indx = r - 2
            #orderl_items.append([qtsp, itp, plp, order[0], order[2], indx])
            orderl_items.append([qtsub, qtplus, order[0], order[2], indx])
            r += 1

        #for objects in orderl_items:
        #    objects[0].config(command=lambda: spinboxchange(objects[3], objects[4], objects[5]))

        for qtchange in orderl_items:
            qtchange[0].config(command=lambda: quantity_change(qtchange[2], qtchange[3], qtchange[4], '-'))
            qtchange[1].config(command=lambda: quantity_change(qtchange[2], qtchange[3], qtchange[4], '+'))

        total_v = 0
        for subtotal in orderl:
            total_v += subtotal[3]

        total_str = 'Total: PHP ' + str(total_v) + '.00'

        total_l = Label(frame3, text=total_str, bg='#272727', fg='#ffffff', font=('Arial Bold', 15), anchor=E, padx=5, pady=5)
        total_l.grid(row=r, columnspan=3, sticky=W + E, pady=5)

        r+=1
        confirm_orderb = Button(frame3, text="Confirm Order", bg='red', fg='#ffffff', font=('Arial Bold', 15), command=lambda: proceed(orderl, customer_name))
        confirm_orderb.grid(row=r, columnspan=3, sticky=W + E)

        print('\n' + str(orderl_items))

    def order(quant, item, price):
        orderl.append([quant, item, price, price])  # 2nd price is subprice/price*quantity
        print_order()

    def chicken_cat():
        global frame2
        global cat
        global itl1, thl1, itl2, thl2
        cat = "Chicken"

        frame2.grid_forget()
        frame2 = LabelFrame(root, padx=10, pady=20, borderwidth=0, highlightthickness=0, bg='#303030')
        frame2.grid(row=1, column=1)

        catt = Label(frame2, text=cat, pady=20, padx=20, bg='#272727', fg='#ffffff', font=('Arial Rounded MT Bold', 18), anchor=W)
        catt.grid(row=0, columnspan=4, sticky='nsew', pady=20)

        # item 1
        qt1=IntVar()
        qt1.set(1)
        pr1 = chickenl[0].price
        it1=chickenl[0].name
        itstr1=it1 + "\nPHP " + str(pr1) + ".00"
        thl1=ImageTk.PhotoImage(Image.open(chickenl[0].th))
        itemth1 = Label(frame2, image=thl1, bg='#272727')
        itemth1.grid(row=1, column=0, padx=15)
        itemb1 = Button(frame2, text=itstr1, bg='#58E3E4', font=('Arial Rounded MT Bold', 12), command=lambda: order(qt1, it1, pr1))
        itemb1.grid(row=2, column=0, sticky=W + E, padx=15)

        # item 2
        qt2 = IntVar()
        qt2.set(1)
        pr2 = chickenl[1].price
        it2 = chickenl[1].name
        itstr2 = it2 + "\nPHP " + str(pr2) + ".00"
        thl2 = ImageTk.PhotoImage(Image.open(chickenl[1].th))
        itemth2 = Label(frame2, image=thl2, bg='#272727')
        itemth2.grid(row=1, column=1, padx=15)
        itemb2 = Button(frame2, text=itstr2, bg='#58E3E4', font=('Arial Rounded MT Bold', 12), command=lambda: order(qt2, it2, pr2))
        itemb2.grid(row=2, column=1, sticky=W + E, padx=15)

    #show button
    chicken = Button(frame, text="Chicken           >", fg='#ffffff', bg='#272727', font=('Arial Rounded MT Bold', 15), width=12, command=chicken_cat)
    chicken.grid(row=1, sticky=E)

    def palabok_cat():
        global frame2
        global cat
        global itl1, thl1, itl2, thl2, itl3, thl3
        cat = "Palabok"

        frame2.grid_forget()
        frame2 = LabelFrame(root, padx=10, pady=20, borderwidth=0, highlightthickness=0, bg='#303030')
        frame2.grid(row=1, column=1)

        catt = Label(frame2, text=cat, pady=20, padx=20, bg='#272727', fg='#ffffff', font=('Arial Rounded MT Bold', 18), anchor=W)
        catt.grid(row=0, columnspan=4, sticky='nsew', pady=20)

        # item 1
        qt1=IntVar()
        qt1.set(1)
        pr1=palabokl[0].price
        it1=palabokl[0].name
        itstr1= it1 + "\nPHP " + str(pr1) + ".00"
        thl1=ImageTk.PhotoImage(Image.open(palabokl[0].th))
        itemth1 = Label(frame2, image=thl1, bg='#272727')
        itemth1.grid(row=1, column=0, padx=15)
        itemb1 = Button(frame2, text=itstr1, bg='#58E3E4', fg='#000000', font=('Arial Rounded MT Bold', 12), command=lambda: order(qt1, it1, pr1))
        itemb1.grid(row=2, column=0, sticky=W + E, padx=15)

        # item 2
        qt2 = IntVar()
        qt2.set(1)
        pr2 = palabokl[1].price
        it2 = palabokl[1].name
        itstr2 = it2 + "\nPHP " + str(pr2) + ".00"
        thl2 = ImageTk.PhotoImage(Image.open(palabokl[1].th))
        itemth2 = Label(frame2, image=thl2, bg='#272727')
        itemth2.grid(row=1, column=1, padx=15)
        itemb2 = Button(frame2, text=itstr2, bg='#58E3E4', fg='#000000', font=('Arial Rounded MT Bold', 12), command=lambda: order(qt2, it2, pr2))
        itemb2.grid(row=2, column=1, sticky=W + E, padx=15)

        # item 3
        qt3 = IntVar()
        qt3.set(1)
        pr3 = palabokl[2].price
        it3 = palabokl[2].name
        itstr3 = it3 + "\nPHP " + str(pr3) + ".00"
        thl3 = ImageTk.PhotoImage(Image.open(palabokl[2].th))
        itemth3 = Label(frame2, image=thl3, bg='#272727')
        itemth3.grid(row=1, column=2, padx=15)
        itemb3 = Button(frame2, text=itstr3, bg='#58E3E4', fg='#000000', font=('Arial Rounded MT Bold', 12), command=lambda: order(qt3, it3, pr3))
        itemb3.grid(row=2, column=2, sticky=W + E, padx=15)

    palabok = Button(frame, text="Palabok           >", fg='#ffffff', bg='#272727', font=('Arial Rounded MT Bold', 15), width=12, command=palabok_cat)
    palabok.grid(row=5, sticky=E)

    #frame 2
    global frame2
    frame2 = LabelFrame(root, padx=10, pady=20, borderwidth=0, highlightthickness=0, bg='#303030')
    frame2.grid(row=1, column=1)

    #frame 3
    global frame3
    frame3 = LabelFrame(root, padx=10, pady=10, borderwidth=0, highlightthickness=0)
    frame3.grid(row=1, column=2, sticky='nsew')

    qtyd = Label(frame3, text='Qty.', bg='#272727', fg='#ffffff', font=('Arial', 15))
    qtyd.grid(row=0)

    itemd = Label(frame3, text='Item', font=('Arial Bold', 15), width=13)
    itemd.grid(row=0, column=1)

    priced = Label(frame3, text='Price', bg='#272727', fg='#ffffff', font=('Arial', 15), width=9)
    priced.grid(row=0, column=2)

    total_v=0
    total_str='Total: PHP ' + str(total_v) + '.00'

    total_l = Label(frame3, text=total_str, bg='#272727', fg='#ffffff', font=('Arial Bold', 15), anchor=E, padx=5, pady=5)
    total_l.grid(row=3,columnspan=3,sticky=W+E, pady=5)

    orderl=[]
    confirm_orderb = Button(frame3, text="Confirm Order", bg='red', fg='#ffffff', font=('Arial Bold', 15), command=lambda: proceed(orderl, customer_name))
    confirm_orderb.grid(row=4,columnspan=3,sticky=W+E)

    #driver
    chickenl=[items.opccs(), items.tpccs()]
    palabokl=[items.ps(), items.pfp(), items.fpd()]

    orderl=[]

    start=chicken_cat()

    root.mainloop()

def confirm_order(orders, customer_name):
    #initial
    checkout = Tk()
    checkout.geometry("+0+0")
    checkout.title('Jollibae Ordering System')
    checkout.iconbitmap('assets/wut2.ico')

    # header
    logo = Image.open("assets/logo.PNG")
    logo = logo.resize((120, 120), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(logo)

    header = LabelFrame(checkout, bg='#272727', borderwidth=0, highlightthickness=0, )
    header.grid(columnspan=3, sticky=W+E)

    logol = Label(header, image=logo, borderwidth=0, highlightthickness=0)
    logol.grid(row=0, column=0, padx=50, pady=20, sticky=W)

    title = Label(header, text="Order Confirmation", bg='#272727', fg='#ffffff', font=('Arial Rounded MT Bold', 60), anchor=E)
    title.grid(row=0, column=1, sticky=W + E)

    datet = datetime.datetime.now().strftime("%A %m-%d-20%y, %H:%M:%S")
    datel = Label(header, text=datet, padx=20, pady=20, bg='#272727', fg='#ffffff', font=('Arial Rounded MT Bold', 15), anchor=S + E)
    datel.grid(row=0, column=2, sticky='nsew')

    inst='Please fill in the form with your information to complete order.   If you are a new customer, Please register first.'
    desc = Label(header, text=inst, padx=40, pady=10,
                 background="#303030", fg='#ffffff', font=('Arial', 12), width=161, anchor=W)
    desc.grid(row=2, columnspan=3)

    def register():
        #registration form
        reg_l = Label(frame1, text='Registration Form', pady=10, padx=20, bg='#303030', fg='#ffffff', font=('Arial Rounded MT Bold', 18), anchor=W)
        reg_l.grid(row=5, columnspan=5, sticky='nsew', pady=10)

        customer_info=[]

        first_namel.grid(row=6, column=0, padx=20, pady=(10, 0), sticky=W)
        first_name.insert(0, customer_name)
        first_name.grid(row=7, column=0, padx=20, pady=(0, 10))

        mi_l.grid(row=6, column=1, padx=20, pady=(10, 0), sticky=W)
        mi.grid(row=7, column=1, padx=20, pady=(0, 10), sticky=W)

        last_namel.grid(row=6, column=2, padx=20, pady=(10, 0), sticky=W)
        last_name.grid(row=7, column=2, padx=20, pady=(0, 10))

        genderl.grid(row=6, column=3, padx=20, pady=(10, 0), sticky=W)
        genderbox.grid(row=7, column=3, padx=20, pady=(0, 10))
        g1.grid(row=7, column=3, sticky=W, padx=20, pady=(0, 10))
        g2.grid(row=7, column=3, sticky=E, padx=20, pady=(0, 10))

        street_adrl.grid(row=8, column=0, padx=20, pady=(10, 0), sticky=W)
        street_adr.grid(row=9, column=0, columnspan=2, padx=20, pady=(0, 10), sticky=W)

        cityl.grid(row=8, column=1, padx=50, pady=(10, 0), columnspan=2)
        city.grid(row=9, column=1, padx=(45,0), pady=(0, 10), columnspan=2)

        provl.grid(row=8, column=3, pady=(10, 0), sticky=W)
        province.grid(row=9, column=3, pady=(0, 10), sticky=W)

        zipl.grid(row=8, column=4, padx=20, pady=(10, 0), sticky=W)
        zipcode.grid(row=9, column=4, padx=20, pady=(0, 10))

        cpl.grid(row=10, column=0, padx=20, pady=(10, 0), sticky=W)
        contact_no.grid(row=11, column=0, padx=20, pady=(0, 10))

        emaill.grid(row=10, column=1, padx=20, pady=(10, 0), columnspan=2, sticky=W)
        email.grid(row=11, column=1,  padx=20, pady=(0, 10), columnspan=2, sticky=W)

        order_label.grid(row=12, column=0, padx=20, pady=(10, 0), sticky=W)
        orderbox.grid(row=13, column=0, padx=20, pady=(0, 10))
        td.grid(row=13, column=0, sticky=W, padx=20, pady=(0, 10))
        t.grid(row=13, column=0, sticky=E, padx=20,  pady=(0, 10))
        t.deselect()

        rc_l.grid(row=12, column=1, padx=20, pady=(10, 0), columnspan=2, sticky=W)
        reward_card.grid(row=13, column=1,  padx=20, pady=(0, 10), columnspan=2, sticky=W)

        submit_info.grid(row=12, column=3, rowspan=2, columnspan=6, pady=10)

        mi.insert(0, 'f')
        last_name.insert(0, 'davis')
        street_adr.insert(0, 'grove st.')
        city.insert(0, 'san andreas')
        province.insert(0, 'wu han')
        zipcode.insert(0, '4327')
        contact_no.insert(0, '09989888998')
        email.insert(0, 'lamardavis@gmail.com')
        reward_card.insert(0, '4444444444444444')

    def get_info(customer_type):
        customer_info=[]
        orders_str = str(orders)
        if customer_type == 'existing':
            order_typexf = orderx_type.get()
            reward_cardxf = reward_cardx.get()
            customer_info.append(order_typexf)
            customer_info.append(reward_cardxf)
            confirm(customer_type, customer_info, orders_str)
            print(customer_info)
        elif customer_type == 'new':
            first_namef = first_name.get()
            mif= mi.get()
            last_namef=last_name.get()
            genderf= gender.get()
            street_adrf= street_adr.get()
            cityf= city.get()
            provincef= province.get()
            zipcodef= zipcode.get()
            contact_nof= contact_no.get()
            emailf= email.get()
            order_typef= order_type.get()
            reward_cardf= reward_card.get()

            customer_info.append(reward_cardf)
            customer_info.append(first_namef)
            customer_info.append(mif)
            customer_info.append(last_namef)
            customer_info.append(genderf)
            customer_info.append(street_adrf)
            customer_info.append(cityf)
            customer_info.append(provincef)
            customer_info.append(zipcodef)
            customer_info.append(contact_nof)
            customer_info.append(emailf)
            customer_info.append(order_typef)
            print(customer_info)
            confirm(customer_type, customer_info, orders_str)

    def confirm(customer_type, customer_info, orders_str):
        cus_len = len(customer_info)
        if customer_info == []:
            messagebox.showerror("Empty Fields", "Please Fill up the required fields first. Thank You.")
        elif customer_type=='existing':
            if customer_info[0]=='0':
                messagebox.showerror("Incomplete Fields", "Please Fill up the required fields first. Thank You.")

            else:
                response= messagebox.askquestion("Finalize Order", "Confirm Order?")
                if response == "yes":
                    conn = sqlite3.connect('Jollibae_orders.db')
                    c = conn.cursor()
                    c.execute("INSERT INTO order_tbl VALUES (:items_qty, :date_time, :order_type, :total_price)",
                              {
                                  'items_qty': orders_str,
                                  'date_time': datet,
                                  'order_type': customer_info[0],
                                  'total_price': total_v
                              })

                    c.execute("SELECT oid FROM order_tbl")
                    order_nol = c.fetchall()
                    order_no = str(order_nol[-1][0])


                    c.execute("SELECT orders FROM customer_tbl WHERE reward_card = :reward_card",
                              {
                                  'reward_card': customer_info[1]
                               })
                    orders_up = c.fetchall()
                    orders_up = orders_up[0][0] + ', ' + order_no

                    c.execute("""UPDATE customer_tbl SET
                        orders = :orders 
                        WHERE reward_card = :reward_card""",
                              {
                                  'orders': orders_up,
                                  'reward_card': customer_info[1]
                              })

                    for order in orders:
                        item = order[1]
                        qty_sale = order[0]
                        price_sale = order[3]

                        c.execute("SELECT item_sold, total FROM sales_tbl WHERE item = :item",
                                  {
                                      'item': item
                                  })
                        sales_up = c.fetchall()
                        print(sales_up)
                        sales_up_qty = sales_up[0][0] + qty_sale
                        sales_up_price = sales_up[0][1] + price_sale

                        c.execute("""UPDATE sales_tbl SET
                        item_sold = :item_sold, total = :total
                        WHERE item = :item""",
                              {
                                  'item_sold': sales_up_qty,
                                  'total': sales_up_price,
                                  'item': item
                              })

                    conn.commit()
                    conn.close()
                else: pass
        elif (customer_type=='new'):
            if cus_len!=12:
                messagebox.showerror("Incomplete Fields", "Please Fill up the required fields first. Thank You.")

            else:
                response = messagebox.askquestion("Finalize Order", "Confirm Order?")
                if response == "yes":
                    conn = sqlite3.connect('Jollibae_orders.db')
                    c = conn.cursor()
                    c.execute("INSERT INTO order_tbl VALUES (:items_qty, :date_time, :order_type, :total_price)",
                              {
                                  'items_qty': orders_str,
                                  'date_time': datet,
                                  'order_type': customer_info[-1],
                                  'total_price': total_v
                              })

                    c.execute("SELECT oid FROM order_tbl")
                    order_nol = c.fetchall()
                    order_no = str(order_nol[-1][0])

                    c.execute("INSERT INTO customer_tbl VALUES (:reward_card, :first_name, :mi, :last_name, :gender, :street_adr, :city, :province, :zipcode, :contact_no, :email, :orders)",
                              {
                                  'reward_card': customer_info[0],
                                  'first_name': customer_info[1],
                                  'mi': customer_info[2],
                                  'last_name': customer_info[3],
                                  'gender': customer_info[4],
                                  'street_adr': customer_info[5],
                                  'city': customer_info[6],
                                  'province': customer_info[7],
                                  'zipcode': customer_info[8],
                                  'contact_no': customer_info[9],
                                  'email': customer_info[10],
                                  'orders': order_no
                              })

                    for order in orders:
                        item = order[1]
                        qty_sale = order[0]
                        price_sale = order[3]

                        c.execute("SELECT item_sold, total FROM sales_tbl WHERE item = :item",
                                  {
                                      'item': item
                                  })
                        sales_up = c.fetchall()
                        print(sales_up)
                        sales_up_qty = sales_up[0][0] + qty_sale
                        sales_up_price = sales_up[0][1] + price_sale

                        c.execute("""UPDATE sales_tbl SET
                        item_sold = :item_sold, total = :total
                        WHERE item = :item""",
                              {
                                  'item_sold': sales_up_qty,
                                  'total': sales_up_price,
                                  'item': item
                              })

                    conn.commit()
                    conn.close()
                else:
                    pass

    # frame 1
    frame1 = LabelFrame(checkout, padx=10, pady=20, borderwidth=0, highlightthickness=0, bg='#272727')
    frame1.grid(row=1, column=0, sticky='nsew')

    #express order
    eo_l = Label(frame1, text='Express Order', pady=20, padx=20, bg='#303030', fg='#ffffff', font=('Arial Rounded MT Bold', 18), anchor=W)
    eo_l.grid(row=0, columnspan=5, sticky='nsew',  pady=(0,10))

    orderx_type= StringVar()
    orderx_label= Label(frame1, bg='#303030', fg='#ffffff', text='Order Type', font=('Arial Bold', 15))
    orderx_label.grid(row=1, column=0, padx=20, pady=(10, 0), sticky=W)
    orderxbox = Label(frame1, font=('Arial', 18), width=14, bg='#272727')
    orderxbox.grid(row=2, column=0, padx=20, pady=(0, 10))
    Checkbutton(frame1, text='Dine-In', variable=orderx_type, onvalue='Dine-In', font=('Arial Bold', 13),width=5).grid(row=2, column=0, sticky=W, padx=20,  pady=(0, 10))
    tx=Checkbutton(frame1, text='Take-Out', variable=orderx_type, onvalue='Take-out', font=('Arial Bold', 13),)
    tx.grid(row=2, column=0, sticky=E, padx=20,  pady=(0, 10))
    tx.deselect()

    rcx_l = Label(frame1, bg='#303030', fg='#ffffff', text='Jollireward Card No.', font=('Arial Bold', 15))
    rcx_l.grid(row=1, column=1, padx=20, pady=(10, 0), columnspan=2, sticky=W)
    reward_cardx = Entry(frame1, font=('Arial', 18), width=20)
    reward_cardx.grid(row=2, column=1,  padx=20, pady=(0, 10), columnspan=2, sticky=W)

    submit_infox= Button(frame1, text="Submit and Confirm Order", bg='red', fg='#ffffff', font=('Arial Bold', 18), command=lambda: get_info('existing'))
    submit_infox.grid(row=1, column=3, rowspan=2, columnspan=2, pady=10)

    registerb = Button(frame1, text="Register for Express Order           >", bg='#58E3E4', font=('Arial Rounded MT Bold', 12), width=30, command=register)
    registerb.grid(row=3, sticky=E, columnspan=2)

    reward_cardx.insert(0, '4444444444444444')

    #register objects
    first_namel = Label(frame1, bg='#303030', fg='#ffffff', text='First Name', font=('Arial Bold', 15))
    first_name = Entry(frame1, font=('Arial', 18), width=15)

    mi_l = Label(frame1, bg='#303030', fg='#ffffff', text='M.I.', font=('Arial Bold', 15))
    mi = Entry(frame1, font=('Arial', 18), width=3)

    last_namel = Label(frame1, bg='#303030', fg='#ffffff', text='Last Name', font=('Arial Bold', 15))
    last_name = Entry(frame1, font=('Arial', 18), width=15)

    gender = StringVar()
    genderl = Label(frame1, bg='#303030', fg='#ffffff', text='Gender', font=('Arial Bold', 15))
    genderbox = Label(frame1, font=('Arial', 18), width=12, bg='#272727')
    g1=Radiobutton(frame1, text='Male', variable=gender, value='Male', font=('Arial Bold', 13), width=5)
    g2=Radiobutton(frame1, text='Female', variable=gender, value='Female', font=('Arial Bold', 13), )

    street_adrl = Label(frame1, bg='#303030', fg='#ffffff', text='Address/Street', font=('Arial Bold', 15))
    street_adr = Entry(frame1, font=('Arial', 18), width=20)

    cityl = Label(frame1, bg='#303030', fg='#ffffff', text='City/Municipality', font=('Arial Bold', 15))
    city = Entry(frame1, font=('Arial', 18), width=15)

    provl = Label(frame1, bg='#303030', fg='#ffffff', text='Province', font=('Arial Bold', 15))
    province = Entry(frame1, font=('Arial', 18), width=15)

    zipl = Label(frame1, bg='#303030', fg='#ffffff', text='ZIP Code', font=('Arial Bold', 15))
    zipcode = Entry(frame1, font=('Arial', 18), width=9)

    cpl = Label(frame1, bg='#303030', fg='#ffffff', text='Contact No.', font=('Arial Bold', 15))
    contact_no = Entry(frame1, font=('Arial', 18), width=15)

    emaill = Label(frame1, bg='#303030', fg='#ffffff', text='Email', font=('Arial Bold', 15))
    email = Entry(frame1, font=('Arial', 18), width=20)

    order_type = StringVar()
    order_label = Label(frame1, bg='#303030', fg='#ffffff', text='Order Type', font=('Arial Bold', 15))
    orderbox = Label(frame1, font=('Arial', 18), width=12, bg='#272727')

    td=Checkbutton(frame1, text='Dine-In', variable=order_type, onvalue='Dine-In', font=('Arial Bold', 13), width=5)
    t = Checkbutton(frame1, text='Take-Out', variable=order_type, onvalue='Take-out', font=('Arial Bold', 13))

    rc_l = Label(frame1, bg='#303030', fg='#ffffff', text='Jollireward Card No.', font=('Arial Bold', 15))
    reward_card = Entry(frame1, font=('Arial', 18), width=20)

    submit_info = Button(frame1, text="Submit and Confirm Order", bg='red', fg='#ffffff', font=('Arial Bold', 18),
                         command=lambda: get_info('new'))

    #print orders
    frame3 = LabelFrame(checkout, padx=10, pady=10, borderwidth=0, highlightthickness=0)
    frame3.grid(row=1, column=2, sticky='nsew')

    qtyd = Label(frame3, text='Qty.', bg='#272727', fg='#ffffff', font=('Arial', 15))
    qtyd.grid(row=0, sticky=W + E)

    itemd = Label(frame3, text='Item', font=('Arial Bold', 15), width=13)
    itemd.grid(row=0, column=1)

    priced = Label(frame3, text='Price', bg='#272727', fg='#ffffff', font=('Arial', 15), width=9)
    priced.grid(row=0, column=2)

    r = 1
    for order in orders:
        qtlab = Label(frame3, text=order[0], font=('Arial Bold', 12), width=4)
        qtlab.grid(row=r, column=0, padx=5, pady=5)

        itp = Label(frame3, text=order[1], font=('Arial Bold', 10))
        itp.grid(row=r, column=1, sticky=W + E)

        pstr = "PHP " + str(order[3]) + ".00"
        plp = Label(frame3, text=pstr, font=('Arial Bold', 10))
        plp.grid(row=r, column=2, sticky=W + E)

        r += 1

    total_v = 0
    for subtotal in orders:
        total_v += subtotal[3]

    total_str = 'Total: PHP ' + str(total_v) + '.00'

    total_l = Label(frame3, text=total_str, bg='#272727', fg='#ffffff', font=('Arial Bold', 15), anchor=E, padx=5,
                    pady=5)
    total_l.grid(row=r, columnspan=3, sticky=W + E, pady=5)

    items_qtyl = []
    for order in orders:
        items_qty = str(order[0]) + order[1]
        items_qtyl.append(items_qty)

    checkout.mainloop()

confirm_order([[1, '2 - pc. Chickenjoyy Solo', 168, 168], [2, '1 - pc. Chickenjoyy Solo', 84, 168]], 'lamar')
