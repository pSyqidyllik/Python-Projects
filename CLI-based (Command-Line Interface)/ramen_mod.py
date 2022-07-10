import time
from datetime import date

#intial
# get current date
today = date.today()
total=0

def menu():
    print('Welcome to Ichiraku Ramen!')
    time.sleep(1)
    print('')
    print('---------------------------------------')
    print('          R A M E N  (M E N U)        ')
    print('---------------------------------------')
    print(' (PL)  Plain Ramen.............P99.00')
    print(' (TK)  Tonkatsu Ramen..........P159.00')
    print(' (MS)  Miso Ramen..............P169.00')
    print(' (CT)  Cheesy Tonkatsu Ramen...P169.00')
    print(' (ST)  Spicy Tonkatsu Ramen....P179.00')
    print(' (IB)  Ichiban Ramen...........P189.00')
    print(' (SI)  Spicy Ichiban Ramen.....P199.00')
    print('---------------------------------------')
    print('')

class Ramen(object):
    def __init__(self, spec, quantity):
        self.spec = spec
        self.quantity = int(quantity)

    def show(self):
        print('\nYour order is ({}) {} Ramen...'.format(self.quantity, self.spec))

    def total(self):
        # menu item prices
        if self.spec == 'PL':
            price = 99
        elif self.spec == 'TK':
            price = 159
        elif self.spec == 'MS':
            price = 169
        elif self.spec == 'CT':
            price = 169
        elif self.spec == 'ST':
            price = 179
        elif self.spec == 'IB':
            price = 189
        elif self.spec == 'SI':
            price = 199
        else:
            print('Invalid input...')
            return spec

        # calculate order
        curprice = self.quantity * price
        return curprice

#start
menu()
time.sleep(1)

orderl = []
spec = input('>>> What is your order? ').upper()
quantity = int(input('>>> How many? '))
orderl.append([spec,quantity])

spec = input('>>> Anything else you would like to add? If none, please enter NO to proceed to checkout.').upper()

while spec != 'NO':
    quantity = int(input('>>> How many? '))
    orderl.append([spec, quantity])
    spec = input('>>> Anything else you would like to add? If none, please enter NO to proceed to checkout.').upper()

customer_name = input('>>> Name: ').upper()
customer_address = input('>>> Address: ').upper()

#order proper
stotal = []
for order in orderl:
    ordern = Ramen(order[0],order[1])
    ordern.show()
    time.sleep(1)
    stotal.append(ordern.total())

for totala in stotal:
    total += totala
print('Total amount of your order is P{}.00 ( P{}.00 + P10.00 delivery fee)'.format(total + 10, total))


def receipt():
    pay = int(input('\nChoose payment method: (1) E-wallet / (2) Cash-on-Delivery '))
    if pay == 1:
        p = 'E-WALLET'
        print('\nPayment received. Thank you have a nice day!')
        time.sleep(1)
    elif pay == 2:
        p = 'COD'
        print('\nWait for your order to arrive. Please prepare the exact amount of cash for your order.')
        print('Thank you have a nice day!')
        time.sleep(1)
    else:
        print('\nInvalid input...')
        return pay

    # print receipt
    print('')
    print('---------------------------------------')
    print('       R A M E N  R E C E I P T        ')
    print('---------------------------------------')
    print('NAME:', customer_name)
    print('ADDRESS:', customer_address)
    print('DATE:', today)
    print('---------------------------------------')
    print('ORDER:')

    n = 0
    for order in orderl:
        ordern = Ramen(order[0], order[1])
        print('  ({})  {} RAMEN     P{}.00'.format(ordern.quantity, ordern.spec, stotal[n]))
        n = n+1
        print('')

    print('  DELIVERY FEE      P10.00')
    print('')
    print('  TOTAL AMOUNT:     P{}.00'.format(total + 10))

    print('  PAYMENT METHOD:  ', p)
    print('---------------------------------------')
    print('      Thank you for your purchase!     ')
    print('---------------------------------------')

receipt()
