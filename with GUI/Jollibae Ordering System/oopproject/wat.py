    def spinboxchange(qt, pr):
        qtc = qt.get()

        if qtc == 0:
            print("wala")

        p1 = int(qtc) * pr
        p1l = "PHP " + str(p1) + ".00"
        p1 = Label(frame3, text=p1l, font=('Arial Bold', 10))
        p1.grid(row=2, column=2, sticky=W + E)

    #change to print order
    def order(qt, it, pr):

        qts = Spinbox(frame3, from_=0, to=10, font=('Arial Bold', 10), width=1, textvariable=qt, command=lambda: spinboxchange(qt, pr))
        qts.grid(row=2, column=0, sticky=W + E)

        it1 = Label(frame3, text=it, font=('Arial Bold', 10))
        it1.grid(row=2, column=1, sticky=W + E)

        p1l = "PHP " + str(pr) + ".00"
        p1 = Label(frame3, text=p1l, font=('Arial Bold', 10))
        p1.grid(row=2, column=2, sticky=W + E)

def spaghetti_cat():
    global frame2
    global cat
    global itl1, thl1, itl2, thl2, itl3, thl3
    cat = "Spaghetti"

    frame2.grid_forget()
    frame2 = LabelFrame(root, padx=10, pady=20, borderwidth=0, highlightthickness=0, bg='#303030')
    frame2.grid(row=1, column=1)

    catt = Label(frame2, text=cat, pady=20, padx=20, bg='#272727', fg='#ffffff', font=('Arial Rounded MT Bold', 18), anchor=W)
    catt.grid(row=0, columnspan=4, sticky='nsew', pady=20)

    # item 1
    itl1=spaghettil[0].name + "\nPHP " + str(spaghettil[0].price) + ".00"
    thl1=ImageTk.PhotoImage(Image.open(spaghettil[0].th))
    itembt = Label(frame2, image=thl1, bg='#272727')
    itembt.grid(row=1, column=0, padx=15)
    itemb = Button(frame2, text=itl1, bg='#58E3E4', fg='#000000', font=('Arial Rounded MT Bold', 12))
    itemb.grid(row=2, column=0, sticky=W + E, padx=15)

    # item 2
    itl2 = spaghettil[1].name + "\nPHP " + str(spaghettil[1].price) + ".00"
    thl2 = ImageTk.PhotoImage(Image.open(spaghettil[1].th))
    itembt = Label(frame2, image=thl2, bg='#272727')
    itembt.grid(row=1, column=1, padx=15)
    itemb = Button(frame2, text=itl2, bg='#58E3E4', fg='#000000', font=('Arial Rounded MT Bold', 12))
    itemb.grid(row=2, column=1, sticky=W + E, padx=15)

    # item 3
    itl3 = spaghettil[2].name + "\nPHP " + str(spaghettil[2].price) + ".00"
    thl3 = ImageTk.PhotoImage(Image.open(spaghettil[2].th))
    itembt = Label(frame2, image=thl3, bg='#272727')
    itembt.grid(row=1, column=2, padx=15)
    itemb = Button(frame2, text=itl3, bg='#58E3E4', fg='#000000', font=('Arial Rounded MT Bold', 12))
    itemb.grid(row=2, column=2, sticky=W + E, padx=15)

    def insert():
        conn = sqlite3.connect('Jollibae_orders.db')
        c = conn.cursor()

        c.execute("INSERT INTO order_tbl VALUES (:items_qty, :total_price)",
                {
                    'items_qty': items_qty.get(),
                    'total_price': total_price.get(),
                })

        conn.commit()
        conn.close()

#def proceed, command confirm sa button, def confirm order