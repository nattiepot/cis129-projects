# Author: Natalie O.
# lab 3 in my cis129 course
# a short program in Python that asks the user for the number of coffee and muffins they are purchasing

# cup of coffee is $5 and the price of a muffin is $4
# 6% sales tax on order

print('My Coffee and Muffin Shop')
aCoffees = int(input('Number of Coffees bought?\n'))
aMuffins = int(input('Number of Muffins bought?\n'))

priceCoffees= aCoffees * 5.00
priceMuffins= aMuffins * 4.00

print('My Coffee and Muffin Shop Reciept')
print(aCoffees , 'Coffee at $5 each: $' ,priceCoffees)
print(aMuffins, 'Muffins at $4 each: $' ,priceMuffins)
tax= (priceCoffees + priceMuffins) * .06
print('6% tax: $' ,tax)
print('--------')
print('Total: $' ,priceCoffees + priceMuffins + tax)
