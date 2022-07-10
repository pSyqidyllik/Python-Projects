#Burgers
class Burger(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.th = th

class ys(Burger):
    def __init__(self):
        self.name = 'Yummburger Solo'
        self.price = 39
        self.th = 'assets/ys.png'

class cys(Burger):
    def __init__(self):
        self.name = 'Yummcheezeburger Solo'
        self.price = 54
        self.th = 'assets/cys.png'

class bcys(Burger):
    def __init__(self):
        self.name = 'Yummbaconcheezyburger Solo'
        self.price = 72
        self.th = 'assets/bcys.png'

class aays(Burger):
    def __init__(self):
        self.name = 'Yummazingalohaburger Solo'
        self.price = 94
        self.th = 'assets/aays.png'

class cdys(Burger):
    def __init__(self):
        self.name = 'Yummcheezydeluxeburger Solo'
        self.price = 83
        self.th = 'assets/cdys.png'

#Chickens
class Chicken(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.th = th

class opccs(Chicken):
    def __init__(self):
        self.name = '1 - pc. Chickenjoyy Solo'
        self.price = 84
        self.th = 'assets/1pccs.png'

class tpccs(Chicken):
    def __init__(self):
        self.name = '2 - pc. Chickenjoyy Solo'
        self.price = 168
        self.th = 'assets/2pccs.png'


#Spaghetti
class Spaghetti(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.th = th

class jss(Spaghetti):
    def __init__(self):
        self.name = 'Jollyy Spaghetti Solo'
        self.price = 55
        self.th = 'assets/jss.png'

class jsfp(Spaghetti):
    def __init__(self):
        self.name = 'Jollyy Spaghetti Family Pan'
        self.price = 220
        self.th = 'assets/jsfp.png'

class fpd(Spaghetti):
    def __init__(self):
        self.name = 'Family Pan Duo'
        self.price = 549
        self.th = 'assets/fpd.png'

#Burger Steaks
class BurgerSt(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.stock = stock
        self.th = th

class spbsfp(BurgerSt):
    def __init__(self):
        self.name = '6-pc. Burger Steak Family Pan'
        self.price = 308
        self.th = 'assets/6pbsfp.png'

class epbsfp(BurgerSt):
    def __init__(self):
        self.name = '8-pc. Burger Steak Family Pan'
        self.price = 396
        self.th = 'assets/8pbsfp.png'

class opbss(BurgerSt):
    def __init__(self):
        self.name = '1-pc. Burger Steak Solo'
        self.price = 55
        self.th = 'assets/1pbss.png'

class tpbss(BurgerSt):
    def __init__(self):
        self.name = '2-pc. Burger Steak Solo'
        self.price = 96
        self.th = 'assets/2pbss.png'

#Palaboks
class Palabok(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.stock = stock
        self.th = th

class ps(Palabok):
    def __init__(self):
        self.name = 'Palabok Solo'
        self.price = 109
        self.th = 'assets/ps.png'

class pfp(Palabok):
    def __init__(self):
        self.name = 'Palabok Family Pan'
        self.price = 352
        self.th = 'assets/pfp.png'

class fpd(Palabok):
    def __init__(self):
        self.name = 'Family Pan Duo'
        self.price = 549
        self.th = 'assets/fpd.png'

#Beverages
class Beverages(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.th = th

class bsmtp(Beverages):
    def __init__(self):
        self.name = 'Brown Sugar Milk Tea w/ Pearls'
        self.price = 83
        self.th = 'assets/bsmtp.png'

class bsmt(Beverages):
    def __init__(self):
        self.name = 'Brown Sugar Milk Tea'
        self.price = 55
        self.th = 'assets/bsmt.png'

class iccj(Beverages):
    def __init__(self):
        self.name = 'Iced Coffee w/ Coffee Jelly'
        self.price = 65
        self.th = 'assets/iccj.png'

class ic(Beverages):
    def __init__(self):
        self.name = 'Iced Coffee'
        self.price = 43
        self.th = 'assets/ic.png'

class it(Beverages):
    def __init__(self):
        self.name = 'Iced Tea'
        self.price = 61
        self.th = 'assets/it.png'

#Additionals
class Additionals(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.th = th


class hmd(Additionals):
    def __init__(self):
        self.name = 'Honey Mustard Dip'
        self.price = 11
        self.th = 'assets/hmd.png'

class tid(Additionals):
    def __init__(self):
        self.name = 'Thousand Island Dip'
        self.price = 11
        self.th = 'assets/tid.png'

class cms(Additionals):
    def __init__(self):
        self.name = 'Creamy Macaroni Soup'
        self.price = 44
        self.th = 'assets/cms.png'

class er(Additionals):
    def __init__(self):
        self.name = 'Extra Rice'
        self.price = 33
        self.th = 'assets/er.png'

