import sqlite3
import items

conn = sqlite3.connect('Jollibae_orders.db')

c = conn.cursor()

c.execute("""CREATE TABLE customer_tbl (
		reward_card integer,
		first_name text,
		mi text,
		last_name text,
		gender text,
		street_adr text,
		city text,
		province text,
		zipcode integer,
		contact_no integer,
		email text,
		orders text
		)""")

c.execute("""CREATE TABLE order_tbl (
		items_qty text,
		date_time text,
		order_type text,
		total_price integer		
		)""")

c.execute("""CREATE TABLE sales_tbl (
		item text,
		item_sold integer,
		total integer		
		)""")

items = [items.opccs(), items.tpccs(), items.ys(), items.cys(), items.bcys(), items.cdys(), items.aays(), items.jss(),
         items.jsfp(), items.fpd(), items.opbss(), items.tpbss(), items.spbsfp(), items.epbsfp(), items.ps(), items.pfp(),
         items.fpd(), items.bsmtp(), items.bsmt(), items.iccj(), items.ic(), items.it(),
         items.hmd(), items.tid(), items.cms(), items.er()]

for item in items:
    c.execute("INSERT INTO sales_tbl VALUES (:item, :item_sold, :total)",
                                  {
                                      'item': item.name,
                                      'item_sold': 0,
                                      'total': 0
                                  })

conn.commit()
conn.close()
