# Author: Natalie O.
# lab 3 in my cis129 course
# a short program in Python that asks the user for the number of coffee and muffins they are purchasing

# cup of coffee is $5 and the price of a muffin is $4
# 6% sales tax on order

# cup of tea is $3 and a scone is $4

print('♡Welcome to Cafe Nattie!♡')

customerName = input('Can I please get a name for this order?\n')
print('Great, thanks!')
aCoffees = int(input('How many cups of coffee would you like?\n'))
aTeas = int(input('How many cups of tea would you like\n'))
aMuffins = int(input('How many muffins would you like?\n'))
aScones = int(input('How many scones would you like?\n'))


priceCoffees= aCoffees * 5.00
priceTeas= aTeas * 3.00
priceMuffins= aMuffins * 4.00
priceScones= aScones * 4.00

print('\n♡Cafe Nattie Reciept♡\n\t for', '♡',customerName,'♡')
print(aCoffees , 'Cups of Coffee at $5 each: $' ,priceCoffees)
print(aTeas , 'Cups of Tea at $3 each: $' ,priceTeas)
print(aMuffins, 'Muffins at $4 each: $' ,priceMuffins)
print(aScones, 'Scones at $4 each: $' , priceScones)
tax= (priceCoffees + priceTeas + priceMuffins + priceScones) * .06
print('6% tax: $' ,tax)
print('--------')
print('Total: $' ,priceCoffees + priceTeas + priceMuffins + priceScones + tax)

print('♡Thanks for visiting Cafe Nattie!♡\n\t ♡We hope to see you again soon, ',customerName,'!♡')
