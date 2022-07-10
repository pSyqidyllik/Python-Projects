from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import datetime
import sqlite3
from tkinter import messagebox


#created file
import items

c.execute("SELECT orders FROM customer_tbl WHERE reward_card = :reward_card")
                records = c.fetchall()

                c.execute("""UPDATE customer_tbl SET
                    orders = :orders 
                    WHERE reward_card = :reward_card""",
                          {
                              'orders': orders_editor.get(),
                              'reward_card': reward_card
                          })

reward_cardx.insert(0, '4444444444444444')

mi.insert(0, 'f')
last_name.insert(0, 'davis')
street_adr.insert(0, 'grove st.')
city.insert(0, 'san andreas')
province.insert(0, 'wu han')
zipcode.insert(0, '4327')
contact_no.insert(0, '09989888998')
email.insert(0, 'lamardavis@gmail.com')
reward_card.insert(0, '4444444444444444')