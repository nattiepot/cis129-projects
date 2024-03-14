# Natalie O.
# 3/14/2024
# calculates how much money is earned for returning bottles for a week
# Lab 5:Bottle Return Program

# declare variables
totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0
keepGoing = 'y'
numOfDays = 7

# loop to run program again
while keepGoing == 'y':

    # code to set/reset value of variables
    totalBottles = 0
    counter = 1
    todayBottles = 0
    totalPayout = 0

    # loop to declare total bottles for the week
    while counter <= numOfDays:
        todayBottles = int(input(f'Enter number of bottles returned for day# {counter}: '))
        totalBottles += todayBottles
        counter +=1

    # calculates total payout
    payoutPerBottle = .10
    totalPayout = 0
    totalPayout = totalBottles * payoutPerBottle

    # prints totalBottles and totaltPayout
    print(f'\nTotal bottles collectes is: {totalBottles}')
    print(f'Total paid out is: ${totalPayout:.1f}')

    # prompts user to enter more data
    print('\nDo you want to enter another week\'s worth of data?')
    keepGoing = input(('(Enter y or n): '))

