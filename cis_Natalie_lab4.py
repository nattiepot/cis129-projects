# Module 4 lab 4
# Natalie Orcutt
# 2/27/24
# takes a stores monthly sales and percent increase in sales and determines what store and employee bonuses are applied

monthlySales = 0    #monthly sales amount
storeAmount = 0     #store bonus amount
empAmount = 0       #employee bonus amount
salesIncrease = 0   #percent of sales increase
prompt = ('Please enter your monthly sales. ')

#this gets monthly sales
monthlySales = float(input(prompt))


#this determines the store bonus
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0




#this gets the percent increase in sales
salesIncrease = float(input('Please enter your percent of sales increase. '))
salesIncrease = salesIncrease / 100


#this determines employee bonus
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0


#this prints bonus info
print('The store bonus amount is $',storeAmount)
print('The employee bonus is $',empAmount)
if (storeAmount == 6000) and (empAmount == 75):
    print('Congrats! You have reached the highest bonus amounts possible!')