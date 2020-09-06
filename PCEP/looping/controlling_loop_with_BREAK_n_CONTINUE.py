#!/usr/local/bin/python3.8

print ('\nBreak and Continue\n')

# Controlling loop execution with 'break' and 'continue'


##################################
# CONTINUE
##################################
'''
Continue: you go to the next iteration of the loop
and you won't go further with anything after the 'continue' keyword
i.e. it'll stop the current iteration of the loop and go to the next
'''

print ('CONTINUE CONDITION')

count = 0

while count <= 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f'This is an odd number: {count}')       # is a short hand for doing string formatting
    count += 1

# print('This is an odd number:', count)  == print(f'This is an odd number: {count}')


##################################
# BREAK
##################################
'''
Break: stops the execution of the loop entirely
i.e. it will not go to the next itteration.
'''

print ('\nBreak CONDITION\n')

count = 1
while count < 10:
    if count % 2 == 0:
        count += 1
        break
    print(f'This is an odd number: {count}')
    count += 1


##################################
# EXAMPLE
##################################
colours = ['red', 'pink', 'blue', 'purple']

for colour in colours:
    if colour == 'red':
        continue
    elif colour == 'blue':
        break
    else:
        print(f'\nThe colour: {colour}\n')

# only 'pink' should be printed
    # red ==> continue = cancel current itteration
    # pink ==> print the colour
    # blue ==> break = cancel the entire parent looping system