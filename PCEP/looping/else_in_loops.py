#!/usr/local/bin/python3.8


##################################################
print('While loop')
##################################################
count = 1

while count <= 3:
    print (count)
    count += 1
else:
    print('while loop has completed')


##################################################
print('\nElse loop')
##################################################

for each_number in (1, 2, 3):
    print(each_number)
else:
    print('for loop has completed')


##################################################
print('\nReal life applications and use\n')
##################################################

colours = ['red', 'white', 'blue', 'purple', 'orange']

for colour in colours:
    if colour == 'purple':
        print('The colour', colour, 'is in the list')
        break
else:
    print('The colour purple is not in the list')


# You should only really use the else statement in the for loop if you're using break inside the for loop.
