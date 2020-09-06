#!/usr/local/bin/python3.8

print ('If and else statement')

print ( 'a\'s value is:', ord('a') )
print ( 'b\'s value is:', ord('b') )


print ( 'is a less than b:', 'a' < 'b' )

if 'a' < 'b':
    print ("\nYou've got the right answer\n")

if True:                                                # This was always print the True (first) condition
    print ('This is a True statement')
else:
    print ('This is a False statement')


if False:                                                # This was always print the False (second) condition
    print ('This is a True statement')
else:
    print ('This is a False statement')